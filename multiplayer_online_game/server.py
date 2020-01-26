import socket
import random
from _thread import *
import sys

positions = [(0,0), (100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(transform_pos(positions[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())

            if not data:
                print("Disconnected")
                break
            else:
                positions[player] = data
                if player == 1:
                    reply = positions[0]
                else:
                    reply = positions[1]
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(transform_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


def read_pos(str_pos):
    pos = str_pos.split(',')
    return (int(pos[0]), int(pos[1]))


def transform_pos(tup_pos):
    return str(tup_pos[0]) + ',' + str(tup_pos[1])


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
