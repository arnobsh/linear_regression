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

![Higher Dimension][Higher Dimension]

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
[Higher Dimension]: ../resources/higher_dimention.PNG "Higher Dimension"