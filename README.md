## Linear Regression Model

The linear regression model is represented as:

$y = mx + b$

Where:
- $y$ is the predicted value (in this case, the predicted salary).
- $m$ is the slope (or coefficient) of the linear model.
- $b$ is the intercept (or bias) of the linear model.
- $x$ is the input feature, which represents years of experience.

## Cost Function (Mean Squared Error)

The cost function measures the error between the predicted values ($y$) and the actual values ($y_i$). For linear regression, the cost function is typically the Mean Squared Error (MSE), defined as:

$J(m, b) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - (mx_i + b))^2$

Where:
- $J(m, b)$ is the cost function, which quantifies how well the model fits the data.
- $n$ is the number of data points in the dataset.
- $y_i$ is the actual value (salary) for the $i$th data point.
- $x_i$ is the input feature (years of experience) for the $i$th data point.
- $m$ and $b$ are the parameters of the linear model that we want to optimize to minimize the cost function.

## Gradient Descent Updates

Gradient descent is an iterative optimization algorithm used to find the values of $m$ and $b$ that minimize the cost function $J(m, b)$. The key idea is to update the parameters $m$ and $b$ in the direction of steepest decrease in the cost function. This is done by computing the gradients of the cost function with respect to $m$ and $b$, denoted as $\frac{\partial J}{\partial m}$ and $\frac{\partial J}{\partial b}$, respectively.

The update formulas for $m$ and $b$ are as follows:

### Update for $m$:

$m = m - l \cdot \frac{\partial J}{\partial m}$

Where:
- $m$ is the current value of the slope.
- $l$ is the learning rate, which controls the step size of the updates.
- $\frac{\partial J}{\partial m}$ is the gradient of the cost function with respect to $m$.

### Update for $b$:

$b = b - l \cdot \frac{\partial J}{\partial b}$

Where:
- $b$ is the current value of the intercept.
- $l$ is the learning rate.
- $\frac{\partial J}{\partial b}$ is the gradient of the cost function with respect to $b$.

These update formulas are applied iteratively for a specified number of epochs (iterations) to gradually adjust the values of $m$ and $b$ and minimize the cost function. The learning rate ($l$) controls the step size of each update, ensuring that the algorithm converges to the optimal values of $m$ and $b$ that provide the best linear fit to the data.
