from pickle import TRUE
import random

class Dice:
    def __init__(self, f):
        self.value = 0
        self.faces = int(f)

    def lanzar(self):
        self.value = random.randint(1,self.faces)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0

class Game:
    def __init__(self, dices, rounds, p, f):
        self.dices = int(dices)
        self.rounds = int(rounds)
        self.p = int(p)
        self.players = []
        self.dice = Dice(f)

    def register(self):
        print("Welcome, what's your name?: ")
        pname = input()
        player = Player(pname)
        print("\nThank you " + pname + ", Good luck!\n")
        self.players.append(player)

    def Players(self):
        for ply in range(0, self.p):
            self.register()

    def roundWin(self, scores):
        Max = max(scores)
        for ply in self.players:
            if ply.score == Max:
                ply.wins += 1

    def winner(self):
        Scores = [];
        for ply in self.players:
            Scores.append(ply.wins)
        Max = max(Scores)
        for ply in self.players:
            if ply.wins == Max:
                print("With a total of "+str(ply.wins)+" wins "+ply.name + " is the winner, congratulations!\n")

    def play(self):
        for rnd in range(0, self.rounds):
            scores = [];
            print("ROUND "+str(rnd)+"\n")
            for ply in self.players:
                ply.score = 0
                print("It's "+ply.name+"'s turn\n")
                for d in range(0, self.dices):
                    self.dice.lanzar()
                    ply.score += self.dice.value
                print("Scored: "+str(ply.score)+"\n")
                scores.append(ply.score)
            self.roundWin(scores)
    
print("Welcome to KrazyDizes\n")

p = True
while p:
    players = input("How many players will play: ")
    for i in players:
        if i not in "1234567890":
            print("Invalid input, please try again\n")
        else:
            p = False
r = True
while r:
    rounds = input("\nHow many rounds do you want to play: ")
    for i in rounds:
        if i not in "1234567890":
            print("Invalid input, please try again\n")
        else:
            r = False
d = True
while d:
    dices = input("\nHow many dices per round: ")
    for i in dices:
        if i not in "1234567890":
            print("Invalid input, please try again\n")
        else:
            d = False
f = True
while f:   
    faces = input("How many faces per dice: ")
    for i in faces:
        if i not in "1234567890":
            print("Invalid input, please try again\n")
        else:
            f = False

game = Game(dices, rounds, players, faces)
game.Players()
game.play()
game.winner()