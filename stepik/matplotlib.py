#простой график с выводом на экран

from matplotlib.pyplot import *
from numpy import *

x = linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

figure()
plot(x, y , "r")

xlabel("x")
ylabel("y")
title("title")
show()



