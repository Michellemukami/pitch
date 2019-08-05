from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class UpdateProfile(FlaskForm):
    post = TextAreaField('Write your post.',validators = [Required()])
    submit = SubmitField('Submit')
class ReviewForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Movie review')

 submit = SubmitField('Submit')