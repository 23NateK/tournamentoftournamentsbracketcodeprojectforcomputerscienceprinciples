from Competitor import Competitor

def score(listOfGuesses, key):
  # score each competitor in listOfGuesses with the key
  # returns a list of competitor objects with their scores

  retList = []
  tierScore = [1, 2, 4, 6, 8, 10] # score for current round
  for bracket in listOfGuesses: #bracket tells us which student's bracket we're on
    score = 0 #score accrued by the student's bracket
    for tierNum in range(1, len(bracket)):  #tierNum tells us what tier we're on but the first 'tier' is their name
      for guess in range(len(bracket[tierNum])):
        try:
          if key[tierNum][guess] in bracket[tierNum]:
            score += tierScore[tierNum-1]
        except:
          tierNum = tierNum #I don't want an exception
    compy = Competitor(bracket[0], score)
    retList.append(compy)
  return retList
