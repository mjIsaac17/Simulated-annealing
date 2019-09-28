# Simulated annealing 
# By: Isaac Montes Jiménez
# Created: 9/28/2019
# Modified: 
import random as r
import math 

INITIAL_TEMPERATURE = 20
TEMPERATURE_REDUCTION_FACTOR = 0.95
ITERATIONS_EACH_TEMPERATURE = 10

#Define the range of the values of the objective function 
MAX_R = 5
MIN_R = -5

#Maximum amount to explore the neighborhood
MAX_STEP = 0.5

#objective function (ackley function)
def fn_ackley_function(x,y):
    f = -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return f
#print(fn_ackley_function(-5,-5))

def fn_initialize_solution():
    x = r.uniform(MIN_R, MAX_R)
    y = r.uniform(MIN_R, MAX_R)
    return x, y

def fn_exploration():
    step_x = r.uniform(0,MAX_STEP)
    step_y = r.uniform(0,MAX_STEP)
    return step_x, step_y