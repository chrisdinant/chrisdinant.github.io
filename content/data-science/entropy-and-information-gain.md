Title: Entropy and Information Gain
Date: 2018-03-17
Tags: entropy
Slug: entropy-and-information-gain
author: Chris Dinant
headline: The more homogeneous a set, the higher the entropy and the lower the amount of information.
Summary: Entropy and Information Gain

Neither 'Entropy' nor 'Information' are concepts with very intuitive definitions. Most people learn about entropy in chemistry class where it is used to describe the amount of 'order' in a system. But how do you translate 'order' into a mathematical equation? And what about information?  

In data science the terms 'Entropy' and 'Information Gain' are usually used in the context of decision trees. Here entropy describes the 'purity' of a set, which of course is equivalent to the order of a system in chemistry. Decision trees try to split up a dataset based on differences in a single feature such that the split results in the 'purest' branches, meaning the lowest amount of variation in the target variable. Then the branches are split again according to the same criterion, until we reach the point where all branches are pure, or we decide the model is strong enough. The entropy (or often you will see <i>cross-entropy </i>or<i> deviance</i> (<i>D</i>)) of a set is defined as follows:
$$D=-\sum_{k=1}^K\hat{p}_{mk}\log\hat{p}_{mk}$$
where
$p_{mk}$
is the probability, or fraction of the set <i>m</i>, for all data points of class <i>K</i>. The lower the entropy, the more pure the set. The split that results in the lowest sum of proportional entropies is chosen for each node. This combined in the definition for information gain which describes how much purer children are to their parent node.
$$IG=D_{ps}-\sum_{c=1}^C\hat{p}_{cs}D_{cs}$$
This is simply the difference in entropy of the parent <i>p</i>&nbsp;at split <i>s </i>and the average entropy of its children <i>C</i>.<br />
<br />
Some intuition:<br />
The more homogeneous a set, the higher the entropy and the lower the amount of information it contains. You want to increase the amount of information at each split to get accurate classifications.  


*This was published previously on my old blog*  
&#916;9
