import numpy
import pycpd
import matplotlib.pyplot as plt

first_pos = numpy.array([[10, 15.2],[10, 10],[15, 15]])
second_pos = numpy.array([[15, 15],[15, 10],[10, 10]])
  
x1 = [x[0] for x in first_pos]
y1 = [x[1] for x in first_pos]

x2 = [x[0] for x in second_pos]
y2 = [x[1] for x in second_pos]

plt.scatter(x1, y1, color="blue", s=30)
plt.scatter(x2, y2, color="red", s=15)

test = pycpd.AffineRegistration(X=first_pos, Y=second_pos, max_iterations=50).register()
#test = pycpd.RigidRegistration(X=first_pos, Y=second_pos, max_iterations=50).register()

print(test)

third_pos = test[0]
x3 = [x[0] for x in third_pos]
y3 = [x[1] for x in third_pos]
plt.scatter(x3, y3, color="green", s=5)

plt.show()