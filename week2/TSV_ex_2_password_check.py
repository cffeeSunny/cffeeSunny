def password_check(username: str, password: str) -> str:
    score = 3
    list_password = list(password)
    bad_username = [username,"qwert","password","12345"]

    if len(list_password) < 12:
        score -=1
    for ele in bad_username:
        if ele in password:
            score -=1
            break
    if password.isalnum():
        score -=1
    if score == 0:
        return "bad"
    elif score == 1:
        return "weak"
    elif score == 2:
        return "Ok"
    elif score == 3:
        return "good"
    pass
