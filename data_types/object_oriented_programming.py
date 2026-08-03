class UserInfo:
    def __init__(self,name , age , email, address):
        self.__name = name
        self.age = age
        self.__email = email
        self.address = address

    def get_user_name(self):
        return self.__name

    @property
    def get_user_email(self):
        return self.__email

class UpdateUserInfo(UserInfo):
    def __init__(self, name ,email ,education):
        super().__init__(name, None, email, None)
        self.education = education

update_user = UpdateUserInfo("John Doe", "q6Mz6@example.com", "Bachelor's degree")
print(update_user.education)
print(update_user.get_user_name())


# userintro = UserInfo("John Doe", 30, "q6Mz6@example.com", "123 Main St")
# print(userintro.name)
# print(userintro.age)
# print(userintro.email)
# print(userintro.address)
