class ExampleAuth:
    def __init__(self, user):
        self.user = user

    def authenticate(self):
        return self.user.is_authenticated

    def authorize(self):
        return self.user.role == "admin"
