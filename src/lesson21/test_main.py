from user import login


def test_login_successfully():
    """Test that user logged in successfully"""
    assert "Hello, test" == login("test", "123123abc")


def test_login_invalid():
    assert "Invalid credentials for user admin" == login(
        "admin", "test password"
    )
