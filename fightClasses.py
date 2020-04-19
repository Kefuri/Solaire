class Player:
    def __init__(self):
        self.monsters = [] #array that holds all of the user's monster objects
        self.monster_index = 0 #the initial monster in battle

    def get_monster(self):
        return self.monsters[self.monster_index]
        #gets the object of the monster in use
    def take_damage(self,damage):
        mon = self.get_monster()
        mon.health -= (damage - mon.defense) #how the monster will lose health
        if mon.health <= 0: #if the monster ends up being destroyed
            mon.state = False #state used as a reference for being destroyed
            mon.health = 0 #keeps health at 0 for display
            print(f"{mon.name} has been destroyed and can no longer be used!")
        else:
            print(f"{mon.name} now has {mon.health} health.")

    def switchmon(self, newnum):
        if self.monsters[newnum].state ==  False: #state used to check whether the monster
            print("This creature is destroyed and cannot be used!") #is alive or not
        else:
            self.monster_index = newnum #the new monster is switched to by changing the
            mon= self.get_monster()     #index value to the monster wanted
            print(f"New active monster: {mon.name}")

class Monster:
    def __init__(self, health, attack, defense, speed, name, type, sprite):
        self.health = health
        self.monAttack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.monType = type
        self.sprite = sprite
        self.state = True #holds whether the monster is dead or alive

        self.moves = [] #holds monster's attack objects

    def get_mon_health(self):
        return self.health #gets the creature health
    def get_mon_atk(self):
        return self.monAttack #gets the creature attack
    def get_mon_def(self):
        return self.defense #gets the creature defense
    def get_mon_speed(self):
        return self.speed #gets the creature speed
    def get_mon_type(self):
        return self.monType
    def get_mon_state(self):
        return self.state #gets the creature state

class Attack():
    def __init__(self, damage, type, name):
        self.damage = damage
        self.type = type
        self.atkname = name

    def get_attack_dmg(self):
        return self.damage
    def get_attack_type(self):
        return self.type
    def get_attack_name(self):
        return self.atkname

    def get_attack_modifier(self, atktype, enemytype):
        types = {
        'Fire': 0,
        'Water': 1,
        'Earth': 2,
        'Light': 3,
        'Dark' : 4
        } #stores each type and the equivalent integer for each type
        atkval = types[atktype] #finds the user attack value
        enmval = types[enemytype] #finds the enemy attack value
        if atkval >= 3 and enmval >= 3: #if the types are both light or dark
            if atkval != enmval: #if one chose light and the other chose dark
                return 1.2
            else: #if the same type was chosen the damage is neutral
                return 1
        result = ((atkval-enmval)+5) % 3 #a calculation that returns 1, 0 or 2
        if result == 1:
            return 1.2 #if the calculation returns 1, the damage is buffed
        elif result == 0: #if the calculation returns 0, the damage is dropped
            return 0.8
        else: #anything else will be considered neutral.
            return 1

    def overall_damage(self, basedamage, attack, enemytype): #this function calls the modifier function
        modifier = self.get_attack_modifier(self.type, enemytype) #and uses this modifier to calculate the total damage dealt
        totaldamage = (attack + basedamage) * modifier #as shown here
        return totaldamage #it is returned so that it can be used in the take_damage function

me = Player()
enemy = Player()

monster0 = Monster(150, 30, 70, 50, 'Skultulus', 'Dark', 'pipo-boss002.png')
monster1 = Monster(130, 50, 50, 80, 'DekuDeku', 'Earth', 'pipo-enemy006.png')
monster2 = Monster(100, 70, 30, 100, 'Archaeda', 'Fire', 'pipo-boss001.png')
monster3 = Monster(90, 85, 15, 110, 'Juradami', 'Light', 'pipo-boss004.png')

monster4 = Monster(150, 30, 70, 50, 'Skultulus', 'Dark', 'pipo-boss002.png')
monster5 = Monster(100, 70, 30, 100, 'Archaeda', 'Fire', 'pipo-boss001.png')
me.monsters.append(monster0)
me.monsters.append(monster1)
me.monsters.append(monster2)
me.monsters.append(monster3)
enemy.monsters.append(monster4)
enemy.monsters.append(monster5)

smack = Attack(100, 'Light', 'Smack')
beatup = Attack(150, 'Dark', 'Beat Up')
ember = Attack(90, 'Fire', 'Ember')
flare = Attack(100, 'Light', 'Flare')

monster0.moves.append(smack)
monster0.moves.append(beatup)
monster1.moves.append(ember)
monster1.moves.append(flare)
monster2.moves.append(smack)
monster2.moves.append(ember)
monster3.moves.append(flare)
monster3.moves.append(ember)

monster4.moves.append(smack)
monster4.moves.append(beatup)

monster5.moves.append(ember)
monster5.moves.append(flare)

#enemy.take_damage(atk1.overall_damage(atk1.damage, me.get_monster().monAttack, enemy.get_monster().monType))
