#Questions=>
import numpy as np
from sklearn.linear_model import LinearRegression

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    s_x = sum(marketing_expenditure)
    s_y = sum(units_sold)
    xy = [] 
    for i in range (len(marketing_expenditure)):
        z= marketing_expenditure[i]*units_sold[i]
        xy.append(z)
    s_xy = sum(xy)
    sq_x = [number ** 2 for number in marketing_expenditure]
    s_sq_x = sum(sq_x)
    sq_y = [number ** 2 for number in units_sold]
    s_sq_y = sum(sq_y)   
    
    # calculating coefficients a and b for liner regression
    a=((s_y*s_sq_x) - (s_x*s_xy))/(len(marketing_expenditure)*s_sq_x - (s_x**2))
    b=(len(marketing_expenditure)*s_xy - (s_x*s_y))/(len(marketing_expenditure)*s_sq_x - (s_x**2))
    return (desired_units_sold-a)/b

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))
