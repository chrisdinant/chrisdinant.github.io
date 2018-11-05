Title: What is Gradient Descent?
Date: 2018-11-03
tags: gradient descent, partial derivative, cost function, weights, biases, neural network, deep learning, data science
slug: gradient-descent
author: chris dinant
Summary: Gradient descent updates the parameters of a model so that the output of the cost function is reduced.
og_image: /images/descending.jpg
cover: /images/descending.jpg
Status: draft

Fitting a machine learning model means finding optimal values for the parameters of the model. Sometimes this can be done in one step (when a closed form solution is available), but more often than not even if this can be done it is computationally prohibitively expensive. That is why most of the time iterative methods such as gradient descent are used for optimization problems.  

With gradient descent at every iteration the parameters $w$ and $b$ (for *weights* and *biases*) are adjusted a certain amount in the direction that results in the reduction of the cost function $J$. So how do we determine the direction and amount to adjust? We use the gradient of the cost function with regards to the parameters.  

Here's how calculate this gradient:  

The cost function takes the output of the model $\hat{y}$ and compares it with the actual value of the training sample, $y$, to determine how *wrong* the model is at this stage of training. Often you see functions like *mean squared error* (MSE) or *cross entropy* used for this. The $\hat{y}$ value in turn is determined by the activation  at the output layer (if we are talking about a neural network), which in the case of a binary classification problem would probably be a sigmoid function. And the input to this sigmoid function would be a linear function in the style of $$w_1x_1 + w_2x_2 + ... + w_Nx_N + b$$ for a fully-connected layer with $N$ neurons. Now, to take the derivative of cost function $J$ with regards to the parameters you take the (partial) derivatives of $J$ at each of the above steps and multiply them with each other. This is called the chain rule. It goes as follows:  
1. If we are using cross entropy, the derivative of $J$ with regards to $\hat{y}$ is:  $$\frac{\partial{J}}{\partial{\hat{y}}}=-\frac{y}{\hat{y}}+\frac{1-y}{1-\hat{y}}$$  
2. One step down the derivative of $\hat{y}$ with regards to the output of the linear function (let's call it $z$) is:
$$\frac{\partial{\hat{y}}}{\partial{z}}=\hat{y}(1-\hat{y})$$  
3. And the partial derivative for the parameters is:
$$\frac{\partial{z}}{\partial{w_n}}=x_n$$ for all the weights and simply $1$ for bias $b$.  

A funny thing about using a sigmoid activation function in the output layer and cross entropy as the loss function is that with the chain rule this end of the network simplifies to:
$$\frac{\partial{J}}{\partial{w_n}}=\frac{\partial{J}}{\partial{\hat{y}}}\frac{\partial{\hat{y}}}{\partial{z}}\frac{\partial{z}}{\partial{w_n}}=x_n(\hat{y}-y)$$
for the weights and $\hat{y}-y$ for the bias.  

Now we can adjust the parameters as follows:
$$\Delta{w_n}=-\alpha{\frac{\partial{J}}{\partial{w_n}}}$$
We use a small scalar $\alpha$ here, always $<1$ and often $<0.01$, in order not to update the parameters in too large steps because this usually leads to increasing $J$ instead of decreasing it. This $\alpha$ is called the learning rate.  
