import sys

def sayHello():
    return "Hello world!"

def sayGoodbye():
    return "Goodbye, cruel world!"

def run_tests():
    tests = [
        sayHello() == "Hello world!",
        sayGoodbye() == "Goodbye, cruel world!"
    ]
    
    if all(tests):
        sys.exit(0)
    else:
        sys.exit(1)

run_tests()