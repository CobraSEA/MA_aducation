FILENAME = 'loger.txt'

class MyLogger:
    def __enter__(self):
        self.file = open(FILENAME, 'a+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

logger = MyLogger()

with logger as file:
    file.write('write file!')
