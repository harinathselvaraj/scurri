from app import default

def test_index():
    assert default() == "Hello, world!"