Title: What is k-Nearest Neighbors?
Date: 2018-02-25
tags: knn, kNN, k-nearest, neighbors, data science
og_image: /extra/delta9.png
headline: A short explanation of k-Nearest Neighbors
slug: k-nearest-Neighbors


k-Nearest Neighbors or kNN is a classification algorithm that asigns a class to a new data point based on known data points that are similar, or nearby.<br />
<br />
<b>What do you mean 'nearby'?</b><br />
To determine similarity of data you can use a few different distance algorithms. For example <i>Euclidian distance</i>, which is the square root of the sum of squares of the difference of the parameters of data points v and w.<br />
$$d=\sqrt{(v_1 - w_1)^2 + ...+(v_n - w_n)^2}$$

Or the <i>City Block/Manhattan distance</i> (yes that's what it's called) which is the sum of the absolute differences of v and w. <br />
$$d=|(v_1 - w_1)| + ...+|(v_n - w_n)|$$

Or the <i>Cosine distance</i>, which measures the "angle" between two parameter vectors v and w.<br />
$$d=\Bigg(1-\dfrac{vw'}{\sqrt{(vv')(ww')}}\Bigg)$$
</script>

<br />
<br />
<b>What does kNN do?</b><br />
It goes through all the known data points and measures the distance to the new point. Then it assigns the class of the majority of&nbsp;<i>k</i>&nbsp;nearest data points to the new measurement. Yes, it goes through all training data every time you run this algorithm! No model is actually created. This is called a <i>lazy learning </i>technique.<br />
<br />
<b>When should you use kNN?</b><br />
kNN is useful mostly when your parameter vectors are not too long. Or in other words, the dimensionality of your data is small. This is because the more dimensions, the more distances become similar to the average distance of any two points, even if these points have different labels. Basically, all distances become bigger and bigger; even if two points are in the same class, they will be very far apart in multi dimensional space. This is called the <i>curse of dimensionality.</i>  

&#916;9
