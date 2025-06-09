
class InvalidAgeError(Exception):
    def __init__(self, message = "Age will be 18 or above."):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid Age: {age}. You must be 18 or above.")
    else:
        print(f"Age {age} is valid!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError :
    print("Please enter a valid integer for age.")