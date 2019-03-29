# Linear Regression

### Moving A Line

![Moving A Line][Moving A Line]

### Absolute Trick

![Absolute Trick][Absolute Trick]

![Absolute Trick With Positive Value][Absolute Trick With Positive Value]

![Absolute Trick With Negative Value][Absolute Trick With Negative Value]

### Square Trick

![Square Trick][Square Trick]

### Mean Absolute Error

![Mean Absolute Error][Mean Absolute Error]

### Mean Squared Error

![Mean Squared Error][Mean Squared Error]

### Minimizing Error Function

![Minimizing Error Function][Minimizing Error Function]

#### Development of the derivative of the error function

![Derivative Error Function][Derivative Error Function]

![Derivative Error Function 2][Derivative Error Function 2]

### Mean vs Total Squared

![Mean vs Total Squared][Mean vs Total Squared]

### Batch vs Stochastic Gradient Descent

At this point, it seems that we've seen two ways of doing linear regression.

* By applying the squared (or absolute) trick at every point in our data one by one, and repeating this process many times.
* By applying the squared (or absolute) trick at every point in our data all at the same time, and repeating this process many times.

More specifically, the squared (or absolute) trick, when applied to a point, gives us some values to add to the weights of the model. We can add these values, update our weights, and then apply the squared (or absolute) trick on the next point. Or we can calculate these values for all the points, add them, and then update the weights with the sum of these values.

The latter is called batch gradient descent. The former is called stochastic gradient descent.

![Batch Vs Stochastic Gradient Descent][Batch Vs Stochastic Gradient Descent]

### Higher Dimension

![Higher Dimension Multiple Values][Higher Dimension Multiple Values]
![Higher Dimension][Higher Dimension]

### Multiple Linear Regression

A predictor is a variable you're looking at in order to make predictions about other variables, while the values you are trying to predict are known as dependent variables.

In X, Y dataset of single predict, If X is the predictable data set , Y will be dependent on X values. SO we we ant to to predict X it will depend on the Y values which is dependent on X.

We can do that using multiple linear regression. If the outcome you want to predict depends on more than one variable, you can make a more complicated model that takes this into account. As long as they're relevant to the situation, using more independent/predictor variables can help you get a better prediction.

When there's just one predictor, the linear regression model is a line, but as you add more predictor variables, you're adding more dimensions to the picture.

When you have one predictor variable, the equation of the line is

y = m x + b 

and the plot might look something like this:

![Multiple Linear Regression With One Predictor][Multiple Linear Regression With One Predictor]

Adding a predictor variable to go to two predictor variables means that the predicting equation is:

y = m_1 x_1 + m_2 x_2 + b

To represent this graphically, we'll need a three-dimensional plot, with the linear regression model represented as a plane:

![Multiple Linear Regression With Two Predictor][Multiple Linear Regression With Two Predictor]

You can use more than two predictor variables - in fact, you should use as many as is useful! If you use nn predictor variables, then the model can be represented by the equation

y = m_{1} x_{1} + m_{2} x_{2} + m_{3} x_{3}+ ... +m_{n} x_{n} + b

###  Closed form solution math

#### Mean Squared Error For Two Dimension

![Mean Squared Error For Two Dimension][Mean Squared Error For Two Dimension]

### Polynomial Regression

![Polynomial Regression][Polynomial Regression]

[//]: # (Image References)

[Moving A Line]: ../resources/moving_a_line.PNG "Moving A Line"
[Absolute Trick]: ../resources/absolute_trick.PNG "Absolute Trick"
[Absolute Trick With Positive Value]: ../resources/absolute_trick_with_equation_positive.PNG "Absolute Trick With Positive Value"
[Absolute Trick With Negative Value]: ../resources/absolute_trick_with_equation_negative.PNG "Absolute Trick With Negative Value"
[Square Trick]: ../resources/square_trick.PNG "Square Trick"
[Mean Absolute Error]: ../resources/mean_absolute_error.PNG "Mean Absolute Error"
[Mean Squared Error]: ../resources/mean_squared_error.PNG "Mean Squared Error"
[Minimizing Error Function]: ../resources/minimizing_error_function.PNG "Minimizing Error Function"
[Derivative Error Function]: ../resources/derivative_error_function.PNG "Derivative Error Function"
[Derivative Error Function 2]: ../resources/derivative_error_function_2.jpg "Derivative Error Function 2"
[Mean vs Total Squared]: ../resources/mean_vs_total_squared.PNG "Mean vs Total Squared"
[Batch Vs Stochastic Gradient Descent]: ../resources/batch_vs_stochastic_gradient_descent.PNG "Batch Vs Stochastic Gradient Descent"
[Higher Dimension Multiple Values]: ../resources/higher_dimention_multiple_values.PNG "Higher Dimension Multiple Values"
[Multiple Linear Regression With One Predictor]: ../resources/linear_regression_with_one_predictation_varaible.PNG "Multiple Linear Regression With One Predictor"
[Multiple Linear Regression With Two Predictor]: ../resources/linear_regression_with_two_predictation_varaible.PNG "Multiple Linear Regression With Two Predictor"
[Mean Squared Error For Two Dimension]: ../resources/mean_squared_error_w1_w2.PNG "Mean Squared Error For Two Dimension"
[Polynomial Regression]: ../resources/polynomial_regression.PNG "Polynomial Regression"