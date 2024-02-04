class Character():
    
    def __init__(self, name, gender, race, archetype, level = 1):
        self.gender = gender.lower()
        self.name = name.lower()
        self.race = race
        self.archetype = archetype
        self.level = int(level)


classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'dex_fighter', 'monk', 'paladin', 'ranger', 'rogue','sorcerer', 'warlock', 'wizard']

classesTwo = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'dex_fighter', 'monk', 'paladin', 'ranger', 'rogue','sorcerer', 'warlock', 'wizard','artificer','blood Hunter',  'random']
    
raceList = ['dragonborn','dwarf','elf','gnome','half-elf','halfling','half-orc','tiefling']

races = {'dragonborn': {'strength': 2, 'charisma': 1}, 'dwarf': {'constitution': 2}, 'elf':{'dexterity':2}, 'gnome': {'int': 2}, 
        'half-elf':{'charisma':2, 'any': 1,'anyTwo':1}, 'halfling': {'dexterity':2}, 'half-orc':{'strength':2, 'constitution':1,}, 'tiefling':{'charisma':2,'intelligence':1}}    

names = {'dragonborn': {'male' : ['Arjhan', 'Balasar', 'Bharash', 'Donaar', 'Ghesh', 'Heskan', 'Kriv', 'Medrash', 'Mehen', 'Nadarr', 'Pandjed', 'Patrin', 'Rhogar', 'Shamash', 'Shedinn', 'Tarhun', 'Torinn'],
                        'female': ['Akra', 'Biri', 'Daar', 'Farideh', 'Harann', 'Havilar', 'Jheri', 'Kava', 'Korinn', 'Mishann', 'Nala', 'Perra', 'Raiann', 'Sora', 'Surina', 'Thava', 'Uadjit']},
        'dwarf': {'male' : ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik',
                 'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin', 'Thorin',' Tordek', 'Traubon', 'Travok,' 'Ulfgar', 'Veit', 'Vondal'], 
                 'female': ['Adrika', 'Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 'Liftrasa', 'Mardred', 'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra']},
        'elf': {'male': ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian', 
                'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'], 
                'female' : ['Adrana','Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua', 'Bethrynna', 'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Felosial',
                'Ielenia', 'Jelenneth', 'Keyleth', 'Leshanna', 'Lia', 'Meriele', 'Mialee', 'Naivara', 'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava', 'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia']},
        'half-elf': {'male': ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian', 
                'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'], 
                'female' : ['Adrana','Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua', 'Bethrynna', 'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Felosial',
                'Ielenia', 'Jelenneth', 'Keyleth', 'Leshanna', 'Lia', 'Meriele', 'Mialee', 'Naivara', 'Quelenna', 'Quillathe', 'Sariel', 'Shanairra', 'Shava', 'Silaqui', 'Theirastra', 'Thia', 'Vadania', 'Valanthe', 'Xanaphia']},
        'gnome': {'male': [ 'Alston',' Alvyn', 'Boddynock', 'Brocc', 'Burgell', 'Dimble', 'Eldon', 'Erky', 'Fonkin', 'Frug', 'Gerbo', 'Gimble', 'Glim', 'Jebeddo', 'Kellen', 'Namfoodle', 'Orryn', 'Roondar', 'Seebo', 'Sindri', 'Warryn', 'Wrenn', 'Zook'],
                'female': ['Alvyna','Bimpnottin', 'Breena', 'Caramip', 'Carlin', 'Donella', 'Duvamil', 'Ella',' Ellyjobell', 'Ellywick', 'Lilli', 'Loopmottin', 'Lorilla', 'Mardnab', 'Nissa',' Nyx',' Oda', 'Orla', 'Roywyn', 'Shamil', 'Tana', 'Waywocket', 'Zanna']},
        'halfling': {'male': ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich', 'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo', 'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby'], 
                   'female': ['Cada']},
        'half-orc': {'male' : ['Dench', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Keth', 'Krusk', 'Mhurren', 'Ront', 'Shump', 'Thokk'], 
                   'female': ['Gella']},
        'tiefling': {'male' : ['Akmenos', 'Amnon', 'Barakas', 'Damakos', 'Ekemon', 'Iados', 'Kairon', 'Leucis', 'Melech', 'Mordai', 'Morthos', 'Pelaios', 'Skamos', 'Therai'], 
                    'female': ['Iadis']}}

modifier= {3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:4, 17:3, 18:4, 19:4, 20:5}

proficiencies = {'armor':['light', 'medium', 'heavy', 'shields'],'weapons': ['simple', 'martial', 'hand crossbows', 'light crossbows', 'longswords',
                'rapiers', 'shortswords', 'clubs', 'daggers', 'darts','javelins','maces','quarterstaffs','scimitars', 'sickles', 'slings', 'spears']}

chooseSkills = ['animal handling', 'acrobatics', 'athletics', 'intimidation', 'nature', 'perception', 'survival','sleight of hand', 'stealth',
                'arcana','history', 'investigation', 'religion', 'insight', 'medicine', 'deception', 'performance', 'persuasion']


classesTerminal = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'dex_fighter', 'monk', 'paladin', 'ranger', 'rogue','sorcerer', 'warlock', 'wizard','random']

raceListTerminal = ['dragonborn','dwarf','elf','gnome','half-elf','halfling','half-orc','tiefling', 'random']