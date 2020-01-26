import socket

class Network(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 3000

    def getData(self):
        return self.data

    def connect(self):
        try:
            self.socket.connect((self.server, self.port))
            data = self.socket.recv(2048).decode()
            return data
        except:
            pass

    def send(self, data):
        try:
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
        except socket.error as err:
            print(err)
