import argparse
import os
import tempfile
import json
import sys

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def del_temp_file():
    if os.path.isfile(storage_path):
        os.remove(storage_path)

class Database:
    def __init__(self):
        if os.path.isfile(storage_path):
            with open(storage_path) as f:
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
