# Simulated annealing 
# By: Isaac Montes Jiménez
# Created: 9/28/2019
# Modified: 
import random as r
import math 

INITIAL_TEMPERATURE = 20
FINAL_TEMPERATURE = 0
TEMPERATURE_REDUCTION_FACTOR = 0.95
ITERATIONS_EACH_TEMPERATURE = 10

#Define the range of the values of the objective function 
MAX_R = 5
MIN_R = -5

#Maximum amount to both sides to explore the neighborhood
MAX_STEP = 0.5 

#objective function (ackley function), evaluates the energy
def fn_ackley_function(x,y):
    f = -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return f
#print(fn_ackley_function(-5,-5))

def fn_initialize_solution():
    x = r.uniform(MIN_R, MAX_R)
    y = r.uniform(MIN_R, MAX_R)
    return x, y

def fn_exploration():
    step_x = r.uniform(-1*MAX_STEP, MAX_STEP)
    step_y = r.uniform(-1*MAX_STEP, MAX_STEP)
    return step_x, step_y


def fn_main_SA_ackleyF():
    x, y = fn_initialize_solution()
    energy = fn_ackley_function(x,y)
    temperature = INITIAL_TEMPERATURE
    while(temperature > INITIAL_TEMPERATURE): #termination criteria
        for i in range(ITERATIONS_EACH_TEMPERATURE):
            step_x, step_y = fn_exploration()
            new_energy = fn_ackley_function(x+step_x, y+step_y)
            delta_energy = new_energy - energy
            if(delta_energy <= 0):
                x += step_x
                y += step_y
                energy = new_energy
            else:
                rand = r.random()
                if(rand < math.exp((-1*delta_energy)/temperature)):
                    x += step_x
                    y += step_y
                    energy = new_energy
        temperature *= TEMPERATURE_REDUCTION_FACTOR

