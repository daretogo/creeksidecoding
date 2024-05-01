### Homework Assignment: Optimizing the Fun in the Gopher Game

#### Objective:
The goal of this assignment is to explore and adjust various settings in your "Gopher Game" to make it the most enjoyable version possible. You'll be changing some variables that affect how the game plays to discover what you think makes the game the most fun!

#### Instructions:

1. **Understand the Variables**: 
   Begin by reviewing the key variables in the script that you can adjust. These include:
   - `initial_max_light_on_time`: The maximum time a light stays on at the beginning of the game.
   - `initial_max_wait_time`: The maximum time to wait before a new light turns on at the start.
   - `min_light_on_time`: The minimum time a light will stay on.
   - `min_wait_time`: The minimum waiting time before a new light turns on.
   - `hit_milestone`: How often (in terms of score) the game speeds up.
   - `decay_rate_duration`: How much shorter the light stays on after each milestone.
   - `decay_rate_interval`: How much shorter the wait time becomes after each milestone.

2. **Experiment with Settings**:
   Change one variable at a time in your script to see how it affects the gameplay. Make a hypothesis about what will happen when you change each setting before you actually make the change. Here are some ideas to get you started:

   - What happens if you decrease the `initial_max_light_on_time`? Does the game become more challenging and fun?
   - Try adjusting the `decay_rate_duration` to be smaller (like 0.3). Does making the lights turn off faster each round make the game more exciting?
   - Increase the `hit_milestone` to a higher number. Does having longer intervals before the game speeds up make it more enjoyable or less frantic?

   Example change:
   ```python
   initial_max_light_on_time = 2  # Decreased from 3 for a faster start
3. **Document Your Changes**:
   For each change you make, write down:
   - The variable you changed and the new value you set.
   - Your hypothesis on how it would change the gameplay.
   - Your observations on what actually happened. Did it make the game more fun?

4. **Find Your Best Setup**:
   After experimenting with different values, decide on a set of variables that you think makes the game the most enjoyable. 

5. **Reflect**:
   Write a short reflection on how changing different variables affects the game's challenge and enjoyment. Which settings did you find offered the best experience and why?

6. **Save Your Work**:
   Make sure to save your final version of the script in your "personal folder" within the CreeksideCoding repo. Include comments in your script to describe what changes you made and why.


This assignment will help you understand how tweaking different parameters can affect a user's experience in interactive applications, giving you a deeper insight into game design and user engagement!
