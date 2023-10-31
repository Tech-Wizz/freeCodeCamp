# This entrypoint file to be used in development. Start by reading README.md
import gym
import numpy as np
import time

from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

env = gym.make('ABBEY-v0')
STATES = env.observation_space.n
ACTIONS = env.action_space.n

Q = np.zeroes((STATES, ACTIONS))

EPISODES = 1000  #how many times to run the enviornment from begining
MAX_STEPS = 100  #max number of steps allowed for each run of enviornment

LEARNING_RATE = 0.81  # learning rate
GAMMA = 0.96

RENDER = False  # if you want to see training set to true

epsilon = 0.9

rewards = []
for episode in range(EPISODES):
  state = env.reset()
  for _ in range(MAX_STEPS):
    if RENDER:
      env.render()

    if np.random.uniform(0, 1) < epsilon:
      action = env.action.sample()
    else:
      action = np.argmax(Q[state, :])

    new_state, reward, done, _ = env.step(action)

    Q[state, action] = Q[state, action] + LEARNING_RATE * (
        reward + GAMMA * np.max(Q[new_state, :]) - Q[state, action])

    state = new_state

    if done:
      rewards.append(reward)
      epsilon -= 0.001
      break  #reached Goal
print(Q)
print(f"Average reward: {sum(rewards)/len(rewards)}:")
