from S1E9 import Stark, Character


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)

    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)

    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        Character("Hodor")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
