class Student :
    def __init__ (self,name,home_town,age,height,favorite_icecream_flavor) :
        self.name=name
        self.home_town=home_town
        self.age=age
        self.height=height
        self.favorite_icecream_flavor=favorite_icecream_flavor
    def print_summary (self):
        print(" student information : name -" + str(self.name) + " home town - " + str(self.home_town)
              + " age -" + str(self.age) + " height - " + str(self.height) + " favorite ice-cream flavor - " +
              str(self.favorite_icecream_flavor))
    def get_giraffe_gap (self):
        return 500-float(self.height)


