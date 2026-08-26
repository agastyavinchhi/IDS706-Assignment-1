from src.main import welcome_message, message_about_credits


# I am creating new inpus for bonus points
# I have added a new function that inputs number of credits for the entier class. I am also checking if it is 3 credits.
def test_welcome_message():
    assert (
        welcome_message("Agastya") == "Agastya, welcome to the Data Engineering course."
    )
    assert (
        message_about_credits(3)
        == "The number of credits for the Data Engineering course is 3."
    )
