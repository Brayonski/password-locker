import unittest
from password import Password


class TestPassword(unittest.TestCase):
    def setUp(self):
        self.new_account = Password(
            "James", "Muriuki", "0712345678", "james@ms.com")  # create password object

    def tearDown(self):
        Password.password_list = []

    def test_init(self):
        self.assertEqual(self.new_account.first_name, "James")
        self.assertEqual(self.new_account.last_name, "Muriuki")
        self.assertEqual(self.new_account.phone_number, "0712345678")
        self.assertEqual(self.new_account.email, "james@ms.com")

    def test_save_password(self):
        self.new_account.save_password()  # saving the new password
        self.assertEqual(len(Password.password_list), 1)

    def test_save_multiple_password(self):
        self.new_account.save_password()
        test_password = Password("Test", "user", "0712345678",
                               "test@user.com")  # new password
        test_password.save_password()
        self.assertEqual(len(Password.password_list), 2)

    def test_delete_password(self):
        self.new_account.save_password()
        test_password = Password("Test", "user", "0712345678",
                               "test@user.com")  # new password
        test_password.save_password()

        self.new_account.delete_password()  # deleting a password objeect
        self.assertEqual(len(Password.password_list), 1)

    def test_find_password_by_number(self):
        self.new_account.save_password()
        test_password = Password("Test", "user", "0711223344",
                               "test@user.com")  # new password
        test_password.save_password()

        found_password = Password.find_by_number("0711223344")

        self.assertEqual(found_password.email, test_password.email)

    def test_password_exist(self):
        self.new_account.save_password()
        test_password = Password("Test", "user", "0711223344",
                               "test@user.com")  # new password
        test_password.save_password()

        password_exists = Password.password_exist("0711223344")
        self.assertTrue(password_exists)

    def test_display_all_passwords(self):
        self.assertEqual(Password.display_passwords(), Password.password_list)


if __name__ == '__main__':
    unittest.main()
