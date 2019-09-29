# Simulated annealing 
# By: Isaac Montes Jiménez
# Created: 9/28/2019
# Modified: 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import random as r
import numpy as np
import math 

INITIAL_TEMPERATURE = 20
FINAL_TEMPERATURE = 0.05 
TEMPERATURE_REDUCTION_FACTOR = 0.95
ITERATIONS_EACH_TEMPERATURE = 10

#Define the range of the values by the objective function 
#Ackley function
MAX_R_ACKLEY = 5
MIN_R_ACKLEY = -5

#Beale function
MAX_R_BEALE = 4.5
MIN_R_BEALE = 4.5

#Goldstein–Price function
MAX_R_GOLDSTEIN = 2
MIN_R_GOLDSTEIN = -2


#Maximum amount to both sides to explore the neighborhood
MAX_STEP = 0.5 

#objective function (ackley function), evaluates the energy
def fn_ackley_function(x,y):
    f = -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return f

def fn_beale_function(x,y):
    f = (1.5 - x + x*y)**2 + (2.25 - x + (x*y**2))**2 + (2.625 - x + (x*y**3))**2
    return f

def fn_goldstein_price_function(x,y):
    f = ( (1+(x+y+1)**2) * (19 - 14*x + (3*x**2) - 14*y + 6*x*y + (3*y**2)) ) * (30 + ((2*x - 3*y)**2) * (18 - 32*x + (12*x**2) + 48*y - 36*x*y + (27*y**2)) ) 
    return f

def fn_initialize_solution_akley():
    x = r.uniform(MIN_R_ACKLEY, MAX_R_ACKLEY)
    y = r.uniform(MIN_R_ACKLEY, MAX_R_ACKLEY)
    return x, y

def fn_initialize_solution_beale():
    x = r.uniform(MIN_R_BEALE, MAX_R_BEALE)
    y = r.uniform(MIN_R_BEALE, MAX_R_BEALE)
    return x, y

def fn_initialize_solution_goldstein():
    x = r.uniform(MIN_R_GOLDSTEIN, MAX_R_GOLDSTEIN)
    y = r.uniform(MIN_R_GOLDSTEIN, MAX_R_GOLDSTEIN)
    return x, y

def fn_exploration():
    step_x = r.uniform(-1*MAX_STEP, MAX_STEP)
    step_y = r.uniform(-1*MAX_STEP, MAX_STEP)
    return step_x, step_y

def fn_plot(array_x, array_y, array_energy, title):   
    fig = plot.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z') 
    ax.plot_trisurf(array_x, array_y,array_energy, cmap=plot.cm.Spectral, antialiased=False)
    plot.show()

def fn_mainSA_ackley():
    x, y = fn_initialize_solution_akley()
    energy = fn_ackley_function(x,y)
    temperature = INITIAL_TEMPERATURE
    array_x = []
    array_y = []
    array_energy = []
    while(temperature > FINAL_TEMPERATURE): #termination criteria
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
            array_x.append(x)
            array_y.append(y)
            array_energy.append(energy)
        temperature *= TEMPERATURE_REDUCTION_FACTOR
        print(temperature)
    print("Final value of objective function: ", energy)
    print("X: ", x)
    print("Y: ", y)
    fn_plot(array_x, array_y, array_energy,'Ackley function')

def fn_mainSA_beale():
    x, y = fn_initialize_solution_beale()
    energy = fn_beale_function(x,y)
    temperature = INITIAL_TEMPERATURE
    array_x = []
    array_y = []
    array_energy = []
    while(temperature > FINAL_TEMPERATURE): #termination criteria
        for i in range(ITERATIONS_EACH_TEMPERATURE):
            step_x, step_y = fn_exploration()
            new_energy = fn_beale_function(x+step_x, y+step_y)
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
            array_x.append(x)
            array_y.append(y)
            array_energy.append(energy)
        temperature *= TEMPERATURE_REDUCTION_FACTOR
        print(temperature)
    print("Final value of objective function: ", energy)
    print("X: ", x)
    print("Y: ", y)
    fn_plot(array_x, array_y, array_energy, 'Beale function')

def fn_mainSA_goldstein_price():
    x, y = fn_initialize_solution_goldstein()
    energy = fn_goldstein_price_function(x,y)
    temperature = INITIAL_TEMPERATURE
    array_x = []
    array_y = []
    array_energy = []
    while(temperature > FINAL_TEMPERATURE): #termination criteria
        for i in range(ITERATIONS_EACH_TEMPERATURE):
            step_x, step_y = fn_exploration()
            new_energy = fn_goldstein_price_function(x+step_x, y+step_y)
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
            array_x.append(x)
            array_y.append(y)
            array_energy.append(energy)
        temperature *= TEMPERATURE_REDUCTION_FACTOR
        print(temperature)
    print("Final value of objective function: ", energy)
    print("X: ", x)
    print("Y: ", y)
    fn_plot(array_x, array_y, array_energy, 'Goldstein-price function')

#fn_mainSA_ackley()
#fn_mainSA_beale()
fn_mainSA_goldstein_price()