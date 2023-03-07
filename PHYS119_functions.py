import numpy as np
import matplotlib.pyplot as plt

#Please make sure all of your inputed data is in SI units (m,kg,s, etc)
#All inputs are assumed to be scalars(a number) unless explicitly stated otherwise
#"Standard" font for labels

g = 9.809 #Acceleration due to gravity


#   _   _                     _        _       _         
#  | | | |_ __   ___ ___ _ __| |_ __ _(_)_ __ | |_ _   _ 
#  | | | | '_ \ / __/ _ \ '__| __/ _` | | '_ \| __| | | |
#  | |_| | | | | (_|  __/ |  | || (_| | | | | | |_| |_| |
#   \___/|_| |_|\___\___|_|   \__\__,_|_|_| |_|\__|\__, |
#                                                  |___/                                                                                                                                                               

#Lower t -> more similar results 
#Calculates the t' value given:
#A: Measurement 1
#B: Measurment 2
#uA: u[A], uncertainty of A
#uB: u[B], uncertainty of B
def calc_t_prime(A, B, uA, uB):
    t_prime = np.abs(A-B)/(np.sqrt(uA**2 + uB**2))
    print("t' = ", t_prime)
    return t_prime

#Lower t -> more similar results 
#Calculates the t' value using standard deviation given:
def calc_t_prime(A, B):
    t_prime = np.abs(A-B)/(np.sqrt(np.std(A, ddof = 1)**2 + np.std(B, ddof = 1)**2))
    print("t' = ", t_prime)
    return t_prime

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

def calc_weightedMean(x,u_x):
    w = 1 / (u_x)**2
    x_bar = np.sum(x * w) / np.sum(w)

    return x_bar

#Calculates sd of a list x given:
#x: a numpy array of scalars(numbers)
def calc_sd(x):
    mean = np.mean(x)
    print("Mean = ", mean)

    #calculates x_i - x_ave
    x = x - mean

    #Calcs the denominator to 1 degree of freedom
    NMinusOneInverse = 1 / (len(x) - 1)

    #Calcualtes the sd
    sd = (NMinusOneInverse * np.sum(x**2))**0.5
    print("SD = ", sd)
    return sd

#Calculates the standard error(u[SD]) of x given:
#x: a numpy array of scalars
def calc_standard_error(x):
    sd = ((1/(len(x)-1)) * np.sum((x-np.mean(x))**2))**0.5 # Condensed calc of sd. Refer to calc_sd
    print("SD = ", sd)

    u_sd = sd / (len(x) ** 0.5)
    print("Standard Error = ", u_sd)
    return u_sd

#Calculates the u[x_ave] given:
#x: a numpy array of scalars
def calc_u_x_ave(x):
    sd = np.std(x)
    root_N = len(x)**0.5
    
    u_x_ave = sd / root_N
    print("u[x_ave] = ", u_x_ave)

    return u_x_ave

#    ____                 _     _                ___     ____           _     _             _     
#   / ___|_ __ __ _ _ __ | |__ (_)_ __   __ _   ( _ )   |  _ \ ___  ___(_) __| |_   _  __ _| |___ 
#  | |  _| '__/ _` | '_ \| '_ \| | '_ \ / _` |  / _ \/\ | |_) / _ \/ __| |/ _` | | | |/ _` | / __|
#  | |_| | | | (_| | |_) | | | | | | | | (_| | | (_>  < |  _ <  __/\__ \ | (_| | |_| | (_| | \__ \
#   \____|_|  \__,_| .__/|_| |_|_|_| |_|\__, |  \___/\/ |_| \_\___||___/_|\__,_|\__,_|\__,_|_|___/
#                  |_|                  |___/                                                     

# Graphs a scatter and residual graph. DO NOT use as function, use as skeleton to copy
# Replace xVec,uxVec,yVec, uyVec with appropriate values or assign xVec etc with correct values
# Replace labels with appropriate label text
def residual_graph(xVec,uxVec,yVec, uyVec):

    # Scatter step 1: find the limits of the data:
    xmin = np.min(xVec) # use the np.min function to find the smallest x value
    xmax = np.max(xVec) # same for max
    #print (xmin, xmax)  # uncomment to see what the limits are

    # Scatter step 2: generate a bunch of x points between xmin and xmax
    xpoints = np.linspace(xmin, xmax, 200) # gives 200 evenly spaced points between xmin and xmax
    #print(xpoints) # uncomment to see the x values that were generated.

    # Step 3: calculate the model values:
    #################################### MODIFY THIS PART ###########################################
    slope = 1 # Estimate of the slope.
    intercept = 1.1  # Estimate of the intercept
    ypoints = xpoints * slope + intercept # this calculates the yvalues at all 200 points.
    #################################################################################################

    # Scatter step 4: plot the curve. We plot this as a red line "r-" :
    plt.plot(xpoints, ypoints, "r-", label = "F = kx")

    # Scatter step 5: plot the data:
    plt.errorbar(xVec, yVec, uyVec, fmt="bo", markersize = 3, label="Experimental data")
    plt.title("x vs. y for given situation")
    plt.xlabel("Label for x (Unit)")
    plt.ylabel("Label for y (Unit)")
    plt.legend()
    plt.show()

    # Residuals step 1: Calculate the model at each x-datapoint
    ymodel = slope * xVec # y = mx at each x_i

    # Residuals step 2: Calcualte the residual vector
    RVec = yVec - ymodel

    # Resoduals step 3: Plot the residual vector against the x-data vector
    plt.errorbar(xVec, RVec, uyVec, fmt="bo", markersize = 3)

    # Residuals step 4: Add a R = 0 x-axis (horizontal line) to the plot
    plt.hlines(y=0, xmin=xmin, xmax=xmax, color='k') # draw axis at y = 0.

    # Residuals step 5: Add axis labels and title, and show the graph
    plt.title("Residuals for y vs. x for given situation")
    plt.xlabel("Label for x residual")
    plt.ylabel("Residual = data - model (Unit)")
    plt.show()

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
    print("u[Δm] = ", u_delta_m)
    print("u[Δx] = ", u_delta_x)

    u_delta_f = g * u_delta_m #Calculates u[deltaF]
    print("u[Δf] = ", u_delta_f)

    #Calculates deltaF and deltaX
    delta_f = g * np.abs(m1-m2)
    delta_x = np.abs(x1-x2)
    print("Δf = ", delta_f)
    print("Δx = ", delta_x)

    #Calculates and returns the sigmaF value
    u_k = k * ((u_delta_f/delta_f)**2 + (u_delta_x/delta_x)**2)**0.5
    print("u[k] = ", u_k)
    return u_k

#   ____       __                _   _             
#  |  _ \ ___ / _|_ __ __ _  ___| |_(_) ___  _ __  
#  | |_) / _ \ |_| '__/ _` |/ __| __| |/ _ \| '_ \ 
#  |  _ <  __/  _| | | (_| | (__| |_| | (_) | | | |
#  |_| \_\___|_| |_|  \__,_|\___|\__|_|\___/|_| |_|

#Calculates a (diameter of hair) given:
#p: A given dark minimum, p = {1,2,3,...} pick 1 number
#lamda: Wavelength of light shone
#L: Length between hair and paper/surface
#y: Distance between center of central bright fringe and the given dark minimum in accordance to p
def calc_a_diameter(p, lambdaVal, L, y):
    z = L/y #equal to cotangent(theta)
    print("z = ", z)

    a = p * lambdaVal * (1 + z**2) ** 0.5
    print("a = ", a)
    return a

#Calculates u[a] given:
#a: Diameter of hair
#L: Length between hair and paper/surface
#y: Distance between center of central bright fringe and the given dark minimum in accordance to p
#u_L: u[L], Uncertainty of L
#u_y: u[y], Uncertainty of y
def calc_u_a(p,L, y, u_L, u_y, lambdaVal):
    z = L/y
    print("z = ", z)

    u_z = z * ((u_L/L)**2 + (u_y/y)**2) ** 0.5 #calcs u[z]
    print("u[z] = ", u_z)

    u_a = ((p * lambdaVal * u_z * z) / (1 + z**2) ** 0.5) #calcs and prints u[a]
    print("u[a] = ",u_a)

    return u_a


## Pendulum

def calc_basic_analysis(tVec, MVec):
    print("tVec = ", tVec)
    TVec = tVec/MVec
    print("TVec = ", TVec)

    tave = np.mean(tVec)
    Tave = np.mean(TVec)
    print("tave = ", tave)
    print("Tave = ", Tave)

    ut = np.std(tVec, ddof = 1)
    uT = np.std(TVec, ddof = 1)
    print("ut = ", ut)
    print("uT = ", uT)

    utave = ut/(len(tVec)**0.5)
    uTave = uT/(len(tVec)**0.5)
    print("utave = ", utave)
    print("uTave = ", uTave)

    relutave = utave/tave
    reluTave = uTave/Tave
    print("relutave = ", relutave)
    print("reluTave = ", reluTave)

    return