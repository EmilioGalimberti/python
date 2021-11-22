import main


def test_add(): # test must be used for pytest and use the same name for the function.
    assert main.add(3, 4) == 7 # assert statement ensure that all these passes TRUE.
    assert main.add(3.5, 4) == 7
    assert main.add(3.9, 4) == 7
    assert main.add(3.9, 4.1) == 8


def test_to_sentence():
    assert main.to_sentence('apple') == 'Apple.' # Expected output.
    assert main.to_sentence('Apple trees') == 'Apple trees.'
    assert main.to_sentence('Apple trees.') == 'Apple trees.'
