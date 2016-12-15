class Student :
    def _init_ (self,name,home_town,age,height,favorite_icecream_flavor) :
        self.name=name
        self.home_town=home_town
        self.age=age
        self.height=height
        self.favorite_icecream_flavor=favorite_icecream_flavor
    def print_summary (self):
        print(" student information : name -" + self.name + " home town - " + self.home_town
              + " age -" + age + " height - " + self.height + " favorite ice-cream flavor - " +
              self.favorite_icecream_flavor)
    def get_giraffe_gap (self):
        return 500-self.height


