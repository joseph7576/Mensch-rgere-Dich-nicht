from random import randint
import keyboard  # i didn't use this!
import types


class Player():
    def __init__(self, name, indexPos):
        self.name = name
        self.pos = indexPos
        self.winPos = indexPos


def SetPlayerStartPosition():
    for i in playSpace:
        for j in players:
            if i == j.pos:
                playSpace[i] = j.name


def MovePlayer(index):
    SetPlaySpaceIndex(index)
    print(
        "\n| Player {} --- at {}".format(players[index].name, players[index].pos))
    dice = RollDice()
    players[index].pos = (players[index].pos + dice) % 28
    print("- Dice Rolled:", dice)
    print("- {} is now at: {}".format(players[index].name, players[index].pos))
    SetPlayersInPosition(index)


def SetPlaySpaceIndex(index):
    for i in playSpace:
        if i == players[index].name:
            playSpace[playSpace.index(i)] = players[index].pos + 1
            return
        elif playSpace.index(i) == players[index].pos and len(i) > 1:
            playSpace[playSpace.index(i)] = i[2:]
            return


def SetPlayersInPosition(index):
    for i in playSpace:
        if playSpace.index(i) == players[index].pos and isinstance(i, int):
            playSpace[playSpace.index(i)] = players[index].name
            return
        elif playSpace.index(i) == players[index].pos and isinstance(i, str):
            playSpace[playSpace.index(i)] += "|" + players[index].name
            return


def RollDice():
    return int(input("ENTER DICE: "))  # test
    # return randint(1, 6) + randint(1, 6)


def PrintGround():
    print("-"*125)
    print("", playerPosition)  # - for debug puropses
    print("", playSpace)
    print("-"*125)


def Win(l):
    # for i in playSpace:
    #     if isinstance(i, str):
    #         for j in players:
    #             if playSpace.index(i) == j.winPos:
    #                 print(" {} has WON!".format(j.name))
    #                 players.remove(j)
    #                 return
    for i in players:
        if i.pos == i.winPos:
            print("{} has WON!".format(i.name))
            players.remove(i)
            l -= 1
            return


def RemovePlayer(l):  # useless
    for i in players:
        if i.pos == i.winPos:
            print("{} has WON!".format(i.name))
            players.remove(i)
            l -= 1
            return


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

# Print First Site Of Ground
PrintGround()

# Play Turning Mechanisem
l = 0
winCondition = False
while l < len(players):
    # playerTurn = int(
    #     input(" Player {} | Enter 1 to Roll the Dice: "
    #           .format(players[l].name)))

    MovePlayer(l)
    PrintGround()

    if winCondition:
        Win(l)

    l += 1

    if l == len(players):
        l = 0
        winCondition = True

# TODO WIN CONDITION!!!
