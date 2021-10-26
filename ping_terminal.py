from terminalplot import plot
from pythonping import ping
import numpy as np


xs_min=[1,2,3]
ys_min=[1,10,2]

while 1:
    #y=y+1
    ping_out = ping('8.8.8.8', count = 5)

    ping_arr = str(ping_out)[len(str(ping_out))-28:].split(" ")
    print(ping_arr)
    for i in range(len(ping_arr)):
        if len(ping_arr[i]) > 10:
            time_min = ping_arr[i].split("/")[0]

    print(time_min)

    xs_min.append(float(len(ys_min)))
    ys_min.append(float(time_min))

    xs1 = np.array(xs_min[-75:])
    ys1 = np.array(ys_min[-75:])

   # x_smooth = np.linspace(xs1.min(),xs1.max(),300)
   # y_smooth = spline(xs1,ys1, x_smooth)
#    plot(x_smooth, y_smooth)
    plot(xs_min[-10:], ys_min[-10:])


print(xs)
