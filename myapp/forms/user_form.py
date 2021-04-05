from wtforms.validators import DataRequired, Length
from wtforms.fields import StringField
from wtforms import Form

class UserForm(Form):
    USER_MIN_LEN = 5
    USER_MAX_LEN = 7
    name = StringField(u'name', 
    validators=[
        DataRequired(message="name is required"),
        Length(min=USER_MIN_LEN, message="name is {} character min".format(USER_MIN_LEN)),
        Length(max=USER_MAX_LEN, message="name is {} character max".format(USER_MAX_LEN))
    ])
