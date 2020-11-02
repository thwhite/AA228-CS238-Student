
"""
BRAINSTORM OUTLINE
We need to get the policy - structure of states.

There are different possible methods. Let's start by implementing a model-based method, because it seems a lot simpler.

Steps:
- Based on the problem, generate an estimate
    - You calculate the maximum probability transition function by how often you get to s' from s, a.
        - Divided by all the s, as.
        - Then calculate reward.
        - Basically we're just counting outcomes.
        - How do we get those outcomes?!?
    - Then, in exploration and exploitation, we discuss how to explore and then recieve reward
        - So, at a high level, we just need to return an optimal policy. That means we could iterate over policies a
        shit ton as long as it worked.
        - But still we need to be able to make decisions as wel go, right?


    - In the long run, we can implement that backwards thing.

- Based on the estiamte, calculate an optimal policy action.
    - We'll figure this out later.



REV1 FUNCTIONAL OUTLINE

- Data structure for the problem type. Imports all the stuff from the places.
- Epsilon-Greedy Function
    - When called, takes an action, or the greedy action.
        - LOOKAHEAD - figures out what action to take.
        - UPDATE - updates
- Greedy function - just does the greedy action.
- Full update - updates the value function


REV2 FUNCTIONAL OUTLINE

- Model. Data structure for the MDP - holds info on currently understood problem formulation.
- Test: imports data, declares classes, and does stuff
    - Calls: epsilon-greedy to take an exploration step
        - Calls: lookahead to find the greedy step
    - Calls: update_model the model to incorporate the new facts.
    - Calls: update_value_function the value function

REV3 FUNCTIONAL OUTLINE
- um shit so i was wrong about how this works
- we still need to output a deterministic policy, but now it's a normal-ass search problem

TODO:

Milestones:

- Deal with how to prevent it from going over the edges



- Figure out the exact state function
- Figure out what an MDP class is and if I need it as distinct from the partial one


Then:
- Try to run all three types of code with this and see what happens.
- Submit a readme with those answers *before I go to sleep tonight*.
- See what score I get with that! If it's good enough, yay! If not, I have five hours tomorrow to figure it out.
"""