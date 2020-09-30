class FileReader:
    """
    FileReader class
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return f"source: {self.file_path}"

    def __repr__(self):
        return f"source: {self.file_path}"

    def read(self):
        try:
            with open(self.file_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            return ""


if __name__ == "__main__":
    pass
