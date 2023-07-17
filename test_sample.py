# content of test_sample.py

def func(x):
    return x +1

def test_calfunc():
    return 9+1


def test_answer():
    assert func(3) == 5

def rocky():
    assert test_calfunc() == 10