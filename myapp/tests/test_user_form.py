import unittest
from myapp.forms.user_form import UserForm

class TestUserForm(unittest.TestCase):

    def test_required_name(self):
        form = UserForm()
        assert form.validate() == False

    def test_required_error_message(self):
        form = UserForm()
        form.validate()
        assert len(form.errors["name"]) == 1
        assert form.errors["name"][0] == "name is required"

    def test_valid_form(self):
        form = UserForm(data={"name": "ahlev1"})
        assert form.validate() == True
    
    def test_min_name(self):
        form = UserForm(data={"name": "aa"})
        assert form.validate() == False
        assert len(form.errors["name"]) == 1
        assert form.errors["name"][0] == "name is {} character min".format(UserForm.USER_MIN_LEN)

    def test_max_name(self):
        form = UserForm(data={"name": "asfsdfsdfasfsdaf"})
        assert form.validate() == False
        assert len(form.errors["name"]) == 1
        assert form.errors["name"][0] == "name is {} character max".format(UserForm.USER_MAX_LEN)
