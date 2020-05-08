import matplotlib.pyplot as plt
from numpy import *
import numpy as np

#10 main lines of code below
def linear_regression(X, y, m, c, epochs=1000, learning_rate=0.0001):
     N = float(len(y))
     for i in range(epochs):
          y_guess = (m * X) + c
          error = sum([data**2 for data in (y_guess-y)]) / N
          #print error
          small_value_of_m = (2/N) * sum(X * (y_guess - y))
          small_value_of_c = (2/N) * sum(y_guess - y)
          m = m - (learning_rate * small_value_of_m)
          c = c - (learning_rate * small_value_of_c)
     return m, c, error

def run():
	m = 1
	c = 1
 	#Read data from CSV file
	points = genfromtxt("advertising-sales-data.txt", delimiter=",")
	#print points
	#print points[:,0] #first column from data
	#print points[:,1] #second column from data
	best_fit_m, best_fit_c, minimum_error = linear_regression(points[:,0], points[:,1], m, c)
	#print best_fit_m, best_fit_c, minimum_error
	#Plotting points and axes
	plt.plot(points[:,0], points[:,1], 'b*')
	plt.xlabel('Ad investment (In 1000s of rupees)')
	plt.ylabel('Sales output (In 1000s of rupees)')
	plt.axis([0, 12, 0, 60])
	plt.grid(True)
	#Plotting initial line
	x_values = np.linspace(0,12,10)
	y_values = m*x_values + c
	plt.plot(x_values, y_values, '-r', label='Starting Line')
	#Plotting final line with updated values of m and b
	x_data = np.linspace(0,12,10)
	y_data = best_fit_m*x_data+best_fit_c
	plt.plot(x_data, y_data, '-g', label='Best Fit Line')
	plt.legend(loc='best')
	plt.show()

if __name__ == '__main__':
    run()

#Source - https://towardsdatascience.com/linear-regression-using-gradient-descent-in-10-lines-of-code-642f995339c0
