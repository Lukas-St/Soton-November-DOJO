import random
import math


def load_file():
    input_file = open('DOJO Input string.txt', 'r')
    Votes = []
    for i in range(0, 100):
        line = input_file.readline().rstrip()
        Votes.append([])
        for j in range(0, 99):
            Votes[i].append(line[j])
        # Votes[i] = Votes[i].rstrip()
    return (Votes)


def print_result(Votes):
    for i in range(0, 100):
        print Votes[i]


def countVotes(matrix, start, width):
    red = 0
    blue = 0
    for y in range(0, 100):
        for x in range(start, start+width-1):
            if (matrix[y][x] == '1'):
                red += 1
            elif (matrix[y][x] == '2'):
                blue += 1

    return (red, blue)


def winner(red, blue):
    if red > blue:
        return 1
    elif blue > red:
        return 2
    else:
        return None


def generateRandomWidths():
    widths = []
    for i in range(10):
        width = random.random()
        widths.append(width)

    # Random width constituancies
    newWidths = []
    for w in widths:
        n = int(math.floor(w * 100 / sum(widths)))
        newWidths.append(n)
    newWidths[4] += 100 - sum(newWidths)

    # Cumulative widths corresponding to start-index of constituancy
    indices = []
    for i in range(0, 10):
        mySum = 0
        for j in range(0, i):
            mySum += newWidths[j]
        indices.append(mySum)
    return newWidths, indices

matrix = load_file()
constit = [[0 for x in range(100)] for x in range(100)]
desired_winner = 2

the_winner = 1
# While our desired winner isn't winning
while not (the_winner == desired_winner):
    widths, indices = generateRandomWidths()
    winners = []  # The winners of each constituancy

    # For each constituancy, count the votes, find the winner
    for i, w in enumerate(widths):
        redVotes, blueVotes = countVotes(matrix, indices[i], w)
        constit_winner = winner(redVotes, blueVotes)
        winners.append(constit_winner)

    # The winner is whoever had more constituancies
    nRed = winners.count(1)
    nBlue = winners.count(2)
    if nRed > nBlue:
        the_winner = 1
    elif nBlue > nRed:
        the_winner = 2
    else:
        the_winner = 3  # A tie

# Populate the constituancy matrix
for i, w in enumerate(widths):
    for y in range(0, 100):
        for x in range(indices[i], indices[i]+w):
            constit[y][x] = i

output = open('output.txt', 'w')
for y in range(100):
    string = ""
    for x in range(100):
        string += str(constit[y][x])
    output.write(string + '\n')
