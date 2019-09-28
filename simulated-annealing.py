# Simulated annealing 
# By: Isaac Montes Jiménez
# Created: 9/28/2019
# Modified: 
import random as r
import math 



#initial solution:
#solution = pending
INITIAL_TEMPERATURE = 20
TEMPERATURE_REDUCTION_FACTOR = 0.5
ITERATIONS_EACH_TEMPERATURE = 10

#finalization criteria is evaluated by the ackley function 
def ackley_function(x,y):
    f = -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return f