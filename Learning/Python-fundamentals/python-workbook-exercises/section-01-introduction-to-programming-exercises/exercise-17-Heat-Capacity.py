'''Q17:- The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 J
g◦C. Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
in this exercise.

Extend your program so that it also computes the cost of heating the water. 
Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.Exercise 17: Heat Capacity 9

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.'''

"""
Summary:- This program can tell amount of energy required to heat a certain amount of water to certian degree celcius 
          and what will be the  cost heating.
"""

# taking user input to place the value in the fomula q = mCΔT.
# where q = amount of energy required to heat the water, which we have to calculate
# m=mass of the given water
# C=specific heat capacity,in this case specific heat capacity of the water
# ΔT= is change in temperature

mass=float(input("\nenter the mass of water in grams:- "))
temp_change=float(input("\nenter the change in temperature in degree celcius :- "))

# Specific heat capacity of water is 4.186
shc_h2o=4.186

# calulating the amount of energy required to heat the water
q=mass*shc_h2o*temp_change

# printing the amount of energy required to heat the water
print(f"\ntotal amount of energy require to heat a of {mass} grams of water to {temp_change} degree celcius\
  is = {q} joules")

# 1 KWh (kilowatt per hour) = 3600000 Joules

# converting joules into kilowatt per hour and calculating the cost of heating the water
cost=q/3600000*8.99

# printing cost of boling water for coffee
print(f"\nCost of electricity boiling {mass} grams of water for coffee = {cost} cents \n")

# Greeting message
print("HAVE NICE DAY :)\n")