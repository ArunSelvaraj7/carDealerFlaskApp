from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,IntegerField,FloatField,RadioField, SelectField,FileField
from wtforms.validators import EqualTo, Email,Length,DataRequired,ValidationError,Optional
from datetime import datetime


class Add_vehicle_form(FlaskForm):
    vehicleNumber=StringField("Registration Number",validators=[DataRequired(),Length(3,10,message='Invalid registration number! Enter without space')])
    make=SelectField("Manufactured by",validators=[DataRequired()],choices=[('Tata Motors','Tata Motors'),
    ('Hyundai','Hyundai'),('Maruthi Suzuki','Maruthi Suzuki'),('Chevrolet','Chevrolet'),('Mahindra','Mahindra'),
    ('Honda','Honda'),('Toyota','Toyota'),('Ford','Ford'),('Renault','Renault')],coerce=str)
    model=StringField("Model",validators=[DataRequired()])
    year=IntegerField("Manufacturing year",validators=[DataRequired()])
    owners=SelectField("No. of owners",validators=[Optional()],choices=[('1','One'),('2','Two'),('3','Three'),('More than 3','More than 3')],coerce=str)
    kms=IntegerField("Kilometers run",validators=[DataRequired()])
    colour=StringField("Colour",validators=[Optional()])
    fuel=SelectField("Fuel",validators=[DataRequired()],choices=[('Petrol','Petrol'),('Diesel','Diesel'),('LPG','LPG'),('Petrol and LPG','Petrol and LPG')],coerce=str)
    finance=StringField("Hypothecation",validators=[Optional()])
    insuranceEndDate=StringField("Insurance end date",validators=[Optional()],default='Nil')
    engine=StringField("Engine number",validators=[Optional()],default='Nil')
    chasis=StringField("Chasis Number",validators=[Optional()],default='Nil')
    purchaseDate=StringField("Purchase date",validators=[DataRequired()])
    purchaseShop=StringField("Purchased from",validators=[DataRequired()])
    purchasePrice=FloatField("Purchase Price",validators=[Optional()])

    salePrice=FloatField("Sale Price",validators=[DataRequired()])    
    isSold=SelectField("Vehicle is sold?",choices=[('True','Yes'),('False','No')],validators=[DataRequired()],coerce=str)
    soldDate=StringField("Sold Date ",validators=[Optional()],default=datetime.date(datetime.now()))    
    soldPrice=FloatField("Sold Price",validators=[Optional()],default=0)
    isDealer=SelectField("Is sold to dealer?",validators=[Optional()],choices=[('True','Yes'),('False','No')],coerce=str)
    buyerName=StringField("Buyer's Name",validators=[Optional()],default='Nil')
    address=StringField("Buyer's Address",validators=[Optional()],default='Nil')
    phoneNo=StringField("Buyer's Contact number",validators=[Optional()],default='Nil')
    idNumber=StringField("Buyer's ID Proof",validators=[Optional()],default='Nil')
    
    url=FileField('Photo',render_kw={'multiple': True})
    
    
    submit=SubmitField()


class search_form(FlaskForm):
    vehicleNumber=StringField("Registration Number",validators=[DataRequired(),Length(3,10,message='Invalid registration number! Enter without space')])
    submit=SubmitField()
   
class Customer_form(FlaskForm):    
    phoneNo=StringField("Contact number",validators=[DataRequired()])
    submit=SubmitField()
