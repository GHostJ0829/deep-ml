import numpy as np

def transform_matrix(A, T, S):
    try:
        A = np.array(A, dtype=float)
        T = np.array(T, dtype=float)
        S = np.array(S, dtype=float)

        if A.ndim != 2 or T.ndim != 2 or S.ndim != 2:
            return -1

        if T.shape != (A.shape[0], A.shape[0]):
            return -1

        if S.shape != (A.shape[1], A.shape[1]):
            return -1

        if np.linalg.matrix_rank(T) < T.shape[0]:
            return -1

        if np.linalg.matrix_rank(S) < S.shape[0]:
            return -1

        transformed_matrix = np.linalg.solve(T, A @ S)

        return transformed_matrix.tolist()

    except (np.linalg.LinAlgError, ValueError):
        return -1