# Тест для модуля авторизации
def test_login_valid_user():
    assert login("admin", "password123") == True

def test_login_invalid_user():
    assert login("guest", "wrongpass") == False

def login(username, password):
    # Упрощённая логика
    if username == "admin" and password == "password123":
        return True
    else:
        return False

if __name__ == "__main__":
    test_login_valid_user()
    test_login_invalid_user()
    print("✅ Все тесты пройдены!")
