Title: What is Gradient Descent?
Date: 2018-11-03
tags: gradient descent, partial derivative, cost function, weights, biases, neural network, deep learning, data science
slug: gradient-descent
author: chris dinant
headline: Gradient descent updates the parameters of a model so that the output of the cost function is reduced.
og_image: /images/descending.jpg
cover: /images/descending.jpg

Fitting a machine learning model means finding optimal values for the parameters of the model. Sometimes this can be done in one step (when a closed form solution is available), but more often than not even if this can be done it is computationally prohibitively expensive. That is why most of the time iterative methods such as gradient descent are used for optimization problems.  

With gradient descent at every iteration the parameters $w$ and $b$ (for *weights* and *biases*) are adjusted a certain amount in the direction that results in the reduction of the cost function $J$. So how do we determine the direction and amount to adjust? We use the gradient of the cost function with regards to the parameters.  

Here's how calculate this gradient:  

The cost function takes the output of the model $\hat{y}$ and compares it with the actual value of the training sample, $y$, to determine how *wrong* the model is at this stage of training. Often you see functions like *mean squared error* (MSE) or *cross entropy* used for this. The $\hat{y}$ value in turn is determined by the activation  at the output layer (if we are talking about a neural network), which in the case of a binary classification problem would probably be a sigmoid function. And the input to this sigmoid function would be a linear function in the style of $$z=w_1x_1 + w_2x_2 + ... + w_Nx_N + b$$ for a fully-connected layer with $N$ neurons. Now, to take the derivative of cost function $J$ with regards to the parameters you take the (partial) derivatives of $J$ at each of the above steps and multiply them with each other. This is called the chain rule. It goes as follows:  

1. If we are using cross entropy, the derivative of $J$ with regards to $\hat{y}$ is:  $$\frac{\partial{J}}{\partial{\hat{y}}}=-\frac{y}{\hat{y}}+\frac{1-y}{1-\hat{y}}$$  
2. One step down the derivative of $\hat{y}$ with regards to the output of the linear function (let's call it $z$) is:
$$\frac{\partial{\hat{y}}}{\partial{z}}=\hat{y}(1-\hat{y})$$  
3. And the partial derivative for the parameters is:
$$\frac{\partial{z}}{\partial{w_n}}=x_n$$ for all the weights and simply $1$ for bias $b$.  

A funny thing about using a sigmoid activation function in the output layer and cross entropy as the loss function is that with the chain rule this end of the network simplifies to:
$$\frac{\partial{J}}{\partial{w_n}}=\frac{\partial{J}}{\partial{\hat{y}}}\frac{\partial{\hat{y}}}{\partial{z}}\frac{\partial{z}}{\partial{w_n}}=x_n(\hat{y}-y)$$
for the weights and $\hat{y}-y$ for the bias. Isn't that nice and simple?

Now we can adjust the parameters as follows:
$$\Delta{w_n}=-\alpha{\frac{\partial{J}}{\partial{w_n}}}$$
We use a small scalar $\alpha$ here, always $<1$ and often $<0.01$, in order not to update the parameters in too large steps because this usually leads to increasing $J$ instead of decreasing it. This $\alpha$ is called the *learning rate*.  
-------------------------
With multi-layer networks the $x_n$ in the above equations is equivalent to the output of the previous activation layer. So to continue back propagation into the upstream layer you take the derivative of $z$ with regards to this activation (let's call it $a^{[l-1]}$ instead of $x$ now to make clear that we are not dealing with the features of the input sample but the activation of upstream layer $l-1$):
$$\frac{\partial{z}}{\partial{a_n^{[l-1]}}}=w_n$$

Next we need the derivative of this activation function $a^{[l-1]}$ with regards to $z^{[l-1]}$. Obviously the formula for this derivation depends on which activation function you choose. Here are some common ones:  

|function|<div style="text-align: center">equation</div>|<div style="text-align: center">derivative</div>|
|--------|:--------:|:----------:|
|Linear  |$$f(x)=x$$   |$$f'(x)=1$$|
|Sigmoid |$$f(x)=\frac{1}{1+e^{-x}}$$|$$f'(x)=f(x)(1-f(x))$$|
|ReLU|$$f(x)=\begin{cases}  0 & \text{for }x<0\\  x & \text{for }x\ge0\end{cases}$$|$$f(x)=\begin{cases}  0 & \text{for }x<0\\  1 & \text{for }x\ge0\end{cases}$$|
|Tanh    |$$f(x)=\frac{2}{1+e^{-2x}}-1$$|$$f'(x)=1-f(x)^2$$|

Say we use Tanh:
$$\frac{\partial{a_n^{[l-1]}}}{\partial{z^{[l-1]}}}=1-a_n^{[l-1]2}$$
And finally the derivative with regards to the parameters of layer $l-1$:
$$\frac{\partial{z^{[l-1]}}}{\partial{w_n^{[l-1]}}}=x_n^{[l-1]}$$

Again we apply the chain rule to update of the weights in layer $l-1$:
$$\Delta{w_n^{[l-1]}}=-\alpha{\frac{\partial{J}}{\partial{w_n^{[l-1]}}}}=-\alpha{x_n^{[l-1]}(1-a_n^{[l-1]2})w_n(\hat{y}-y)}$$
where $a_n^{[l-1]}$ is the output of tanh$(x^{[l-1]})$ and $\hat{y}$ the output of sigmoid$(x)$.  

--------------------------
Now we have seen how to do back propagation by gradient descent for a two-layer neural network. I have not talked about how to deal with batches of data and how to vectorize these calculations for faster computation. We will have to wait for a later post to talk about those topics.   

&#916;9
