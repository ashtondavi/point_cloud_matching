import matplotlib.pyplot as plt

from pointsym import utils
from pointsym import metrics

min_x = 0
max_x = 10
min_y = 0
max_y = 10
number_of_points = 10
noise_shared = 0.5
noise_random = 0.5

cloud = utils.generate_random_cloud(min_x, max_x, min_y, max_y, number_of_points)
noisy_cloud1 = utils.cloud_shared_noise(cloud, noise_shared)
noisy_cloud2 = utils.cloud_random_noise(cloud, noise_random)

print(metrics.average_nearest_neighbour(cloud, noisy_cloud1))
print(metrics.average_nearest_neighbour(cloud, noisy_cloud2))

print(metrics.closest_relative_point(cloud, noisy_cloud1, 0.3))
print(metrics.closest_relative_point(cloud, noisy_cloud2, 0.3))

x1 = [x[0] for x in cloud]
y1 = [x[1] for x in cloud]
plot_1 = plt.scatter(x1, y1, s=20, c="red", alpha=1)

x2 = [x[0] for x in noisy_cloud1]
y2 = [x[1] for x in noisy_cloud1]
plot_2 = plt.scatter(x2, y2, s=20, c="blue", alpha=1)

x3 = [x[0] for x in noisy_cloud2]
y3 = [x[1] for x in noisy_cloud2]
plot_3 = plt.scatter(x3, y3, s=20, c="green", alpha=1)

plt.legend((plot_1, plot_2, plot_3), ("original", "noise_shared", "noise_random"), fontsize=8)

plt.show()
