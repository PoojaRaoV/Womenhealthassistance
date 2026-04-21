class UserProfile:
    def __init__(self):
        self.user_data = {}

    def create_profile(self, name, age, height, weight, condition):
        self.user_data = {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "condition": condition
        }
        return self.user_data

    def get_profile(self):
        return self.user_data