import numpy as np
import matplotlib.pyplot as plt

print(np.pi)
print(np.sin(np.pi/2))

x = np.arange(1,11)
y = np.arange(10,110,10)

plt.figure(figsize = (6,3))
plt.plot(x,y, 'r--')
plt.show()

x_sin = np.arange(0,2*np.pi,0.1)
y_sin = np.sin(x_sin)
x_cos = np.arange(0,2*np.pi,0.1)
y_cos = np.cos(x_cos)

print(y_sin)
print(y_cos)

plt.figure(figsize = (6,6))
plt.subplot(2,2,1)
plt.plot(x_sin,y_sin, 'r')
plt.title('sin curve')
plt.subplot(2,2,2)
plt.plot(x_cos,y_cos, 'b')
plt.title('cos curve')
plt.show()