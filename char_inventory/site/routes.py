from typing import Collection
from flask import Blueprint, render_template, redirect, url_for, flash,json, request, jsonify
from flask_login.utils import login_required
from char_inventory.forms import submitData,UserLoginForm, commitChar
from char_inventory.models import  Character,db, User,character_schema, characters_schema
from char_inventory.helpers import token_required
from char_inventory import Config
from char_inventory.buildCharacter.browserCode import createCharacter, runCreate
from flask_login import login_user, logout_user, current_user, login_required
from char_inventory.buildCharacter.myData import classes, raceList, names, races
# from buildCharacter.randomCode import runCreate
# from buildCharacter.randomCode import createChar


'''
    Note that in the below code,
    some arguments are specified when creating the Blueprint object
    The first argument, 'site', is the Blueprint's name,
    which is used by Flask's routing mechanism.

    The Second argument, __name__, is the Blueprint's import name,
    which Flask uses to locate the Blueprint's resources.    
'''

site = Blueprint('site', __name__, template_folder ='site_templates')
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/creation', methods = ["GET", "POST"])
def creation():
    form =  submitData()
    formTwo = commitChar()
    name = None
    gender = None
    thisRace = None
    thisClass = None
    if form.validate_on_submit():
        print(form.gender.data)
        theRandom = createCharacter(form.name.data.lower(), form.gender.data.lower(), form.thisRace.data.lower(), form.thisClass.data.lower(), int(form.level.data))
        runCreate(theRandom)
        gender = form.gender.data 
        form.gender.data = ''
        level = form.level.data
        form.level.data = ''
        name = form.name.data
        form.name.data = ''
        thisRace = form.thisRace.data
        form.thisRace.data = ''
        thisClass = form.thisClass.data
        form.thisClass.data = ''
        commitCharacter=Character(theRandom.name.title(), theRandom.level, theRandom.race, theRandom.charClass, theRandom.hp, theRandom.ac, theRandom.stats['str'],
        theRandom.stats['dex'],theRandom.stats['con'],theRandom.stats['int'],theRandom.stats['wis'],
        theRandom.stats['cha'], theRandom.dc, current_user.token)
        
        
    
        # if formTwo.validate_on_submit():
        #     print('test')
            # answer = formTwo.answer.data 
            # if answer == 'Yes':
        db.session.add(commitCharacter)
        db.session.commit()        
                # formTwo.answer.data  = ''    
                   
                
        
        flash(f'Congrats! {theRandom.name.title()} The {theRandom.gender.title()}, {theRandom.race.title()}, {theRandom.charClass.title()} submitted successfully!')
        flash(f'Stat rolls: {theRandom.charStats} {theRandom.race.title()}  Racial Bonus: {races[theRandom.race]}')   
        return render_template('creation.html', 
            form= form,
            # formTwo = formTwo,
            gender = gender,
            level = level,
            name = name,
            thisClass = thisClass,
            thisRace = thisRace,
            theRandom = theRandom
            )
            
    else: 
        return  render_template('creation.html', 
            form= form,
            gender = gender,
            name = name,
            thisClass = thisClass,
            thisRace = thisRace,
            )
        

   
# @site.route('/displayCharacter',methods = ['GET'])
# @token_required
# def displayCharacter(current_user_token):
#     owner = current_user_token.token
#     characters = Character.query.filter_by(user_token = owner).all()
#     response = characters_schema.dump(characters)
#     return render_template('displayCharacter.html',
#             owner = owner,
#             characters = characters,
#             response = response)



@site.route('/availableCharacter',methods = ['GET'])
def availableCharacter():
    characters = Character.query.all()
    return render_template('availableCharacter.html',
            characters = characters )
    
    
            
            

            
