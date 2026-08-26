def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."


def message_about_credits(credits):
    return f"The number of credits for the Data Engineering course is {credits}."


if __name__ == "__main__":
    name = input("Enter your name: ")
    credits = input("Enter the number of credits: ")
    print(welcome_message(name))
    print(message_about_credits(credits))
