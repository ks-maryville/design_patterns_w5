"""
-- Singleton --
Logged in user of application

-- Note -- After reading more about the singleton pattern, I have found that there are not very many common
applications for this pattern. While this example shows how a singleton would work, this may not be a scenario that a
singleton will be used."""


class User:
    def __init__(self, id, email, role):
        self.id = id
        self.email = email
        self.role = role

    def __str__(self):
        return "Role: %s \n Email: %s \n ID: %s \n" % (self.role, self.email, self.id)


# Singleton class

class LoggedIn(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = User(1, "email", "role")
        return cls.__instance


def main():
    new_login = LoggedIn()
    print(new_login.__str__())


main()
