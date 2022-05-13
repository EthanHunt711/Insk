class Open_file:
    def __init__(self, path):
        self.path = path

    def open_file(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f