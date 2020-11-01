
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



ACTUAL FUNCTIONAL OUTLINE

- Data structure for the problem type. Imports all the stuff from the places.
- Epsilon-Greedy Function
    - When called, takes an action, or the greedy action.
        - LOOKAHEAD - figures out what action to take.
        - UPDATE - updates
- Greedy function - just does the greedy action.
- Full update - updates the value function




"""