import numpy as np
import matplotlib
from tkinter import *
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Univers:

    def __init__(self, N) -> None:
        self.grid = np.zeros((N, N))
        self.taille = N
        self.corps = [Corp(N) for k in range(3)]
    
    def update_grid(self):
        self.grid = np.zeros((self.taille, self.taille))
        for corp in self.corps:
            self.grid[corp.x, corp.y] = 1
    
    def plot_universe(self):
        for corp in self.corps:
            plt.scatter(corp.x, corp.y)
            plt.xlim([0, self.taille])
            plt.ylim([0, self.taille])
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid()
        plt.show()
    
    def update_agents(self, dt):
        agent1 = self.corps[0]
        agent2 = self.corps[1]
        agent3 = self.corps[2]

        # update corps1
        d31 = agent3 - agent1
        d21 = agent2 - agent1
        agent1[0] += dt * (d31[0] / np.linalg.norm(d31) + d21[0] / np.linalg.norm(d21))
        agent1[1] += dt * (d31[1] / np.linalg.norm(d31) + d21[1] / np.linalg.norm(d21))
        self.corps[0] = np.array([agent1[0], agent1[1]])

        # update corps2
        d32 = agent3 - agent2
        d12 = agent1 - agent2
        agent2[0] += dt * (d32[0] / np.linalg.norm(d32) + d12[0] / np.linalg.norm(d12))
        agent2[1] += dt * (d32[1] / np.linalg.norm(d32) + d12[1] / np.linalg.norm(d12))
        self.corps[1] = np.array([agent2[0], agent1[1]])
        
        # update corps3
        d13 = agent1 - agent3
        d23 = agent2 - agent1
        agent1[0] += dt * (d31[0] / np.linalg.norm(d31) + d21[0] / np.linalg.norm(d21))
        agent1[1] += dt * (d31[1] / np.linalg.norm(d31) + d21[1] / np.linalg.norm(d21))
        self.corps[0] = np.array([agent1[0], agent1[1]])



class Corp:

    def __init__(self, N) -> None:
        self.x = np.random.randint(N)
        self.y = np.random.randint(N)


if __name__ == '__main__':
    # creation d'un univers
    N = 16
    univers = Univers(N)
    univers.update_grid()
    univers.plot_universe()