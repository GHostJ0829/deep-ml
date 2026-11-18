import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)

    exp_scores = [math.exp(x - max_score) for x in scores]

    total = sum(exp_scores)

    return [round(x/total,4) for x in exp_scores]