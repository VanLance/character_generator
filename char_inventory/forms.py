from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField,validators
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    #email, password, submit_button
    # first_name =  StringField('First Name ', validators = [DataRequired()])
    # last_name =  StringField('Last Name ', validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class submitData(FlaskForm):
    name = StringField('Name Or Type Random: ', validators = [DataRequired()])
    gender = SelectField(choices = ['Male', 'Female'], validate_choice= True)
    level = SelectField(choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'], validate_choice= True)
    thisRace = SelectField('random', choices = ['Random','Dragonborn','Dwarf','Elf','Gnome','Half-Elf','Halfling','Half-orc','Tiefling'], validate_choice= True)
    thisClass= SelectField('random', choices = ['Random','barbarian', 'bard', 'cleric', 'druid', 'fighter', 'dex fighter', 'monk', 'paladin', 'ranger', 'rogue','sorcerer', 'warlock', 'wizard'], validate_choice= True)
    submit_button = SubmitField('Submit')
    
class commitChar(FlaskForm):
    answer =  SelectField(choices = ['Yes', 'No'], validate_choice= True)
    submit_button = SubmitField('Commit')