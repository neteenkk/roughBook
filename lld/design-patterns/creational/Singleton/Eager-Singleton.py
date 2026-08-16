class EagerSingleton:
    _instance = None

    def __init__(self):
        if EagerSingleton._instance is not None:
            raise Exception("Use get_instance() instead.")

    @staticmethod
    def get_instance():
        return EagerSingleton._instance


# Create the Singleton instance eagerly
# This happens when the module/class is loaded
EagerSingleton._instance = EagerSingleton()


obj1 = EagerSingleton.get_instance()
obj2 = EagerSingleton.get_instance()
print(obj1 is obj2)


# Direct creation should fail
try:
    obj3 = EagerSingleton()
except Exception as e:
    print(e)