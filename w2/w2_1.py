import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def del_temp_file():
    if os.path.isfile(storage_path):
        os.remove(storage_path)

class Database:
    def __init__(self):
        if os.path.isfile(storage_path):
            with open(storage_path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = dict()
    
    def add(self, key, value):
        if key not in self.data:
            self.data[key] = list()
        self.data[key].append(value)
        with open(storage_path, 'w') as f:
            json.dump(self.data, f)

    def get(self, key):
        if key in self.data:
            return ', '.join(self.data[key])
        else:
            return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clean', help="delete storage", action="store_true")
    parser.add_argument('-a', '--all', help="print all data", action="store_true")
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-v', '--value', type=str)
    args = parser.parse_args()

    storage = Database()

    if args.clean:
        del_temp_file()

    if args.all:
        if os.path.isfile(storage_path):
            print(json.dumps(storage.data, indent=2))

    if args.key:
        if args.value:
            storage.add(args.key, args.value)
        else:
            print(storage.get(args.key))

if __name__ == "__main__":
    main()



"""
import argparse
import json
import os
import tempfile


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    args = parse()

    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        print(*get(storage_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
"""
