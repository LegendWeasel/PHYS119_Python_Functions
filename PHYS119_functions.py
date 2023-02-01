import numpy as np

#Please make sure all of your inputed data is in SI units (m,kg,s, etc)
#All inputs are assumed to be scalars(a number) unless explicitly stated otherwise

g = 9.809 #Acceleration due to gravity


#   _   _                     _        _       _         
#  | | | |_ __   ___ ___ _ __| |_ __ _(_)_ __ | |_ _   _ 
#  | | | | '_ \ / __/ _ \ '__| __/ _` | | '_ \| __| | | |
#  | |_| | | | | (_|  __/ |  | || (_| | | | | | |_| |_| |
#   \___/|_| |_|\___\___|_|   \__\__,_|_|_| |_|\__|\__, |
#                                                  |___/                                                                                                                                                               

#Calculates the t' value given:
#A: Measurement 1
#B: Measurment 2
#uA: u[A], uncertainty of A
#uB: u[B], uncertainty of B
def calc_t_prime(A, B, uA, uB):
    return np.abs(A-B)/(np.sqrt(uA**2 + uB**2))

#Calculates the uncertainty of R(results) assuming R = aX +bY +c given:
#a,b,c: Constants, values with no uncertainty
#uX,uY: u[X],u[Y] respectivly, uncertainty of X and Y
def calc_uncertainty_propagation_linear(a,b,uX,uY):
    return np.sqrt(a * uX ** 2 + b * uY ** 2)

#Calculates the uncertainty of R(results) assuming R = cX^a * Y^b given:
#a,b,c: Constants, values with no uncertainty
#uX,uY: u[X],u[Y] respectivly, uncertainty of X and Y
#R: Result of calculation
def calc_uncertainty_propagation_nonlinear(a,b,uX,uY,X,Y,R):
    return (R * np.sqrt((a * uX/X)**2 + (b * uY/Y) ** 2))


#   ____             _                 
#  / ___| _ __  _ __(_)_ __   __ _ ___ 
#  \___ \| '_ \| '__| | '_ \ / _` / __|
#   ___) | |_) | |  | | | | | (_| \__ \
#  |____/| .__/|_|  |_|_| |_|\__, |___/
#        |_|                 |___/     


#Calculates the spring constant,f, given:
#x1: The initial length of spring(meters)
#x2: The compressed length of spring
#m1: Weight of inital spring (Kilogram)
#m2: Weight if compressed spring
def calc_springConstant(x1 , x2, m1 , m2):
    return g * np.abs(m1-m2) / np.abs(x1 -x2) #Calculates and returns the k value

#Calculates the uncertainty of spring constant, u[k], given:
#k: The calculated spring constant
#um1: u[m1], uncertainty of m1
#um2: u[m2], uncertainty of m2
#ux1: u[x1], uncertainty of x1
#ux2: u[x2], uncertainty if x2
def calc_uK(k, um1, um2, ux1, ux2):

    #Calculates u[deltaM] and u[deltaX]
    u_delta_m = ((um1)**2 + (um2)**2)**0.5
    u_delta_x = ((ux1)**2 + (ux2)**2)**0.5

    u_delta_f = g * u_delta_m #Calculates u[deltaF]

    #Calculates deltaF and deltaX
    delta_f = g * np.abs(m1-m2)
    delta_x = np.abs(x1-x2)

    #Calculates and returns the sigmaF value
    return k * ((u_delta_f/delta_f)**2 + (u_delta_x/delta_x)**2)**0.5

