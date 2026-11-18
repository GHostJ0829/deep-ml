def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    # Your code here
    centroids = initial_centroids.copy()
    for _ in range(max_iterations):
        cluster = [[] for _ in range(k)]

        for point in points:
            distances = [sum((x - y) ** 2 for x,y in zip(point, center)) for center in centroids]
            cloest = distances.index(min(distances))
            cluster[cloest].append(point)

        new_centeroids = []

        for i, cluster in enumerate(cluster):
            if cluster:
                center = tuple(sum(coords)/len(cluster) for coords in zip(*cluster))
                new_centeroids.append(center)
            else:
                new_centeroids.append(centroids[i])
        
        if new_centeroids == centroids:
            break
        
        centroids = new_centeroids
    return [
        tuple(round(x, 4) for x in center)
        for center in centroids
    ]