class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        print("Age is valid")

# Example Usage:
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    check_age(20)
except InvalidAgeError as e:
    print(f"Error: {e}")