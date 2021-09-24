
win = 5
draw = 3
loss = 1

totalWins = int(input("Enter number of wins: "))
totalDraws = int(input("Enter number of draws: "))
totalLosses = int(input("Enter number of losses: "))

totalPoints = (totalWins * win) + (totalDraws * draw) + (totalLosses * loss)
print(f"Total: {totalPoints}")
