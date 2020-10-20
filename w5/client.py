import time
import socket
import operator


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

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

        message_encoded = b""

        while not message_encoded.endswith(b"\n\n"):
            try:
                message_encoded += self.connection.recv(1024)
            except socket.error as identifier:
                raise ClientError("Client: put (recv)", identifier)

        message = message_encoded.decode()

        if message != "ok\n\n":
            raise ClientError("Client: put (decode)")

    def get(self, metric):
        try:
            self.connection.sendall(
                ("get {}\n".format(metric)).encode()
            )
        except socket.error as identifier:
            raise ClientError("Client: get", identifier)

        message_encoded = b""

        while not message_encoded.endswith(b"\n\n"):
            try:
                message_encoded += self.connection.recv(1024)
            except socket.error as identifier:
                raise ClientError("Client: get (recv)", identifier)

        message = message_encoded.decode()
        
        status, payload = message.split("\n", 1)

        if status == "ok":
            data = {}

            try:
                for line in payload.split("\n"):
                    if not line == "":
                        metric, value, timestamp = line.split(" ")
                        if metric not in data:
                            data[metric] = []
                        data[metric].append((int(timestamp), float(value)))
            except BaseException as identifier:
                raise ClientError("Client: get (split)", identifier)

            for key in data:
                (data[key]).sort(key=operator.itemgetter(0))

            return data
        else:
            raise ClientError(payload)

    def close(self):
        try:
            self.connection.close()
        except socket.error as identifier:
            raise ClientError("Client: close", identifier)


if __name__ == "__main__":
    my_list = [(1501865247, 13.045), (1501864247, 10.5), (1501864243, 11.0), (1501864248, 22.5)]
    my_dict = {'unsorted_data': my_list}

    my_list.sort(key = operator.itemgetter(0))

    # print(my_list)

    # for item in my_dict:
    #     print(my_dict[item])

    for item in my_dict.items():
        print(item)





# import bisect
# import socket
# import time


# class ClientError(Exception):
#     """класс исключений клиента"""
#     pass


# class Client:
#     def __init__(self, host, port, timeout=None):
#         self.host = host
#         self.port = port
#         self.timeout = timeout

#         try:
#             self.connection = socket.create_connection((host, port), timeout)
#         except socket.error as err:
#             raise ClientError("Cannot create connection", err)

#     def _read(self):

#         data = b""

#         while not data.endswith(b"\n\n"):
#             try:
#                 data += self.connection.recv(1024)
#             except socket.error as err:
#                 raise ClientError("Error reading data from socket", err)

#         return data.decode('utf-8')

#     def _send(self, data):

#         try:
#             self.connection.sendall(data)
#         except socket.error as err:
#             raise ClientError("Error sending data to server", err)

#     def put(self, key, value, timestamp=None):

#         timestamp = timestamp or int(time.time())
#         self._send(f"put {key} {value} {timestamp}\n".encode())
#         raw_data = self._read()

#         if raw_data == 'ok\n\n':
#             return
#         raise ClientError('Server returns an error')

#     def get(self, key):

#         self._send(f"get {key}\n".encode())
#         raw_data = self._read()
#         data = {}
#         status, payload = raw_data.split("\n", 1)
#         payload = payload.strip()

#         if status != 'ok':
#             raise ClientError('Server returns an error')

#         if payload == '':
#             return data

#         try:

#             for row in payload.splitlines():
#                 key, value, timestamp = row.split()
#                 if key not in data:
#                     data[key] = []
#                 bisect.insort(data[key], ((int(timestamp), float(value))))

#         except Exception as err:
#             raise ClientError('Server returns invalid data', err)

#         return data

#     def close(self):

#         try:
#             self.connection.close()
#         except socket.error as err:
#             raise ClientError("Error. Do not close the connection", err)