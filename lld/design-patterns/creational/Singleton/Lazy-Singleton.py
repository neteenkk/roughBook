class LazySingleton:
    _instance = None

    def __init__(self):
        if LazySingleton._instance is not None:
            raise Exception("Use get_instance() instead.")

    @staticmethod
    def get_instance():
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton()

        return LazySingleton._instance


# Get the singleton instance
l1 = LazySingleton.get_instance()
# Get the same instance again
l2 = LazySingleton.get_instance()
print(l1 is l2)


# Direct creation is not allowed after instance exists
try:
    l3 = LazySingleton()
except Exception as e:
    print(e)