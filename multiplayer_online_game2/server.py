import pygame
import socket
import pickle
from _thread import *
from Player import Player

players = {}

def threaded_client(conn, player):
    conn.send(pickle.dumps(player))

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                players[player.id] = data

            print(players)
            conn.sendall(pickle.dumps(players))
        except:
            break

    print("Lost connection")
    conn.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    id = 0

    try:
        s.bind((socket.gethostname(), 3000))
    except socket.error as e:
        str(e)

    s.listen()
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        player = Player(id)
        players.update({id: player})
        start_new_thread(threaded_client, (conn, player))
        id += 1


main()
