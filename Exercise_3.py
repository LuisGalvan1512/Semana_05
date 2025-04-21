from collections import deque
import random

def hot_potato(players, max_passes):
    queue = deque(players)

    while len(queue) > 1:
        passes = random.randint(1, max_passes)
        print(f"\nPassing the potato {passes} times...")

        for _ in range(passes):
            player = queue.popleft()
            queue.append(player)
            print(f"{player} passed the potato")

        eliminated = queue.popleft()
        print(f"{eliminated} is eliminated! ❌")

    winner = queue[0]
    print(f"\n🏆 The winner is {winner}!")
    return winner

#Tests

players = ["Alice", "Bob", "Charlie", "Diana", "Eli"]
hot_potato(players, 6)
