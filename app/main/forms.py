from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,FileField
from wtforms.validators import Required,Email
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    

class ProductForm(FlaskForm):
    productName= StringField('Product name',validators=[Required()])
    productCategory = RadioField('Label', choices=[('adultMale', 'Adult male'), ('adultFemale', 'Adult female'),('childFemale', 'Child female'),('childMale', 'Child male')])
    productSize=StringField('Product size',validators=[Required()])
    productPrice= StringField('Product price',validators=[Required()])
    productItems= StringField('Product items',validators=[Required()])
    productPicPath=FileField('add product',validators=[Required()])
    submit= SubmitField('Add product')
class ContactForm(FlaskForm):
    email = StringField('your email',validators=[Required()])
    subject= StringField('subject',validators=[Required()])
    message=  TextAreaField('message',validators =[Required()])
    submitBlog= SubmitField('contact us')
class SubscribeForm(FlaskForm):
	email = StringField('your email',validators=[Required()])
	submitComment = SubmitField('subscribe')

