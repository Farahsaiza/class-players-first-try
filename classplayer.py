class player () :
    def __init__(self, name, number, nationality, team, age, post ) :
        self.name  =  name
        self.number =  number
        self.nationality =  nationality
        self.team = team
        self.age =  age
        self.post = post

    def info(self):
        print("the player name is : {}, his number is: {}, his nationality: {}, his team : {}, his age: {}, his post: {}"
              .format( self.name , self.number , self.nationality , self.team , self.age , self.post))
        

emp1 = player("Kylian mbappe", 7, "French", "Paris Saint-Germain", 24,"attacker" )
emp2 = player("Achraf hakimi", 2, "Morrocan", "Paris Saint-Germain", 25,"Defender" )
emp3 = player("Lionel messi", 10, "Argentinian", "Inter Miami CF", 36 ,"attacker" )

emp1.info()
emp2.info()
emp3.info()