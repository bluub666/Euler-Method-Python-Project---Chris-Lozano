#Introduction:
#It is common when we study physics and engineering that we encounter differential equations. While some may have what we call an exact, or "analytic", solution, the majority of them don't.
#From this problem then, we resorted to developing methods of approximating these differential equations. One common method is Euler's method. This method consists of taking tiny steps in our
#function and essentially building it from that information. It is akin to measuring the circumference of a circle by taking tiny, linear measurements with a ruler. The tinier the measurement,
#the more accurate our result will be. However, it also means that we will have to do more measurements as they get smaller and smaller. Here, we can use the power of computers to perform
#thousands of calculations for us. Without further ado, let us begin.

import numpy as np #While we could work with the math module, numpy has a built in array object that can only store homogenous sets of data, so it is more optimal to work with.

#The differential equation that describes the motion of a pendulum, ignoring friction and air resistance is:
# θ" + g/L sin(θ) = 0
#Where θ" represents the angular acceleration of the pendulum, g is the gravitational acceleration on earth 9.8m/s^2, L is the length of our pendulum, and θ is a function of time θ(t)
#which describes the motion of the pendulum at any time.

#We can break this differential equation into 2 separate differential equations that depend onto one another:
  #Let ω = θ' so that we can write the following two equations:
    #θ_n+1 = θ_n + ω_n * dt
    #ω_n+1 = ω_n + θ"_n * dt    Where dt is a small step in time.
#Using the equation for the pendulum we can see that θ"_n = -g/L sin(θ_n), which gives us the form:
    #θ_n+1 = θ_n + ω_n * dt
    #ω_n+1 = ω_n - (g/L * sin(θ_n)) * dt
    #This means that both of these equations will depend on the previous like a recursion. 
#Now that we have our two equations, let us define a function, which we will call euler_method:

def euler_method(theta_initial, omega_intial, dt, num_steps): #This function needs these 4 inputs. Every time we work with a differential equation, we need information of how the system started.
  g = 9.81 # (m/s^2)
  L = 1 # m
  
  #Create an array with the starting conditions:
  theta_values = [theta_initial]
  omega_values = [omega_initial]
  #As we begin walking more steps, we will append our values to these two arrays until we have walked the amount of steps that we defined at the beginning.

  #Let's now use the Euler Method formulas stated above:
  #We first begin with a for loop that will iterate in the range of num_steps, effectively stopping when we finish our step count:
  for i in range(num_steps):
    theta_now = theta_values[-1]
    omega_now = omega_values[-1] #These are the values of theta that will be getting updated each time an iteration happens. The subsequent value will depend on it as well.
    #Note that theta and omega must be the [-1] element so that we can always recall our last value of the list, otherwise this would be too cumbersome.
    
    theta_next = theta_now + omega_now * dt
    omega_next = omega_now - (g / L) * np.sin(theta_now) * dt
  
    #Append values to the array:
    theta_values.append(theta_next)
    omega_values.append(omega_next)

  #Have the function return each value of theta and omega:
  return np.array(theta_values), np.array(omega_values)

#And that is it for Euler's method! All we need to do from here is to input values into our function which will give us a list of our position and velocity at any point in time. Yay!

#Except we first have to compare the validity of this approximation. Let us see how similar this method is to a commonly used method. The Small Angle Approximation!
#If we let the side of the equation sin(θ_n) be equal to roughly θ_n then our differential equation will have the solution:
  #θ(t) = θ_initial * cos(2πf * t) ; where 2πf represents the frequency of our pendulum: 2πf = sqrt(g / L)
  #ω(t) = -(θ_initial * 2πf) * sin(2πf * t) ; this is the angular velocity function

#We can plot the values of these two functions as an array as well to compare it to the values obtained from the Euler Method approximation. By finding their difference, we will then be able to see how much they differ.

#For the small angle approximation, let's define the following function:
def small_angle(theta_intial, dt, num_steps):
  g = 9.81
  L = 1
  
  theta_values = [theta_initial]
  
  for i in range(num_steps):
    theta_now = theta_values[-1]
    theta_next = theta_initial * np.cos(np.sqrt(g / L) * t + i * dt)
