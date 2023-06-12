"""
-- Facade --
"""


class Facade:
    def __init__(self, obj1, obj2):
        self.__obj1 = obj1
        self.__obj2 = obj2

    def begin_check(self):
        print(self.__obj1.perform_action())
        print(self.__obj2.perform_action())


class ObjectOne:
    # def __init__(self):
    #     pass

    def perform_action(self):
        return "performing object 1 action"


class ObjectTwo:
    # def __init__(self):
    #     pass
    def perform_action(self):
        return "performing object 2 action"


def main():
    facade = Facade(ObjectOne(), ObjectTwo())

    print(facade.begin_check())


main()
