import threading

class Singleton:
    _instance = None

    # new is used to create object and init is used to initalize the object
    def __new__(cls):
        if cls._instance is None:
            print("creating new object for Singleton Class")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("constructor called...")
        pass


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)