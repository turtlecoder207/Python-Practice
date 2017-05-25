class HousePark():
    lastname = "park"
    def __init__(self,name):
        self.fullname =  self.lastname +name
    def travel(self, where):
        print("%s travels to %s" %(self.fullname, where))
    def love(self,other):
        print("%s falls in love with %s" %(self.fullname, other.fullname))
    def __add__(self,other):
        print("%s and %s gets married" %(self.fullname, other.fullname))
    def fight(self,other):
        print("%s and %s fights" %(self.fullname, other.fullname))
    def __sub__(self,other):
        print("%s and %s gets divorced" %(self.fullname, other.fullname))
class HouseKim(HousePark):
    lastname = "kim"
    def travel(self, where, day):
        print("%s travels to %s for %d" %(self.fullname,where,day))

pey=HousePark("linny")
juliet=HouseKim("juliet")
pey.travel("busan")
juliet.travel("busan",3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey-juliet
