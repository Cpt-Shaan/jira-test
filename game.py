"""
SWLAB3 - Assignment - 3 - JIRA
Problem statement 1 - Multiplication game program. 
"""

import time
import matplotlib.pyplot as plt
import numpy as np
import random

def playGame(playerName, pointsHistory):
    points = 0
    timeHistory = []
    for i in range(1,11):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        ans = num1 * num2
        print(f"Question {i} : {num1} * {num2} = ", end = "")
        start_time = time.time()
        ansPlayer = int(input())
        end_time = time.time()
        if(ans == ansPlayer):
            print("Right!")
            points += 1
        else:
            print(f"Wrong. The answer is {ans}")
        timeHistory.append(end_time - start_time)

    pointsHistory[playerName] = [points, timeHistory]


def award(pointsHistory):
    # Sort by points (descending), then by total time (ascending)
    sorted_players = sorted(
        pointsHistory.items(),
        key=lambda x: (-x[1][0], sum(x[1][1]))
    )
    prizes = ["Gold Medal ", "Silver Medal ", "Bronze Medal "]
    for i, (player, (points, times)) in enumerate(sorted_players[:3]):
        print(f"{prizes[i]}: {player} - {points} points, Time: {sum(times):.2f} seconds")
    print("\nFull Leaderboard:")
    for player, (points, times) in sorted_players:
        print(f"{player}: {points} points, Time: {sum(times):.2f} seconds")

def plotTimes(pointsHistory):
    players = list(pointsHistory.keys())
    total_times = [sum(pointsHistory[player][1]) for player in players]
    plt.figure(figsize=(10,6))
    bars = plt.bar(players, total_times, color='skyblue')
    plt.xlabel('Players')
    plt.ylabel('Total Time Taken (seconds)')
    plt.title('Time Analysis per Player')
    plt.xticks(rotation=45)
    for bar, t in zip(bars, total_times):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{t:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()

def main():
    
    print(" - x " * 10)
    print(" - - - - - Welcome to the MULTIPLICATION GAME !!!!! - - - - -")
    print(" - x " * 10)

    numPlayers = int(input("Enter the number of players that wish to play (minimum 1): "))

    pointsHistory = dict()

    for player in range(1, numPlayers + 1):
        print()
        playerName = input(f"Enter the name of the player-{player} (for leaderboard) : ")
        playGame(playerName, pointsHistory)
        print()

    print(" --- ---- --- The TOP-3 PlAYERS --- ---- --- ")
    award(pointsHistory)
    print(" - x" * 10)
    print()

    print()
    print("Press Enter for graph of time analysis - ")
    _ = input()
    plotTimes(pointsHistory)

if __name__ == '__main__':
    main()


