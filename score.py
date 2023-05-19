import Competitor

def Score(listOfGuesses, key):
  retList = []
  for bracket in listOfGuesses: #bracket tells us which student's bracket we're on
    score = 0 #score accrued by the student's bracket
    roundScore = 1 #what each correct answer is worth (is edited per tier)
    for tierNum in len(bracket)-1:  #teirNum tells us what teir we're on but the first 'teir' is their name
      for guess in len(bracket[tierNum+1]):
        try:
          if bracket[tierNum][guess].upper() == key[tierNum+1][guess].upper():
            score += roundScore
        except:
          roundScore = roundScore #I don't want an exception
      roundScore = roundScore * 2
      compy = Competitor(bracket[0], score)
      retList.append(compy)
    return listOfGuesses
            
          