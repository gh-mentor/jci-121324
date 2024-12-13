"""
This app uses Python, numpy, matplotlib, and pandas to generate a set of data points and plot them on a graph.
"""

# import the necessary libraries
import numpy as np              # numpy is a library for numerical computing
import matplotlib.pyplot as plt # matplotlib is a library for plotting graphs
import pandas as pd             # pandas is a library for data manipulation

"""
Create a function 'gendatapoints' that generates a set of 100 data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the rang0 e of x values to generate.
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated as a non-linear function of x with excessive random noise: y = x ^ 1.5  + noise.
- The data frame is sorted by the 'x' values.
- The data frame has 100 rows.
Error Handling:
- Raise a ValueError if x_range is not a tuple of two integers.
- Raise a ValueError if x_range[0] is greater than x_range[1].
Examples:
- gendata((0, 100)) generates a data frame with 'x' values between 0 and 100.
- gendata((-100, 100)) generates a data frame with 'x' values between -100 and 100.
"""

def gendatapoints(x_range):
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(x, int) for x in x_range):
        raise ValueError("x_range must be a tuple of two integers")
    if x_range[0] > x_range[1]:
        raise ValueError("x_range[0] must be less than or equal to x_range[1]")
    np.random.seed(0)
    x = np.random.randint(x_range[0], x_range[1], 100)
    noise = np.random.normal(0, 10, 100)
    y = x ** 1.5 + noise
    data = pd.DataFrame({'x': x, 'y': y}).sort_values('x')
    return data

"""
Create a function 'plot_data' that plots the data points from the data frame.
Arguments:
- 'data' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- Plot the data points as a scatter plot.
- Add a title 'Data Points', x-axis label 'X', and y-axis label 'F(X)'.
"""

def plot_data(data):
    plt.scatter(data['x'], data['y'])
    plt.title('Data Points')
    plt.xlabel('X')
    plt.ylabel('F(X)')
    plt.show()

"""
Create a 'main' function that generates data points and plots them.
Arguments:
- None
Returns:
- None
Details:
- Generate data points using gendatapoints((-100, 100)).
- Plot the data points using plot_data.

"""

def main():
    data = gendatapoints((-100, 100))
    plot_data(data)

# Call the main function
if __name__ == "__main__":
    main()

# End of code

