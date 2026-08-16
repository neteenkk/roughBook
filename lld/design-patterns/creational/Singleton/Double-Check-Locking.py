import threading

class DoubleCheckedSingleton:
    _instance = None
    _lock = threading.Lock()


    def __init__(self):
        if DoubleCheckedSingleton._instance is not None:
            raise Exception("Use get_instance() instead")


    @staticmethod
    def get_instance():
        if DoubleCheckedSingleton._instance is None:
            with DoubleCheckedSingleton._lock:
                if DoubleCheckedSingleton._instance is None:
                    DoubleCheckedSingleton._instance = DoubleCheckedSingleton()


        return DoubleCheckedSingleton._instance


obj1 = DoubleCheckedSingleton.get_instance()
obj2 = DoubleCheckedSingleton.get_instance()

print(obj1 is obj2)

try:
    obj3 = DoubleCheckedSingleton()
except Exception as e:
    print(e)

