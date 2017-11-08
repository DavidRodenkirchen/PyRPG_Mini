class Weapon:
    # level,name,type,baseattack,durability,power
    def __init__(self, weaponlevel, weaponname, weapontype, weaponbaseatk, weapondur, weaponpower):
        self.level = weaponlevel
        self.type = weapontype
        self.name = weaponname
        self.baseatk = weaponbaseatk
        self.atk = self.baseatk
        self.maxdur = weapondur
        self.dur = self.maxdur
        self.power = weaponpower

    def broken(self):
        self.baseatk = self.baseatk * .3

    def isbroken(self):
        if self.dur <= 0:
            return True
        else:
            return False

    def repair(self):
        self.atk = self.baseatk
        self.dur = self.maxdur

    def printweaponinfo(self):
        print('Weapon:')
        print('\tLevel:\t\t' + str(self.level))
        print('\tName:\t\t' + str(self.name))
        print('\tType:\t\t' + str(self.type))
        print('\tBase Atk:\t' + str(self.baseatk))
        print('\tAtk:\t\t' + str(self.atk))
        print('\tMax Dur:\t' + str(self.maxdur))
        print('\tDur:\t\t' + str(self.dur))
        print('\tBroken?:\t' + str(self.isbroken()))
        print('\tPower:\t\t' + str(self.power))