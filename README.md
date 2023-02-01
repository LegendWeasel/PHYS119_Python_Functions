# PHYS119_Python_Functions
A python file containing python function code to help those who are struggling with programming in PHYS119.

## Intro: ##
Hi, I am James Hoang from the PHYS 119 L2B section who is majoring in Computer Science. I have noticed many people struggling with the python and coding part of this course and would like to help lessen that burden which is why I have created this. 

Please note that I am not a TA or professor, just a student who knows a bit of python, so the information here could very well be wrong. Use this at your own risk but I will try and keep it as correct as possible. 

Now due to the nature of this file I will require to teach you the basic of "functions" which is completly seperate from the scope of the PHYS course and so if you don't want to learn any or cannot understand any computer science then this won't be much help and I wish you best of lucks. If you are fine with trying to understand some computer science then this hopefully should help with future calculations

## Functions Crash Course: ##
Similar to functions in mathclass, "def calc_t_prime(A, B, uA, uB):" is a function that calculates the t' value we discussed in class. To use this function all we need to do is give it the values and replace the A,B,etc with the propper values and it will "return" the t'. This returned value must be stored into a variable or printed directly or else it will be lost. 

In practice, say I have 2 mesurements of A = 45 $\pm$ 15 and B = 35 $\pm$ 15 (so the u[A] and u[B] are both 15) and I want to store the t' value. ```t_prime = calc_t_prime(45,35,15,15)``` will store the value of t' in ```t_prime```. You can alternatively store all the values in variables named A,B,uA, and uB and call ```t_prime = calc_t_prime(45,35,15,15)``` and it will work exactly the same.

Please note that in order to use a function, the function code (the def part) must be above the code that is trying to use it or else you will get an error.

## How To Use: ##
In this respoitory(basically this page) you should locate a PHYS119_functions.py file which is where I will put all of my said functions. It is currently pretty barren since we have not covered a lot of content but I imagine it will grow over time. You can either download the file or just click into it to preview the file and copy paste any functions you need at the moment into the *TOP* of the Jupyter notebook. Just run that block then you should be able to use the function anywhere else in the notebook. If you reset your notebook you will need to rerun that block as well so keep that in mind. If you decide to just copy a few functions, make sure you have imported numpy into that notebook ```import numpy as np``` for a lot of these functions to work.

If you do notice any issues with the code or something is unclear, please let me know through a comment on GitHub or maybe Piazza. It is just me writting all this so there is bound to be some issues and I would appreciate it if you were to let me know if that is the case.

# Good luck everyone, you can make it through this course! #
