class RomanToInt:

    _lexemes = { elem: i for i, elem in enumerate("sIVXLCDMf") }
    _states  = { elem: i for i, elem in enumerate("sIVXLCDMf") }
    _transitions = [
        #s  I  V  X   L   C    D    M     f
        [0, 1, 5, 10, 50, 100, 500, 1000, 0],   # s
        [0, 1, 3, 8,  50, 100, 500, 1000, 0],   # I
        [0, 1, 5, 10, 50, 100, 500, 1000, 0],   # V
        [0, 1, 5, 10, 30, 80,  500, 1000, 0],   # X
        [0, 1, 5, 10, 50, 100, 500, 1000, 0],   # L
        [0, 1, 5, 10, 50, 100, 300, 800,  0],   # C
        [0, 1, 5, 10, 50, 100, 500, 1000, 0],   # D
        [0, 1, 5, 10, 50, 100, 500, 1000, 0],   # M
        [0, 0, 0, 0,  0,  0,   0,   0,    0]    # f
    ]

    @classmethod
    def convert(cls, s: str) -> int:
        s = f"s{s}f"
        state = 0
        result = 0

        for char in s:
            lexeme = cls._lexemes[char]
            result += cls._transitions[state][lexeme]
            state = cls._states[char]

        return result


def main():
    cases = ["III", "LVIII", "MCMXCIV"]
    for case in cases:
        print(case, RomanToInt.convert(case))


if __name__ == "__main__":
    main()