import math

from pointsym.custom_types import Point, Cloud


def distance(point_a:Point, point_b:Point) -> float:
    """Calculates the distance between two points

    Args:
        point_a (Point): The first xy coordinate
        point_b (Point): The second xy coordinate
    Returns:
        distance (float): The distance between the two points
    """
    
    distance = math.hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])
    return distance


def average_nearest_neighbour(cloud_a:Cloud, cloud_b:Cloud) -> float:
    """Calculates the average nearest neighbour distance between two point clouds

    Args:
        cloud_a (Cloud): The first point cloud
        cloud_b (Cloud): The second point cloud

    Returns:
        average (float): The average nearest neighbour distance
    """

    distance_NN = []
    for point_a in cloud_a:
        distances = [distance(point_a, x) for x in cloud_b]
        distance_NN += [min(distances)]
    average = sum(distance_NN)/float(len(distance_NN))
    return average


def closest_relative_point(cloud_a:Cloud, cloud_b:Cloud, limit:float) -> float:
    """Calculates the average distance between nearest neighbour that pass a relative distance limit

    Args:
        cloud_a (Cloud): The first point cloud
        cloud_b (Cloud): The second point cloud
        limit (float): Relative closest and next closest nearest neighbour distance to be a match

    Returns:
        average (float): The average distance for closest relative point
    """

    distance_NN = []
    for index_a1, point_a in enumerate(cloud_a):
        distances = [distance(point_a, x) for x in cloud_b]
        min_index = distances.index(min(distances))
        closest_point = cloud_b[min_index]
        distances_b = [distance(closest_point, x) for x in cloud_a]
        index_a2 = distances_b.index(min(distances_b))
        if index_a1 == index_a2:
            distances.sort()
            relative_NN_distance = distances[0]/float(distances[1])
            if relative_NN_distance <= limit:
                distance_NN += [distances[0]]
    if len(distance_NN) > 0:
        average = sum(distance_NN)/float(len(distance_NN))
    else:
        average = None
    return average
