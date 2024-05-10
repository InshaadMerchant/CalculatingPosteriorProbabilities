import sys

# Define the hypotheses and their priors
hypotheses = {
    'h1': 0.10,
    'h2': 0.20,
    'h3': 0.40,
    'h4': 0.20,
    'h5': 0.10
}

# Define the transition probabilities for each hypothesis
transitions = {
    'h1': {'C': 1.0, 'L': 0.0},
    'h2': {'C': 0.75, 'L': 0.25},
    'h3': {'C': 0.50, 'L': 0.50},
    'h4': {'C': 0.25, 'L': 0.75},
    'h5': {'C': 0.0, 'L': 1.0}
}


# Function to calculate the likelihood of observing a sequence given a hypothesis
def likelihood(sequence, hypothesis):
    prob = 1.0
    for candy in sequence:
        prob *= transitions[hypothesis][candy]
    return prob


# Function to calculate the posterior probabilities of hypotheses given observations
def calculate_posterior(sequence):
    # Calculate the evidence (normalizing constant)
    evidence = sum(likelihood(sequence, h) * hypotheses[h] for h in hypotheses)

    # Calculate the posterior probabilities
    posteriors = {h: (likelihood(sequence, h) * hypotheses[h]) / evidence for h in hypotheses}

    return posteriors


# Function to calculate the probabilities of the next candy being cherry or lime
def calculate_next_probs(sequence):
    # Calculate the probabilities based on the last observation
    last_observation = sequence[-1] if sequence else None
    cherry_prob = sum(transitions[hypothesis]['C'] * posterior[hypothesis] for hypothesis in posterior)
    lime_prob = sum(transitions[hypothesis]['L'] * posterior[hypothesis] for hypothesis in posterior)

    return cherry_prob, lime_prob


# Main function
def main():
    # Get the observation sequence from command line argument
    if len(sys.argv) > 1:
        observations = sys.argv[1]
    else:
        observations = ""

    # Calculate posteriors
    global posterior
    posterior = calculate_posterior(observations)

    # Write results to file
    with open("result.txt", "w") as file:
        file.write(f"Observation sequence Q: {observations}\n")
        file.write(f"Length of Q: {len(observations)}\n\n")

        if observations:
            for i, obs in enumerate(observations, start=1):
                # Calculate posteriors for each observation
                posterior = calculate_posterior(observations[:i])

                file.write(f"After Observation {i} = {obs}: \n")
                for hypothesis in posterior:
                    file.write(f"P({hypothesis} | Q) = {posterior[hypothesis]:.5f}\n")

                cherry_prob, lime_prob = calculate_next_probs(observations[:i])
                file.write("\n")
                file.write(f"Probability that the next candy we pick will be C, given Q: {cherry_prob:.5f}\n")
                file.write(f"Probability that the next candy we pick will be L, given Q: {lime_prob:.5f}\n")


if __name__ == "__main__":
    main()
