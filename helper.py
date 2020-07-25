def _greet_user(user):
    print("Hello, ", user)

def salutation(is_greeting, user="Caleb"):
    if is_greeting:
        _greet_user(user)
    else:
        print("Goodbye,", user)