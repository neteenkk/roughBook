import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise Exception("Use get_instance() instead.")

    @staticmethod
    def get_instance():
        with ThreadSafeSingleton._lock:
            if ThreadSafeSingleton._instance is None:
                ThreadSafeSingleton._instance = ThreadSafeSingleton()


        return ThreadSafeSingleton._instance


obj1 = ThreadSafeSingleton.get_instance()
obj2 = ThreadSafeSingleton.get_instance()

print(obj1 is obj2)

try:
    obj3 = ThreadSafeSingleton()
except Exception as e:
    print(e)
