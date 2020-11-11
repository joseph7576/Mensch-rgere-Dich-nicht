from random import randint
import keyboard  # i didn't use this!
import types


class Player():
    def __init__(self, name, indexPos):
        self.name = name
        self.pos = indexPos


def SetPlayerStartPosition():
    for i in playSpace:
        for j in players:
            if i == j.pos:
                playSpace[i] = j.name


def MovePlayer(index):
    SetPlaySpaceIndex(index)
    dice = RollDice()
    players[index].pos = (players[index].pos + dice) % 28
    ## --- debug
    print(players[index].pos)
    print(playSpace[players[index].pos])
    ## -- debug
    print("\n| Player {} ---".format(players[index].name))
    print("- Dice Rolled:", dice)
    print("- You Moved to:", players[index].pos)
    SetPlayersInPosition(index)


def SetPlaySpaceIndex(index):
    for i in playSpace:
        if i == players[index].name:
            playSpace[playSpace.index(i)] = players[index].pos + 1

# what the fuck?!


def SetPlayersInPosition(index):
    for i in playSpace:
        print(i == players[index].pos)
        if i == players[index].pos:
            print(type(i))
            playSpace[i] = players[index].name


def RollDice():
    return 8  # test
    # return randint(1, 6) + randint(1, 6)


def PrintGround():
    print("-"*125)
    print("", playerPosition)
    print("", playSpace)
    print("-"*125)


# Create PlayGround
playerPosition = [i for i in range(28)]  # index: 0 - 27
playSpace = [i for i in range(1, 29)]  # 1 - 28

# Create Players
A = Player("A", 3)  # 4
B = Player("B", 10)  # 11
C = Player("C", 17)  # 18
D = Player("D", 24)  # 25

# Create lists of players
players = [A, B, C, D]

# Set Players In Their Starting Position
SetPlayerStartPosition()

# for debug
for i in playSpace:
    if isinstance(i, str):
        print(playSpace[playSpace.index(i)], playSpace.index(i))


# Print First Site Of Ground
PrintGround()

# Play Turning Mechanisem
l = 0
while l < len(players):
    playerTurn = int(
        input(" Player {} | Enter 1 to Roll the Dice: "
              .format(players[l].name)))

    MovePlayer(l)
    PrintGround()

    l += 1

    if l == 4:
        l = 0
