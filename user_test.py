import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Ryan","Munge","Githanji","rgmunge@gmail.com")

    def test1(self):
        self.assertEqual(self.new_user.F_name,"Ryan")
        self.assertEqual(self.new_user.L_name,"Munge")
        self.assertEqual(self.new_user.S_name,"Githanji")
        self.assertEqual(self.new_user.E_mail,"rgmunge@gmail.com")

    def test_save_user(self):
        self.new_user.save_user()

    def tearDown(self):
        User.userList = []
    def test_delete_user():
        self.new_user.save_user()
        test_data = User("Angie","Muthoni","Njoroge","angie.an@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_user(self):
        self.assertEqual(User.display_users(),User.user_list)

if __name__ = "__main__":
    unittest.main()
