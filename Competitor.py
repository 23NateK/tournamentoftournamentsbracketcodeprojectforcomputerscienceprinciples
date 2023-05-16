class Competitor(object):
    # represents a competitor
    # stores the competitor's:
    #   name
    #   classification (teacher or student)
    #   score
    def __init__(self, name, score = 0):
        # creates a competitor with the given name,
        # classification, and score
        self.name = name
        self.score = score

    def getName(self):
        # returns the competitor's name
        return self.name

    def getScore(self):
        # returns the competitor's score
        return self.score

    def addPoints(self, points):
        # add the inputted number of points to score
        self.score += points
