from reha.prototypes import contents


class MyPrincipal(contents.User):

    @property 
    def say_hi(self):
        return "Say Hi From My USer"
