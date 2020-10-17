import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as identifier:
            raise ClientError("Client: __init__", identifier)

    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or int(time.time())

        try:
            self.connection.sendall(
                ("put {} {} {}\n".format(metric, value, timestamp)).encode()
            )
        except socket.error as identifier:
            raise ClientError("Client: put", identifier)

        self.parser()

    def get(self, metric):
        try:
            self.connection.sendall(
                ("get {}\n".format(metric)).encode()
            )
        except socket.error as identifier:
            raise ClientError("Client: get", identifier)

        data_parsed = self.parser()

        data = {}
        if data_parsed == "":
            return data

        for line in data_parsed.split("\n"):
            metric, value, timestamp = line.split()
            if metric not in data:
                data[metric] = []
            data[metric].append((int(timestamp), float(value)))

        return data

    def parser(self):
        message_encoded = b""

        while not message_encoded.endswith(b"\n\n"):
            try:
                message_encoded += self.connection.recv(1024)
            except socket.error as identifier:
                raise ClientError("Client: parser", identifier)

        message = message_encoded.decode()

        status, data = message.split("\n", 1)
        data = data.strip()

        if status == "error":
            raise ClientError("Client: parser (error)")

        return data


if __name__ == "__main__":
    pass
