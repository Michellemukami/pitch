from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired(), Length(min = 2, max = 45)])
    content = TextAreaField('Pitch', validators = [DataRequired()])
    category = SelectField('Pitch Category', choices=[('Inspirational','Inspirational'),('Biography','Biography'),('Business','Business'),('Ideas','Ideas')])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your bio.',validators = [Required()])
    submit = SubmitField('Submit')
