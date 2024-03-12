import pytest

class_name = "SubstitutionCipher"
exception_name = "InvalidSubstitutionCipher"

try:
    import uppgift

    SubstitutionCipher = getattr(uppgift, class_name)
    InvalidSubstitutionCipher = getattr(uppgift, exception_name)

    if not issubclass(InvalidSubstitutionCipher, ValueError):
        pytest.fail("InvalidSubstitutionCipher does not inherit from ValueError")

    # Test av konstruktorns felhantering

    def test_constructor_no_sequence():
        with pytest.raises(TypeError):
            SubstitutionCipher()

    def test_constructor_non_tuple_in_sequence():
        with pytest.raises(TypeError):
            SubstitutionCipher([("A", "B"), ["C", "D"]])

    def test_constructor_tuple_wrong_length():
        with pytest.raises(ValueError):
            SubstitutionCipher([("A", "B", "C"), ("D", "E")])

    def test_constructor_non_string_in_tuple():
        with pytest.raises(TypeError):
            SubstitutionCipher([("A", 1), ("B", "C")])

    # Test för att kontrollera att InvalidSubstitutionCipher ärver från ValueError
    def test_invalid_substitution_cipher_inheritance():
        assert issubclass(
            InvalidSubstitutionCipher, ValueError
        ), "InvalidSubstitutionCipher should inherit from ValueError"

    # Test för felhantering vid anrop till substitution-metoden

    def test_substitute_non_string():
        cipher = SubstitutionCipher([("A", "B")])
        with pytest.raises(TypeError):
            cipher.substitute(123)

    # Exemplen från uppgiftsbeskrivningen

    def test_substitution_example_litet():
        cipher = SubstitutionCipher([("a", "m"), ("b", "n")])
        unencrypted = "abba"
        encrypted = cipher.substitute(unencrypted)
        assert encrypted == "mnnm", "Substitution failed"
        assert cipher.substitute(encrypted) == unencrypted, "Decryption failed"

    def test_substitution_example_tom():
        cipher = SubstitutionCipher([])
        unencrypted = "hello"
        encrypted = cipher.substitute(unencrypted)
        assert encrypted == "hello", "Substitution failed"
        assert cipher.substitute(encrypted) == unencrypted, "Decryption failed"

    def test_substitution_example_teckendubletter():
        with pytest.raises(InvalidSubstitutionCipher):
            SubstitutionCipher([("A", "B"), ("A", "C")])

    def test_substitution_example_stort():
        mapping = list(zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"))
        cipher = SubstitutionCipher(mapping)
        unencrypted = "JACK AND JILL WENT UP THE HILL"
        encrypted = cipher.substitute(unencrypted)
        assert encrypted == "WNPX NAQ WVYY JRAG HC GUR UVYY", "Substitution failed"
        assert cipher.substitute(encrypted) == unencrypted, "Decryption failed"

except ImportError as e:
    pytest.fail(str(e))
