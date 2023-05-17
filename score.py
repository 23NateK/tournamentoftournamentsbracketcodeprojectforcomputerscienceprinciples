def Score(listOfGuesses, key):
  retList = listOfGuesses
  for bracket in listOfGuesses:
    score = 0
    round = 0
    roundScore = 1
    for teir in bracket:
      round += 1
      for i in len(guess):
        try:
          if teir[i+1].upper() == key[round][i+1].upper():
            score += roundScore
      roundScore = roundScore * 2
    bracket.append(score)
            
          
