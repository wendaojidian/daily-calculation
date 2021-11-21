import random
import numpy as np


def vote(times):
    votes_all = np.zeros(13)
    for i in range(787):
        votes = []
        while len(votes) < times:
            num = random.randint(0, 12)
            if num not in votes:
                votes.append(num)
        for v in votes:
            votes_all[v] += 1
    print(votes_all)


if __name__ == '__main__':
    for time in range(1, 13):
        print("投", time, "票:")
        vote(time)

    print("\n\n", 1180/3)
