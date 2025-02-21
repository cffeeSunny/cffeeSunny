class Parrot:
    def __init__(self, name):
        self.name = name

    def say(self, message):
        formatted = f"{{self.name}} says: {message}"
        return formatted.format(self=self)


def main():
    print("Welcome to the Parrot!")
    print("=" * 40)
    with open(__file__) as fh:
        lines = fh.readlines()
        for line in lines:
            if 'SECRET = \'SWAG' in line:
                line = "SECRET = 'none_of_your_business'"
            print(line, end='')
    print("=" * 40)
    parrot_name = input('What would you like to call your parrot? ')
    parrot = Parrot(parrot_name)
    while True:
        inp = input('What would you like the parrot to say? ')
        if inp:
            print(parrot.say(inp))
        else:
            break


if __name__ == '__main__':
    main()
