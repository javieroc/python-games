import socket
import random
import pickle
from _thread import *
import sys
from Player import Player

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                players[player] = data
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    currentPlayer = 0

    try:
        s.bind((socket.gethostname(), 3000))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        # positions.append((random.randint(0, 400), random.randint(0, 400)))

        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1


main()
