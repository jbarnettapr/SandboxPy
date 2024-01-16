def sayHello():
    return "Hello world!"

def run_tests():
    tests = [
        sayHello() == "Hello world!"
    ]
    
    if all(tests):
        return 0
    else:
        return 1    

run_tests()