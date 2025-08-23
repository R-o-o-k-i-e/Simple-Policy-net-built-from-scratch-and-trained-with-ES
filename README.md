A Simple Implementation of Actor-Critic Trained with Evolutionary Strategies
This repository contains a PyTorch implementation of an Actor-Critic model trained from scratch using Evolutionary Strategies (ES) on the CartPole-v1 environment.

Key Features:
-Custom-built Actor network with configurable hidden layers and LayerNorm
-Uniform crossover and Gaussian mutation operations for genetic evolution

Implementation Details:
The algorithm evolves a population of neural networks over generations,
selecting the best performers, applying genetic operations, and mutating weights to improve performance. 
The approach shows how ES can effectively train policy networks in environments with discrete action spaces.
