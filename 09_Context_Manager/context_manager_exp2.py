# Custom context manager.

class FileManager:
    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        print('Entering Context..')
        return self._file
    
    def __exit__(self, type, value, traceback):
        print(f'{type = }\n{value = }\n{traceback = }')
        print('Exiting Context ...')
        self._file.close()
        if type == Exception:
            return True
    
def main():
    with FileManager('test.txt', 'w') as file:
        print('Writing File...')
        file.write('Hello, Dear.. Marry Christmas!!')
        raise Exception()

if __name__ == '__main__':
    main()
