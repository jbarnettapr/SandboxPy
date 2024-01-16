import sys

def sayHello():
    return "Hello world!"

def run_tests():
    tests = [
        sayHello() == "Hello world!",
        sayHello() == "Goodbye, cruel world!"
    ]
    
    if all(tests):
        sys.exit(0)
    else:
        sys.exit(1)

run_tests()