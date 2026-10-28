def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]

    delta = ((a - d) ** 2 + 4 * b * c) ** 0.5

    lambda1 = (a + d + delta) / 2
    lambda2 = (a + d - delta) / 2

    return [lambda1, lambda2]