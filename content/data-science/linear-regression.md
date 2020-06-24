Title: What is Linear Regression?
Date: 2018-03-05
tags: linear, regression, data science
og_image: /extra/delta9.png
headline: A short explanation of Linear Regression
slug: linear-regression

Linear regression is used to model the relationship between continuous variables. For example to predict the price of a house when you have features like size in square meters and crime in the neighborhood etc.&nbsp; A linear regression function takes the form of<br />
$$\hat{y}=\hat{\beta_0}+\hat{\beta_1}x_1+\hat{\beta_2}x_2+\dots+\hat{\beta_p}x_p$$

Here <i>y </i>is the target we're trying to predict (house price), the&nbsp;<i>x'</i>s are the <i>p&nbsp;</i>features or predictors (size, crime) and the <i>β</i>'s are the coefficients or the parameters that we are trying to estimate by fitting the model to data. The little hats on top of the&nbsp;<i>y </i>and&nbsp;<i>β</i>'s are called hats, and indicate we are dealing with estimates here.<br />
With multiple features it is called Multiple Linear Regression and when there's only one feature it is Simple Linear Regression.<br />
For Linear Regression the function does not have to be linear with regards to the predictors as long as it is linear in the parameters. This means that you can model interactions between predictors by, for example, multiplying <i>x</i>'s if this makes a better fit.<br />
$$\hat{y}=\hat{\beta_0}+\hat{\beta_1}x_1+\hat{\beta_2}x_2+\hat{\beta_3}x_1x_2+\dots+\hat{\beta_p}x_p$$

**How do you fit a model to data?**  
You estimate the&nbsp;<i>β</i>'s&nbsp;as the values that minimize the <i>sum of squared residuals, </i>which is the squared difference between the actual value <i>y</i>&nbsp;and the estimated <i>y-hat </i>summed for all <i>x</i>'s. Or<br />
$$\displaystyle\sum_{i=1}^n(y_i-\hat{\beta_0}-\hat{\beta_1}x_{i1}-\hat{\beta_2}x_{i2}-\dots-\hat{\beta_p}x_{ip})^2$$

**When should you use Linear Regression?**  
As a guideline, with any regression problem, try linear regression first and move on to other methods when it is not good enough. This choice should be based on considerations like whether the model under- or overfits the data.  

&#916;9
