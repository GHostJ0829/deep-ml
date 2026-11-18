import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    max_score = np.max(scores)
    shifted = scores - max_score
    log_sum_exp = np.log(np.sum(np.exp(shifted)))
    
    return np.round(shifted - log_sum_exp, 4)