"""
-- Factory --
"""
from abc import ABC, abstractmethod


class ProfileFactory:
    @staticmethod
    def create_profile(profile_type):
        if profile_type == "admin":
            return AdminProfile()
        elif profile_type == "regular":
            return RegularProfile()


class Profile(ABC):
    @abstractmethod
    def common_method(self):
        pass


class AdminProfile(Profile):
    def common_method(self):
        pass

    def __str__(self):
        return "admin profile"


class RegularProfile(Profile):

    def common_method(self):
        pass

    def __str__(self):
        return "regular profile"


def main():
    admin = ProfileFactory.create_profile("admin")
    regular = ProfileFactory.create_profile("regular")

    print(admin.__str__())
    print(regular.__str__())


main()
