import numpy as np
from scipy.stats import mode
from threading import Thread

def NormalRunning():
    lastRound = 6
    round = 1
    dice = 3
    sides = 6
    score = 0
    while round <= lastRound:
        preScore = score

        print(f"Round: {round}")
        cont = True
        while cont:
            tempScore = score
            counter = 0
            rolls = np.random.randint(sides, size=dice)+1
            print(f"You rolled: {rolls[0]} {rolls[1]} {rolls[2]}", end=" ")

            if round == rolls[0] == rolls[1] == rolls[2]:
                score=score+21
                print(" +21")
                print("Bunco!")
            elif rolls[0] == rolls[1] == rolls[2]:
                score=score+5
                print(" +5")
                print("Mini Bunco!")
            else:
                for val in rolls:
                    if val == round:
                        counter = counter+1
                        score=score+1
                print(f" +{counter}")
            if score == tempScore:
                cont=False



        print(f"You scored {score-preScore} points this round!")
        round= round+1

    print(f"\nFinal Score: {score}")





def CalculateAverageScore():
    lastRound = 6
    round = 1
    dice = 3
    sides = 6
    score = 0
    numRounds = 999999
    listScore = []


    for i in range(0,numRounds):
        score = 0
        round = 1

        while round <= lastRound:
            preScore = score

            print(f"Round: {round}")
            cont = True
            while cont:
                tempScore = score
                counter = 0
                rolls = np.random.randint(sides, size=dice)+1
                print(f"You rolled: {rolls[0]} {rolls[1]} {rolls[2]}", end=" ")

                if round == rolls[0] == rolls[1] == rolls[2]:
                    score=score+21
                    print(" +21")
                    print("Bunco!")
                elif rolls[0] == rolls[1] == rolls[2]:
                    score=score+5
                    print(" +5")
                    print("Mini Bunco!")
                else:
                    for val in rolls:
                        if val == round:
                            counter = counter+1
                            score=score+1
                    print(f" +{counter}")
                if score == tempScore:
                    cont=False



            print(f"You scored {score-preScore} points this round!")
            round= round+1

        print(f"\nFinal Score: {score}")
        listScore.append(score)
        print(f"                                                                                                           {i+1}/{numRounds}")

    print(f"{listScore}")
    print(f"Average Score over {numRounds} is {sum(listScore)/len(listScore)}")
    modee, count = mode(listScore, keepdims=False)
    print(f"Mode: {modee} Count: {count}")





if input("Normal Running? y/n: ") == "n":
    CalculateAverageScore()
else:
    NormalRunning()