from hellodemo import say_hello

def test_say_hello_default():
    assert say_hello() == "Hello, world!"

def test_say_hello_custom():
    assert say_hello("Alice") == "Hello, Alice!"