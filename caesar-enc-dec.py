import string
import sys


class Caesar:

    def __init__(self, key: int, message: str, alph: tuple = tuple(string.ascii_lowercase)):
        self.__alph = alph
        self.key = key
        self.message = message

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if not isinstance(value, int):
            raise ValueError("key must be integer")
        elif value <= 0 or value >= 25:
            raise ValueError("key should be less then 1 or greater then 25")
        self._key = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if not isinstance(value, str):
            raise ValueError("message shoould be string type")
        for char in value.lower():
            if char == " ":
                continue
            if char.lower() not in self.__alph:
                raise ValueError("Only letters are allowed in the message")
        self._message = value

    @property
    def decode_message(self) -> str:
        res = []
        for char in self.message.lower():
            if char.lower() in self.__alph:
                if char == " ":
                    res.append(char)
                    continue
                res.append(self.__alph[self.__alph.index(f"{char}")-self.key])
            else:
                res.append(char)
        return "".join(s for s in res)

    @property
    def encode_message(self) -> str:
        res = []
        for char in self.message.lower():
            if char == " ":
                res.append(char)
                continue
            if char.lower() in self.__alph:
                ind: int = self.__alph.index(f"{char}") + self.key
                if ind <= 25:
                    res.append(self.__alph[ind])
                else:
                    res.append(self.__alph[ind - 25])
            else:
                res.append(char)
        return "".join(s for s in res)


def input_mode():
    start = True
    while start:
        get_mode = input("Enter desired mode. 'D' for decode or 'E' for encode: ")
        if get_mode.lower() == "exit":
            exit()
        get_text = input("Enter your message: ")
        try:
            get_key = int(input("Enter a key: "))
            caesar = Caesar(get_key, get_text)
        except Exception as er:
            print(f"[ERROR]: {er}!!!")
            continue
        match get_mode.upper():
            case "D":
                print(caesar.decode_message)
            case "E":
                print(caesar.encode_message)
            case _:
                print("[ERROR]: Enter right mode!!!")
                continue


def console_mode():
    get_text = " ".join(x for x in sys.argv[1:-1])
    try:
        get_key = int(sys.argv[-1])
        caesar = Caesar(get_key, get_text)
    except Exception as er:
        print(f"[ERROR]: {er}!!!")
        exit()
    print(caesar.encode_message)
    return caesar.encode_message


def main():
    if len(sys.argv) == 1:
        input_mode()
    else:
        console_mode()


if __name__ == "__main__":
    main()
