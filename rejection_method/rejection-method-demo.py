#!/usr/bin/python

'''
This is a dynamic plot update demo.
- Note: this really does not work very well in colab
'''

import matplotlib.pyplot as plt
import numpy as np
import random

##########################
# config: number of points 
##########################
n = 300
prob = 0.7

##########################
# set interactive plot mode 
##########################
plt.ion()

##########################
# set up figure and x-y axis limits
##########################
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.set_xlim(0,1)
ax.set_ylim(0,1)

##########################
# generate initial plot : empty plot
##########################

x1 = []
y1 = []
x2 = []
y2 = []

p1,p2 = ax.plot(x1,y1,'og',x2,y2,'xr')

##########################
# sample data and generate animation
##########################

accept = 0
reject = 0

for i in range(0,n):

  sample = random.random() 

  if (sample<prob):
    # ACCEPT!
    x1.append(sample)		# this is the actual sample
    y1.append(random.random()) 	# this is just for show
    p1.set_xdata(x1)
    p1.set_ydata(y1)
    accept = accept + 1
  else: 
    # REJECT!
    x2.append(sample)		# this is the actual sample
    y2.append(random.random()) 	# this is just for show
    p2.set_xdata(x2)
    p2.set_ydata(y2)
    reject = reject + 1

  ax.set_title("Accept = "+str(accept)+", Reject = "+str(reject)+" Probability = "+str(round(accept/(accept+reject),2)))

  fig.canvas.draw()
  fig.canvas.flush_events()

plt.waitforbuttonpress()
