def importResponse(responseFile):
    # import a competitor's response from a file
    response = []

    # open the file & store lines in a list
    with open(responseFile) as file:
        lines = [line.rstrip() for line in file]

    response.append(lines[0]) # append the name to the response

    for i in range(2, 13, 2): # loop through the lines with answers
        response.append([item.strip() for item in lines[i].split(',')])

    return response
