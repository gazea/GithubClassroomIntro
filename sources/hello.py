# import required packages
import numpy as np

# function declaration
def circumference(radius, dp=3):
  # correct formula, make sure it only returns 3 dp
    circumf = round(2*np.pi*radius, dp)
    return circumf
