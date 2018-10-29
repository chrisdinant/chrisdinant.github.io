Title: What's so naive about naive Bayes?
Date: 2018-10-28
Slug: naive-Bayes
tags: naive-Bayes
headline: Assuming feature independence tends to help classification accuracy

![Naive Art]({filename}/images/naive-art_ivan_generalic.jpg)
*Naive art by Ivan Generalic*

Naive Bayes (NB) is 'naive' because it makes the assumption that features of a measurement are independent of each other. This is naive because it is (almost) never true. Here is why NB works anyway.  

NB is a very intuitive classification algorithm. It asks the question, "Given these features, does this measurement belong to class A or B?", and answers it by taking the proportion of all previous measurements with the same features belonging to class A multiplied by the proportion of all measurements in class A. If this number is bigger then the corresponding calculation for class B then we say the measurement belongs in class A. Simple, right?  

Of course in practice we will rarely see many measurements with identical feature sets. In fact if we had to rely on a measurement to be identical to some previously measured data points we would only be able to classify exact duplicates, making Bayes' rule practically useless for classification.  

Now if instead we make the naive assumption that all features are independent of each other, then we don't have to rely on exact duplicates in our training data set to make a classification. We can simply take each feature separately and determine proportion of previous measurements that belong to class A that have the same value for this feature only. Then we do the same with all other features and take the product. We again multiply this with the proportion of class A in the data set and see if this number is larger than if we do the corresponding calculation for class B. It's cheating, but it works.  

The great thing about NB is that the naive assumption actually tends to help the classification. Think of it this way: if two features are actually dependent, say, hair length and gender, then assuming they are independent means you get to double-count evidence. If both gender and long hair are more associated with being a Justin Bieber fan, then assuming independence made you even more sure that she's a Belieber. And perhaps a bit naive.

*This was previously published by the Medium.com publication Towards Data Science, [here](https://towardsdatascience.com/whats-so-naive-about-naive-bayes-58166a6a9eba)*

&#916;9
