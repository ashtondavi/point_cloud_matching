import random

from pointsym.custom_types import Cloud


def generate_random_cloud(min_x:int, max_x:int, min_y:int, max_y:int, number:int) -> Cloud:
    """Generates a random point cloud

    Args:
        min_x (int): The minimum value to use for x axis
        max_x (int): The maximum value to use for x axis
        min_y (int): The minimum value to use for y axis
        max_y (int): The maximum value to use for y axis
        number (int): The number of points to include

    Returns:
        cloud (list): A cloud of xy coordinates
    """

    cloud = []
    for x in range(number):
        cloud += [[random.uniform(min_x, max_x), random.uniform(min_y,max_y)]]
    return cloud


def cloud_random_noise(cloud:Cloud, noise:float) -> Cloud:
    """Adds random noise to the position of the xy coordinates in a cloud

    Args:
        cloud (Cloud): The input cloud
        noise (float): The amount of noise to add

    Returns:
        noisey_cloud (Cloud): The cloud with added noise
    """    

    noisy_cloud = []
    for point in cloud:
        noise_x = random.uniform(-noise, noise)
        noise_y = random.uniform(-noise, noise)
        noisy_point = [point[0] + noise_x, point[1] + noise_y]
        noisy_cloud += [noisy_point]
    return noisy_cloud


def cloud_shared_noise(cloud:Cloud, noise:float) -> Cloud:
    """Adds shared random noise to the position of the xy coordinates in a cloud

    Args:
        cloud (Cloud): The input cloud
        noise (float): The amount of noise to add

    Returns:
        noisey_cloud (Cloud): The cloud with added noise
    """    

    noisy_cloud = []
    noise_x = random.uniform(-noise, noise)
    noise_y = random.uniform(-noise, noise)
    for point in cloud:
        noisy_point = [point[0] + noise_x, point[1] + noise_y]
        noisy_cloud += [noisy_point]
    return noisy_cloud
