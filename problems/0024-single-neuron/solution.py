import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    probabilities = []
    for row in features:
        z = sum(x * w for x,w in zip(row,weights)) + bias
        p = 1/(1+math.exp(-z))
        probabilities.append(p)
    mse = sum((p-y)**2 for p,y in zip(probabilities,labels))/len(labels)
    return probabilities, mse