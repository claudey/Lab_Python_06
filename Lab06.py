class Player:
    def __init__(self, firstname, lastname, team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def __str__(self):
        description = self.first_name,self.last_name,'plays for',self.team

        
    def addScore(self, s):
        self.scores.append(s)

    def totalScore(self):
        totalScore = sum(self.scores)
        return totalScore

    def averageScore(self):
        count = 0
        theAverageScore = float(sum(self.scores))/len(self.scores)
        return theAverageScore

torres = Player('Fernando','Torres','Spain')
torres.addScore(3)
torres.addScore(2)
torres.addScore(7)
print self.first_name
#print 'The total number of goals scored by',self.first_name,'is',torres.totalScore()
print torres.averageScore()


class Team:
    def __init__(self, teamName, league, managerName, points):
        self.name = teamName
        self.league = league
        self.managerName = managerName
        self.points = points
        self.players = []

    def __str__(self):
        description = 'The team of '+self.name+' plays in the '+self.league+\
                      '. It is managed by ' +self.managerName+' and it has '+str(self.points)+' points.'
        return description

    def addPlayer(self, player):
        self.players.append(player)

    def show(self):
        for i in self.players:
            print i

Spain = Team('Spain','La Liga','Paulo Bento',54)
Portugal = Team('Portugal','Primeira Liga','Vicente del Bosque',46)
#print Portugal

Torres = Player('Fernando','Torres',Spain)
Ronaldo = Player('Cristiano','Ronaldo',Portugal)

Spain.addPlayer(Torres)
Portugal.addPlayer(Ronaldo)
Spain.show()
Portugal.show()
