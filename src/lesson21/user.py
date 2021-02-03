def hello(name: str) -> str:
    return f"Hello, {name}"


def check_password(password):
    return password == "123123abc"


def invalid_credentials(username):
    return f"Invalid credentials for user {username}"


def login(username, password):
    if check_password(password):
        return hello(username)
    return invalid_credentials(username)
