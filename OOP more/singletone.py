# single tone --> one single instance
# if you want a new instance , you will get the old one(already created) instances

class Singleton:
    _instance = None
    def __init__(self) -> None:
        if Singleton._instance is None:
            Singleton._instance = self
        else:
            raise Exception('This is singletone,already used')
        @staticmethod
        def get_instance():
            if Singleton.__instance is None:
                Singleton()
            return Singleton.__instance
        
        first = Singleton.get_instance()
        second = Singleton.get_instance()
        third = Singleton.get_instance()

        print(first)
        print(second)
        print(third)
            
