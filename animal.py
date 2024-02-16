import sys

def cat():
    print('Meow')


def  default():
    print("Hello")

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()


if_name_=='_main_':
    main()
