Title: What is Logistic Regression?
slug: logistic-regression
tags: logistic, regression, classification, data science
og_image: /extra/delta9.png
headline: A short explanation of Logistic Regression
Date: 2018-03-06

*Logistic Regression is closely related to Linear Regression. Read my post on Linear Regression [here]({filename}/data-science/linear-regression.md)*  

Logistic Regression is a classification technique, meaning that the target <i>Y</i>&nbsp;is qualitative instead of quantitative. For example, trying to predict whether a customer will stop doing business with you, a.k.a. churn.<br />
Logistic Regression models the probability that a measurement belongs to a class:<br />

$$P(Y=k|X=x)$$

If we would try to predict the target value directly, (let's say churn = 1 and not-churn = 0), as you would with Linear Regression, the model might output negative target values or values larger than 1 for certain predictor values. Probabilities smaller than zero or larger than 1 make no sense, so instead we can use the logistic, or sigmoid, function to model probabilities.<br />
$$p(X)=\dfrac{e^{\beta_0+\beta_1X}}{1+e^{\beta_0+\beta_1X}}$$

This is also:
<br />
$$p(X)=\dfrac{1}{1+e^{-\beta_0-\beta_1X}}$$

which is the form you usually see it in when it is used as the activation function in a neural network layer.<br />
This function will only output values between 0 and 1, which you can then use as is if you need probabilities (i.e. the probability that a customer will churn), or you can use a threshold, say at p(x) &gt; 0.5 for class 1 if you want to do classification.<br />
<br />
<b>How do you fit the Logistic Regression model to data?</b><br />
For this we use the <i>Maximum Likelihood</i> method. This tries to maximize the product of the logistic function for all <i>x</i>'s where&nbsp;<i>y = 1</i>&nbsp;and one minus this where <i>y = 0</i>:<br />
<br />
$$l(\beta_0,\beta_1)=\displaystyle\prod_{i:y=1}p(x_i)\displaystyle\prod_{i':y_{i'}=0}(1-p(x_i'))$$

Logistic Regression can be extended to more than two class problems, but in practice other algorithms are usually preferred for this.  

&#916;9
