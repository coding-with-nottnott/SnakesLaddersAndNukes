import socket
import _thread
import pickle
import game
import debug
import configparser
config = configparser.ConfigParser()

config.read('serverconfig.ini')
server = config['Server']['ip']
port = int(config['Server']['port'])

# server = "192.168.1.79"
# port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {}
game_id = 0
total_id_count = 0
p = 0
game_found = False

def threaded_client(conn, p, game_id, id_count, addr):
    global total_id_count

    connected = True
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "roll":
                        game.roll_dice(p)
                    elif data == "NUKE":
                        game.player_uses_nuke(p)
                    elif data in ("Blue", "Green", "Yellow", "Red"):
                        game.set_color(p, data)
                    elif data == "Ready Up":
                        game.player_ready_up(p)
                    elif data == "debug":
                        game.activate_debug(p)
                    elif data in ("Up", "Down", "Left", "Right"):
                        game.debug_move(p, data)
                    elif data in ("-1", "1", "2", "3", "4", "5", "6"):
                        value = int(data)
                        game.move_player(p, value)

                    # reply = game
                    conn.sendall(pickle.dumps(game))

                    if game.winner != 0:
                        break
            else:
                break
        except:
            break
    game.player_lost_connection(p, id_count)
    print("Lost connection to", addr, ", player", p, "in game", game_id)
    # total_id_count -= 1
    # if game_id in games:
    #     game = games[game_id]
    #     game.player_lost_connection(p)

    if game.num_of_players == 0:
        print("Closing game", game_id)
        del games[game_id]
    # id_count -= 1
    # conn.close()
    # del conn

def start_new_game(game_id):
    games[game_id] = game.Game(game_id)
    print("Creating game ID", game_id)

# def set_new_game_id(new_game_id):
#     global game_id
#     game_id = new_game_id

def start_new_threaded_client(p, unique_game_id):
    games[unique_game_id].new_player(p, id_count=total_id_count, debug=debug.debug)
    print(addr[0], "is player", p, "with ID", total_id_count, "joining game", unique_game_id)
    conn.send(str.encode(str(p)))
    _thread.start_new_thread(threaded_client, (conn, p, unique_game_id, total_id_count, addr))


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    total_id_count += 1

    # if game_id == None:
    #     game_id = 0
    #     start_new_game(game_id)

    if games:
        for id in games:
            if not game_found:
                if not games[id].started:
                    if games[id].num_of_players < 4:
                        for potential_player in range(1, 5):
                            if games[id].players[potential_player][5]:
                                p = potential_player
                                game_found = True
                                start_new_threaded_client(p, id)
                                break
            else:
                break
    if not game_found:
        p = 1
        start_new_game(game_id)
        start_new_threaded_client(p, game_id)
        game_id += 1
    game_found = False
