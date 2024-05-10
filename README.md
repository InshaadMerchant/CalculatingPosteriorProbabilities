# CalculatingPosteriorProbabilities

This project was developed as part of my CSE 4308 Artificial Intelligence class


Programming Language used: Python 3.9.13
Omega Compatibility: No
For compilation and testing: Use PyCharm

How the code is structured:

- hypotheses: Contains a dictionary defining hypotheses and their prior probabilities.
- transitions: Contains a dictionary defining transition probabilities for each hypothesis.
- likelihood(sequence, hypothesis): Calculates the likelihood of observing a sequence given a hypothesis. It iterates over each candy in    the sequence and multiplies the transition probabilities.
- calculate_posterior(sequence): Calculates the posterior probabilities of hypotheses given observations. It utilizes the likelihood function and normalizes the probabilities.
- calculate_next_probs(sequence): Calculates the probabilities of the next candy being cherry or lime given a sequence of observations. It sums the transition probabilities based on the last observation.
- main(): The main function retrieves the observation sequence from the command line argument, calculates posteriors, and writes results to a file. It iterates over each observation, updating the posterior probabilities and calculating probabilities for the next candy.

How to run the code:

On the terminal, type "python compute_a_posteriori.py LCCCCCCCCCCCLLLLLLLLLLLLLLLLLLLLLLL" and press enter
It will generate the posterior probabilities for all 35 observations.

Another way to run the code is simply press the build button on PyCharm and the program will execute. type "compute_a_posteriori.py LCCCCCCCCCCCLLLLLLLLLLLLLLLLLLLLLLL" as the command line arguments. This can be found by clicking on "Run" and then on "Edit Configurations" on PyCharm.
