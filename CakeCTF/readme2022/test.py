import os

if __name__ == '__main__':
    filepath = input("filepath: ")
    filepath = os.path.expanduser(filepath)
    print(filepath)
