# :star: :star: Slitherin' :snake: 

My personal take on the homonym [OpenAI Request for Research
2.0](https://openai.com/research/requests-for-research-2) problem.

---

Implement and solve a multiplayer clone of the classic Snake game (see 
[slither.io](https://slither.io) for inspiration) as a Gym environment.

- Environment: have a reasonably large field with multiple snakes; snakes grow
when eating randomly-appearing fruit; a snake dies when colliding with another
snake, itself, or the wall; and the game ends when all snakes die. Start with
two snakes, and scale from there.

- Agent: solve the environment using self-play with an RL algorithm of your
choice. You’ll need to experiment with various approaches to overcome self-play
instability (which resembles the instability people see with GANs). For example,
try training your current policy against a distribution of past policies. Which
approach works best?

- Inspect the learned behavior: does the agent learn to competently pursue food
and avoid other snakes? Does the agent learn to attack, trap, or gang up against
the competing snakes? Tweet us videos of the learned policies!

