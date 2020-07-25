def _greet_user(user):
    print("Hello, ", user)

def _respond_to_user(result):
    if result > 7:
        print("You are having a great day!")
    elif result > 5:
        print("Your day can get better!")
    else:
        print("I hope your day improves!")


def get_user():
    user = input("Hello, what is your name?: ")
    return user




def interface_with_user(user):
    _greet_user(user)
    question = "How was your day, on a scale from 1-10?:"
    result = input(question)
    _respond_to_user(int(result))