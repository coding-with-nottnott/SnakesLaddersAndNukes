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
game_id = None
total_id_count = 0
p = 0

def threaded_client(conn, p, game_id, id_count):
    global total_id_count
    conn.send(str.encode(str(p)))
    print(id_count)

    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break


                else:
                    if game.players[p][5] == True:
                        game.new_player(p, debug = debug.debug)
                        game.append_id_count(id_count)
                    elif data == "roll":
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

                    reply = game
                    conn.sendall(pickle.dumps(reply))

                    if game.winner != 0:
                        break
            else:
                break
        except:
            break
    game.player_lost_connection(p, id_count)
    print("Lost connection")
    total_id_count -= 1
    # if game_id in games:
    #     game = games[game_id]
    #     game.player_lost_connection(p)

    if game.num_of_players == 0:
        print("Closing Game ", game_id)
        del games[game_id]
    # id_count -= 1
    # conn.close()
    del conn
    exit()

def start_new_game(game_id):
    games[game_id] = game.Game(game_id)
    print("Creating game ID", game_id)

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    total_id_count += 1

    if game_id == None:
        game_id = 0
        start_new_game(game_id)
    else:
        if not debug.debug:
            try:
                if games[game_id].id == game_id and games[game_id].started or games[game_id].num_of_players == 4:
                    game_id += 1
                    start_new_game(game_id)
            except KeyError:
                game_id += 1
                start_new_game(game_id)
        else:
            game_id += 1
            start_new_game(game_id)

    p = games[game_id].num_of_players + 1
    print(addr[0], "is player", p)
    _thread.start_new_thread(threaded_client, (conn, p, game_id, total_id_count))