import Competitor

def Score(listOfGuesses, key):
  retList = []
  for bracket in listOfGuesses: #bracket tells us which student's bracket we're on
    score = 0 #score accrued by the student's bracket
    roundScore = 1 #what each correct answer is worth (is edited per tier)
    for tierNum in len(bracket)-1:  #teirNum tells us what teir we're on but the first 'teir' is their name
      for guess in len(bracket[teirNum+1]):
        try:
          if bracket[tierNum][guess].upper() == key[tierNum+1][i].upper():
            score += roundScore
      roundScore = roundScore * 2
      compy = Competitor(bracket[0], score)
      reList.append(compy)
    return listOfGuesses
            
          
