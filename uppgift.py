# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.
import collections


class InvalidSubstitutionCipher(Exception):
    pass


class SubstitutionCipher:
    def __init__(self, map: [(str, str)]):
        self.map = map

        for i in self.map:
            # Check if tuple is not two values.
            if len(i) != 2:
                raise ValueError(f"{i} invalid tuple length")

            # Check if tuple value is not a string.
            if not isinstance(i[0], str) or not isinstance(i[1], str):
                raise ValueError("Not a string.")

        """if not isinstance(map, collections.abc.Sequence):
            raise TypeError("Null-string not allwed.")
        elif some shit appears multiple times.
            raise InvalidSubstitutionCipher("Invalid cipher.")"""

    def substitute(self, text: str) -> str:
        # Works one way...but how do I do it the other way around?
        for enc_k, dec_k in self.map:
            text = text.replace(enc_k, dec_k)

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
    test = SubstitutionCipher([("a", "m"), ("b", "n"), (1, "g")])
    print(test.substitute("abba"))  # mnnm
    print(test.substitute("mnnm"))  # abba
