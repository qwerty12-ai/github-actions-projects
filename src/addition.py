# app.py
# This is a test commit
def add(a, b):
    return a + b

# Unit test for the add function
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0