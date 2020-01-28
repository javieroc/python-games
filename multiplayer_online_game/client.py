import socket
import pickle


class Network(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 3000
        self.data = self.connect()

    def getData(self):
        return self.data

    def connect(self):
        try:
            self.socket.connect((self.server, self.port))
            return pickle.loads(self.socket.recv(2048))
        except socket.error as err:
            print(err)

    def send(self, data):
        try:
            self.socket.send(pickle.dumps(data))
            return pickle.loads(self.socket.recv(2048))
        except socket.error as err:
            print(err)
