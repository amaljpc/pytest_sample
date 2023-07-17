# content of test_sysexit.py

import pytest
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

# def test_amal():
#     assert 3 == 4

# pytest -q test_sysexit.py

# Execute the test function with “quiet” reporting mode:


