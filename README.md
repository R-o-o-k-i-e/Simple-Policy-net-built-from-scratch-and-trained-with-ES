A Simple Implementation of Policy net Trained with Evolutionary Strategies
This repository contains a PyTorch implementation of a Policy net trained from scratch using Evolutionary Strategies (ES) on the CartPole-v1 environment.

Key Features:
-Custom-built Actor network with configurable hidden layers and LayerNorm
-Uniform crossover and Gaussian mutation operations for genetic evolution

Implementation Details:
The algorithm evolves a population of neural networks over generations,
selecting the best performers, applying genetic operations, and mutating weights to improve performance. 
The approach shows how ES can effectively train policy networks in environments with discrete action spaces.

<img width="552" height="413" alt="500episodes yes champion_save" src="https://github.com/user-attachments/assets/73ac1ec4-bcec-4079-b137-5d89bad25f75" />
<img width="552" height="413" alt="generation_size 500 LayerNorm update no outputs" src="https://github.com/user-attachments/assets/e2b12619-c98e-4b15-894f-509ae6eb124d" />
