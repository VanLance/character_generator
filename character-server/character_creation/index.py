from random import randint
import random
from .data import classes, raceList, names, races, modifier


class createCharacter():
    def __init__(self, name, gender, race, _class, level = 1):
        self.gender = gender.lower()
        self.name = name.lower()
        self.race = race.lower()
        self._class = _class.lower()
        self.level = int(level)

    def select(self):
        if self._class == 'random':
            self._class = random.choice(classes)
        if self.race == 'random':
            self.race= random.choice(raceList)
        if self.name == 'random':
            if self.gender == 'male': 
                self.name = random.choice(names[self.race]['male']).title()
            else:
                self.name = random.choice(names[self.race]['female']).title()
        print(f'\nName: {self.name}\n')  

    def statRolls(self):
        stat = []
        statsArr = []
        for i in range(6):
            for die in range(4):
                stat.append(randint(1,6))
            print(f'Roll {i+1}: {stat}\n')
            sortedStat = sorted(stat)
            threeBest= sortedStat[1::]
            statsArr.append(sum(threeBest))
            stat =[]
        self.charStats= sorted(statsArr)
        print(self.charStats, '\n')

        if self.charStats[0] % 2 == 1 and self.charStats[-1] % 2 == 1:
            self.charStats[0] += 1
            self.charStats[-1] += 1
        elif self.charStats[0] % 2 == 1 and self.charStats[-2] % 2 == 1:
            self.charStats[0] += 1
            self.charStats[-2] += 1
        elif self.charStats[0] % 2 == 1 and self.charStats[-3] % 2 == 1:
            self.charStats[0] += 1
            self.charStats[-3] += 1
        elif self.charStats[0] % 2 == 1 and self.charStats[-4] % 2 == 1:
            self.charStats[0] += 1
            self.charStats[-4] += 1
        elif self.charStats[0] % 2 == 1 and self.charStats[1] % 2 == 1:
            self.charStats[0] += 1
            self.charStats[1] += 1
             
        elif self.charStats[1] % 2 == 1 and self.charStats[-1] % 2 == 1:
            self.charStats[1] += 1
            self.charStats[-1] += 1
        elif self.charStats[1] % 2 == 1 and self.charStats[-2] % 2 == 1:
            self.charStats[1] += 1
            self.charStats[-2] += 1
        elif self.charStats[1] % 2 == 1 and self.charStats[-3] % 2 == 1:
            self.charStats[1] += 1
            self.charStats[-3] += 1
        elif self.charStats[1] % 2 == 1 and self.charStats[-4] % 2 == 1:
            self.charStats[1] += 1
            self.charStats[-4] += 1
        elif self.charStats[1] % 2 == 1 and self.charStats[-4] % 2 == 1:
            self.charStats[1] += 1
            self.charStats[-4] += 1

        elif self.charStats[2] % 2 == 1 and self.charStats[-1] % 2 == 1:
            self.charStats[2] += 1
            self.charStats[-1] += 1
        elif self.charStats[2] % 2 == 1 and self.charStats[-2] % 2 == 1:
            self.charStats[2] += 1
            self.charStats[-2] += 1
        elif self.charStats[2] % 2 == 1 and self.charStats[-3] % 2 == 1:
            self.charStats[2] += 1
            self.charStats[-3] += 1
        
        elif self.charStats[-3] % 2 == 1 and self.charStats[-1] % 2 == 1:
            self.charStats[-3] += 1
            self.charStats[-1] += 1
        elif self.charStats[-3] % 2 == 1 and self.charStats[-2] % 2 == 1:
            self.charStats[-3] += 1
            self.charStats[-2] += 1
        
        if self.level >= 8:
            if self.charStats[-1] <= 16:
                self.charStats[-1] += 2
            elif self.charStats[-1] == 17:
                self.charStats[-1] += 1
                self.charStats[-2] += 1
            elif self.charStats[-2] <= 17:
                if self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-2] % 2 == 0:
                    self.charStats[-2] += 2
            else:
                self.charStats[-3] += 2
               
        if self.level >= 10 and self._class == 'rogue':
            if self.charStats[-2] <= 17:
                if self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-2] % 2 == 0:
                    self.charStats[-2] += 2
            elif self.charStats[-3] <= 17:
                if self.charStats[-3] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-3] % 2 == 0:
                    self.charStats[-3] += 2
            elif self.charStats[-4] <= 17:
                if self.charStats[-4] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-5] += 1
                elif self.charStats[-4] % 2 == 0:
                    self.charStats[-4] += 2
        
        if self.level >= 12:
            if self.charStats[-1] <= 16:
                self.charStats[-1] += 2
            elif self.charStats[-1] == 17:
                self.charStats[-1] += 1
                self.charStats[-2] += 1
            elif self.charStats[-2] <= 17:
                if self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-2] % 2 == 0:
                    self.charStats[-2] += 2
            else:
                self.charStats[-3] += 2
        
        if self.level >= 14 and self._class == 'fighter':
            if self.charStats[-2] <= 17:
                if self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-2] % 2 == 0:
                    self.charStats[-2] += 2
            elif self.charStats[-3] <= 17:
                if self.charStats[-3] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-3] % 2 == 0:
                    self.charStats[-3] += 2
            elif self.charStats[-4] <= 17:
                if self.charStats[-4] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-5] += 1
                elif self.charStats[-4] % 2 == 0:
                    self.charStats[-4] += 2
        
        if self.level >= 16:
            if self.charStats[1] % 2 == 1:
                self.charStats[1] += 1
                if self.charStats[-3] % 2 == 1:
                    self.charStats[-3] += 1
                elif self.charStats[-4] % 2 == 1:    
                    self.charStats[-4] += 1
                else:
                    self.charStats[-3] += 1
            elif self.charStats[2] % 2 == 1:
                self.charStats[2] += 1    
                if self.charStats[-1] % 2 == 1:
                    self.charStats[-1] += 1
                elif self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                elif self.charStats[-3] % 2 == 1:
                     self.charStats[-3] += 1
                else: 
                    self.charStats[-3] += 1
            else:     
                self.charStats[-3] += 2
                
        if self.level >= 19:
            if self.charStats[-2] <= 17:
                if self.charStats[-2] % 2 == 1:
                    self.charStats[-2] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-2] % 2 == 0:
                    self.charStats[-2] += 2
            elif self.charStats[-3] <= 17:
                if self.charStats[-3] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-3] += 1
                elif self.charStats[-3] % 2 == 0:
                    self.charStats[-3] += 2
            elif self.charStats[-4] <= 17:
                if self.charStats[-4] % 2 == 1:
                    self.charStats[-4] += 1
                    self.charStats[-5] += 1
                elif self.charStats[-4] % 2 == 0:
                    self.charStats[-4] += 2
        if self.level >= 4:
            print(f'Stats with Ability Score Improvement: {self.charStats} \n')
        return self.charStats
        
        
    def barbarian(self):
        self.stats= {'str': self.charStats[-1], 'con': self.charStats[-2], 'dex': self.charStats[-3], 'int': self.charStats[0], 'wis':self.charStats[1], 'cha': self.charStats[2]}
        self.hitDice= 12 
        print(f'These are your barbarian\'s stats: {self.stats}')
        # chooseSkills = ['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        # charProficiencies = {'armor': ['light armor', 'medium armor'], 'weapons': ['simple weapons', 'martial weapons'], 'saving throws': ['strength', 'constitution'], 'skills': [chooseSkills.random, chooseSkills.random]}
        # equipment = ['greataxe', 'handaxe', 'handaxe', 'explorer\'s pack']
        
    def bard(self):
        self.stats= {'str': self.charStats[0], 'dex': self.charStats[-2], 'con': self.charStats[-3], 'int': self.charStats[1], 'wis': self.charStats[2], 'cha': self.charStats[-1]}
        self.hitDice= 8
        print(f'These are your bard\'s stats: {self.stats}')
        
    def cleric(self):
        self.stats= {'str': self.charStats[-3], 'dex': self.charStats[-5], 'con': self.charStats[-2], 'int': self.charStats[0], 'wis': self.charStats[-1], 'cha': self.charStats[-4]}
        self.hitDice= 8
        print(f'These are your cleric\'s stats: {self.stats}')
        
    def druid(self):
        self.stats= {'str': self.charStats[0], 'dex': self.charStats[-4], 'con': self.charStats[-2], 'int': self.charStats[-3], 'wis': self.charStats[-1], 'cha': self.charStats[-5]}
        self.hitDice= 8
        print(f'These are your druid\'s stats: {self.stats}')
        
    def fighter(self):
        self.stats= {'str': self.charStats[-1], 'dex': self.charStats[-3], 'con': self.charStats[-2], 'int': self.charStats[0], 'wis': self.charStats[2], 'cha': self.charStats[1]}
        self.hitDice= 10
        print(f'These are your fighter\'s stats: {self.stats}')
        
    def dex_fighter(self):
        self.stats= {'str': self.charStats[-3], 'dex': self.charStats[-1], 'con': self.charStats[-2], 'int': self.charStats[2], 'wis': self.charStats[0], 'cha': self.charStats[1]}
        self.hitDice= 10
        print(f'These are your dex_fighter\'s stats: {self.stats}')
        
    def monk(self):
        self.stats= {'str': self.charStats[1], 'dex': self.charStats[-1], 'con': self.charStats[-3], 'int': self.charStats[0], 'wis': self.charStats[-2], 'cha': self.charStats[-4]}
        self.hitDice= 8
        print(f'These are your monk\'s stats: {self.stats}')
        
    def paladin(self):
        self.stats= {'str': self.charStats[-1], 'dex': self.charStats[-4], 'con': self.charStats[-3], 'int': self.charStats[0], 'wis': self.charStats[1], 'cha': self.charStats[-2]}
        self.hitDice= 10
        print(f'These are your paladin\'s stats: {self.stats}')
        
    def ranger(self):
        self.stats= {'str': self.charStats[-3], 'dex': self.charStats[-1], 'con': self.charStats[-2], 'int': self.charStats[2], 'wis': self.charStats[0], 'cha': self.charStats[1]}
        self.hitDice= 10
        print(f'These are your ranger\'s stats: {self.stats}')
        
    def rogue(self):
        self.stats= {'str': self.charStats[-4], 'dex': self.charStats[-1], 'con': self.charStats[-3], 'int': self.charStats[-2], 'wis': self.charStats[-0], 'cha': self.charStats[-5]}
        self.hitDice= 8
        print(f'These are your rogue\'s stats: {self.stats}')
        
    def sorcerer(self):
        self.stats= {'str': self.charStats[0], 'dex': self.charStats[1], 'con': self.charStats[-2], 'int': self.charStats[-3], 'wis': self.charStats[-4], 'cha': self.charStats[-1]}
        self.hitDice= 6
        print(f'These are your sorcerer\'s stats: {self.stats}')
        
    def warlock(self):
        self.stats= {'str': self.charStats[0], 'dex': self.charStats[1], 'con': self.charStats[-4], 'int': self.charStats[-3], 'wis': self.charStats[-2], 'cha': self.charStats[-1]}
        self.hitDice= 8
        print(f'These are your warlock\'s stats: {self.stats}')
        
    def wizard(self):
        self.stats= {'str': self.charStats[0], 'dex': self.charStats[-4], 'con': self.charStats[-3], 'int': self.charStats[-1], 'wis': self.charStats[-2], 'cha': self.charStats[1]}
        self.hitDice= 8
        print(f'These are your wizard\'s stats: {self.stats}')
        

    def charRace(self):
        if self.race == raceList[0]:
            self.stats['str'] += 2  
            self.stats['cha'] += 1
            return self.stats
        elif self.race == raceList[1]:
            self.stats['con'] += 2 
            return self.stats     
        elif self.race == raceList[2]:
            self.stats['dex'] += 2
            return self.stats  
        elif self.race == raceList[3]:
            self.stats['int'] += 2
            return self.stats  
        elif self.race == raceList[4]:
            self.stats['cha'] += 2
            self.stats['con'] += 1
            self.stats['dex'] += 1
            return self.stats
        elif self.race == raceList[5]:
            self.stats['dex'] += 2
            return self.stats  
        elif self.race == raceList[6]:
            self.stats['str'] += 2 
            self.stats['con'] += 1
            return self.stats
        elif self.race == raceList[7]:
            self.stats['cha'] += 2 
            self.stats['int'] += 1
            return self.stats

    def hitPoints(self):
        if self.stats['con'] >=10:
            self.hp =(self.stats['con'] - 10 )// 2 + self.hitDice
        elif self.stats['con'] <=10 and self.stats['con'] % 2 == 0:
            self.hp=  (10 - self.stats['con']) /2 * -1 + self.hitDice
        else:
            self.hp =(10 - self.stats['con']) // 2 + 1 
            self.hp *= -1 
            self.hp += self.hitDice 
        if self.level > 1:
            for i in range(self.level -1):
                self.hp += random.randint(1, self.hitDice)    
        return self.hp

    def armorClass(self):
        if self.stats['dex'] >=10:
            self.ac =(self.stats['dex'] - 10 )// 2 + 10
        elif self.stats['con'] <=10 and self.stats['dex'] % 2 == 0:
            self.ac=  (10 - self.stats['dex']) /2 * -1  + 10
        else:
            self.ac =(10 - self.stats['dex']) // 2 + 1 
            self.ac *= -1 
            self.ac += 10
            # print(f'\nStarting ac: {self.ac}')
            return self.ac        
    
    def proficiency(self):
        self.bonus = 2
        if self.level >= 5:
            self.bonus = 3
        elif self.level >= 9:
            self.bonus = 4
        elif self.level >= 13:
            self.bonus = 5
        elif self.level >=17:
            self.bonus = 6
        return self.bonus

    def spellDc(self):
        self.dc = 8 + self.bonus
        if self._class in ['bard', 'paladin', 'sorcerer', 'warlock']:
            self.dc += modifier[self.stats['cha']]
        if self._class == 'cleric' or 'druid':
            self.dc += modifier[self.stats['wis']]
        if self._class in ['fighter', 'wizard', 'rogue']:
            self.dc += modifier[self.stats['int']]
        return self.dc
    def commitDB(self):
        newCharacter = createCharacter(self.name, self.gender, self.race, self._class, self.level)


# maleRandom= createCharacter('male',  random.choice(raceList), random.choice(classes))            
# randomChar = createCharacter('female',random.choice(raceList), random.choice(classes))            
  
def runCreate(character):
    character.select()
    character.statRolls()
    print(character._class,'=========')
    print(f'Your new character\'s Race: {character.race.upper()}\nClass: {character._class.upper()}')
    if character._class == classes[0]:
        character.barbarian()
    elif character._class == classes[1]:
        character.bard()
    elif character._class == classes[2]:
        character.cleric()
    elif character._class == classes[3]:
        character.druid()
    elif character._class == classes[4]:
        character.fighter()
    elif character._class == classes[5]:
        character.dex_fighter()
    elif character._class == classes[6]:
        character.monk()
    elif character._class == classes[7]:
        character.paladin()
    elif character._class == classes[8]:
        character.ranger()
    elif character._class == classes[9]:
        character.rogue()
    elif character._class == classes[10]:
        character.sorcerer()    
    elif character._class == classes[11]:
        character.warlock()
    elif character._class == classes[12]:
        character.wizard()
    
    character.charRace()
   
    character.hitPoints()
    character.armorClass()
    character.proficiency()
    
    print(f'\nRacial bonus for your {character.race}: {races[character.race]} ')
    print(f'\nNew stats after racial bonus: {character.stats}\nHP:{character.hp}\nAC:{character.ac}\nProficiency Bonus: {character.bonus}')
    # if character._class in ['bard', 'paladin', 'sorcerer', 'warlock','cleric','druid','fighter', 'wizard', 'rogue']:
    #     character.spellDc()
    #     print(f'Spell DC: {character.dc}')
    
    character.spellDc()
    print(f'Spell DC: {character.dc}')
    character.completeCharacter = {
     'name': character.name,
     "race": character.race, 
     "class": character._class, 
     'level': character.level,
     "hp": character.hp,
     "ac": character.ac,
     "strength": character.stats['str'],
     "dexterity" : character.stats['dex'],
     "constitution" : character.stats['con'],
     "intelligence" : character.stats['int'],
     "wisdom" : character.stats['wis'],
     "charisma" : character.stats['cha'],
     'proficiencyBonus': character.bonus,
     }
    character.completeCharacter['spellDC'] = character.dc
    # if character._class in ['bard', 'paladin', 'sorcerer', 'warlock','cleric','druid','fighter', 'wizard', 'rogue']:
    #     character.completeCharacter['spellDC'] = character.dc
    print('\n', character.completeCharacter)
    return character.completeCharacter