# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.
import collections.abc


class InvalidSubstitutionCipher(ValueError):
    pass


class SubstitutionCipher:

    def __init__(self, map: [(str, str)]):  # type: ignore
        # Save input to object-specific variables.
        self.map = map
        # Keep track of tuple values.
        self.cipher_chars = []

        # If map is not a sequence raise error.
        if not isinstance(self.map, collections.abc.Sequence):
            raise TypeError(f"{self.map} is not a sequence.")

        for i in self.map:
            # Check if tuple is not two values.
            if len(i) != 2:
                raise ValueError(f"{i} invalid tuple length")

            # Check if tuple value is not a string.
            for x in i:
                if x in self.cipher_chars:
                    raise InvalidSubstitutionCipher(f"{x} in map multiple times.")
                else:
                    self.cipher_chars.append(x)

                if len(x) != 1:
                    raise ValueError(f"{x} is not 1 character long.")
                if not isinstance(x, str):
                    raise TypeError(f"{x} is not a string.")

    def substitute(self, text: str) -> str:
        """Substitute chars in text with letters from self.map tuple-pairs."""
        if not isinstance(text, str):
            raise TypeError("text is not a string.")

        for v1, v2 in self.map:
            if v1 in text:
                text = text.replace(v1, v2)
            elif v2 in text:
                text = text.replace(v2, v1)

        return text


if __name__ == "__main__":
    # Här kan du skriva testkod som bara körs när du kör filen direkt och inte
    # när den importeras som modul i en annan fil.
    #
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    #
    # Exempel:
    # minklass = Klass()
    # print(klass.leet("hejsan")
    test = SubstitutionCipher([("a", "m"), ("b", "n")])
    print(f'{test.substitute("abba")}')  # mnnm
    print(f'{test.substitute("mnnm")}')  # abba

    test2 = SubstitutionCipher(
        [("h", "f"), ("a", "b"), ("l", "g"), ("d", "c"), ("n", "o"), ("t", "p")]
    )
    print(f'{test2.substitute("Halloj")}')
    print(f'{test2.substitute("Hbggnj")}')
