def exportFile(competitorList, outputFile):
    # export a list of competitors with the competitor's placement, name, and score
    # this will be sorted from highest to lowest score with an index (the placement) placed at the start of the line
    # this data will be exported to a file

    # competitorList is a list of competitor objects
    # outputFile is the name of a file to output to

    competitorList.sort(key=lambda x: x.score) # sort competitors by score
    competitorList.reverse() # reverse the list so the highest scoring competitors are at the start

    file = open(outputFile, 'w') # open the file to write to; if it exists, it will overwrite it

    i = 0 # index
    while i < len(competitorList):
        file.write('{0}, {1}, {2}, {3}'
                   .format(i,
                           competitorList[i].getName(),
                           competitorList[i].getScore(),
                           ))
        i += 1


    file.close()
