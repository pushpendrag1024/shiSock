import sys
from .eserver import SetupIPC

def main():

    args = sys.argv[::]

    if len(args) > 2:
        print("Too many value to unpack") 
        sys.exit()
    if len(args) == 2:
        if args[1] == "--setupIPC":
            SetupIPC()

if __name__ == "__main__":
    main()