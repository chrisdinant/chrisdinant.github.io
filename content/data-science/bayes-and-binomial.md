Title: Bayes and Binomial Theorems
Date: 2018-02-06
tags: bayes, binomial, data science, tests
og_image: /images/dice.jpeg
headline: Our intuitions about test accuracy are often very inaccurate
cover: /images/numbers.jpg

**Bayes Theorem**  
In statistics there are many situations where you want to determine the probability that a sample for which you have certain measurement belongs to a certain set. Say you want to know the chance that you have HIV if you test positive. No test is perfect, so this probability will depend on the test sensitivity, but also on the specificity and on the incidence in the population, or set, that you belong to. Bayes Theorem is a simply the logic you have to apply to estimate such probabilities.<br />
<br />
As a cancer researcher my attention was naturally drawn to this paper currently trending on Pubmed: <a href="https://www.ncbi.nlm.nih.gov/pubmed/29348365/"><i>Detection and localization of surgically resectable cancers with a multi-analyte blood test.</i></a> This is a perfect practical example for applying Bayes rule! And most of the information we need is right there in the abstract: "<i>The </i>sensitivities<i> ranged from 69% to 98% for the detection of five cancer types (ovary, liver, stomach, pancreas, and esophagus)...</i>" and "<i>The </i>specificity<i> of CancerSEEK was &gt; 99%: only 7 of 812 healthy controls scored positive.</i>" Wow, a <i>sensitivity</i> of up to 98% and a <i>specificity</i> of more than 99%? This sounds like a fool proof test! Right? Now we just need to know the incidences for these cancers and we can see how likely it is that you have that type of cancer given a positive test score.<br />
<br />
<!-- <table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"> -->
<img src="{static}/images/dr-john.jpg", alt="doctor john", style="margin-left: auto; margin-right: auto; text-align: center;"/>
<!-- </td></tr>  
</tbody></table> -->
<p style="text-align: center; font-size: 0.8em;"><i>The Doctor is in.</i></p>
<div class="sub">
<br /></div>
This is Bayes Theorem in math notation:<br />
<br />
$$P(A|B)=\dfrac{P(B|A)\cdot{P(A)}}{P(B)}$$
<br />
<br />
Now replace <i>'A'</i> with <i>'having cancer'</i> and <i>'B'</i> with <i>'testing positive'</i> so we can read this as: "The probability of having cancer given a positive test result (the '<i>posterior</i>', what we want to calculate) is equal to the probability of testing positive given that you have cancer (this is the '<i>sensitivity</i>') times the probability of having cancer (the '<i>prior</i>', which is the incidence of cancer in your population) divided by the probability of testing positive." The <i>specificity</i> is encompassed in the denominator as follows:<br />
<br />
$$P(B)=P(B|A)\cdot{P(A)}+P(B|\neg{A})\cdot{P(\neg{A})}$$
<br />
<br />
where
$P(B|\neg{A})$
is the probability of a <i>positive test</i> given that you <i>do not have cancer</i>, which is the inverse of the <i>specificity</i>, or the chance of getting a false positive result. The other parts of the denominator are the <i>sensitivity</i> times the <i>prior</i>, as seen in the numerator and the probability of <i>not having cancer</i> in your population.<br />
For the incidence of cancer (I picked esophagus cancer for this calculation), Google tells us this is about 4 people per 100,000. So let's put in the numbers:<br />
<br />
$$P(A|B)=\dfrac{0.98\cdot{0.00004}}{(0.98\cdot{0.00004})+(1-0.99)\cdot{(1-0.00004)}}=0.0039$$
<br />
<br />
So if you go in without any symptoms (which is what you want if you want to avoid these cancers, symptoms often mean it is already too late), and take this test, a positive result will increase your risk from&nbsp; 0.004% to 0.4%. Still not very scary, right? Is that surprising?<br />
<br />
What we can learn from this is that intuition from numbers about test <i>accuracy </i>is often very inaccurate. If you are a doctor using these kind of tests you better know what probabilities you are dealing with (don't worry, doctors know this) and do an independent second screen for the same cancer. Because this brings us to the real power of Bayes Theorem: After the first test, our <i>posterior</i> becomes the new <i>prior</i>: we can update our probabilities in light of new information! In other words: after taking the test you don't belong to the general population anymore, now you're a part of the population that tested positive. And in this population the cancer incidence is 0.4%. Just change the numbers for the <i>sensitivity</i>, <i>specificity</i> and replace the old <i>prior</i> with the <i>posterior</i> and you get a new <i>posterior</i>. If this second test (perhaps a scan of some sorts) is equally effective as the blood test above, then a positive outcome will increase the likelihood of you really having cancer from 0.4% to almost 30%. Still not super likely, but a bit more cause for worry.<br />
<br />
Where a test like this really works well though is when you know you are in a high-risk population, e.g. when you have a genetic disposition for a certain kind of cancer (a BRCA1 or BRCA2 mutation for example). In such cases the sample space is drastically reduced and the test can be almost perfect. In the case of BRCA1 mutations where your chance of getting ovarian cancer sometime during your lifetime increases from 1.4% to almost 40% a positive test result will be correct more than 98% of the time.<br />
<br />
<br />
<br />
<b>Combining the Bayes and the Binomial Theorem</b><br />
This is the binomial theorem:
$$\binom{n}{k}\cdot{p^k}\cdot{(1-p)}^{(n-k)}$$
<br />
The first part is the binomial equation and is pronounced <i>n choose k</i>, I (plan to) talk about this in another post, and p stands for <i>probability</i>. The binomial theorem is used to calculate probabilities when there is a binary outcome of an event <i>k</i> out of <i>n</i> total events and the probability of outcome <i>k</i> equals <i>p</i>. Example: <i>What is the probability that you throw exactly 23 sixes (k = 23) in 30 throws (n=30) of a die (p = 1/6)?&nbsp;</i>With the binomial theorem this is a piece of cake. (
$7.2^{-13}$)
<br />
<br />
<!-- <table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"> -->
<img src="{static}/images/dice.jpeg", alt="dices", style="margin-left: auto; margin-right: auto; text-align: center;"/>
<!-- </td></tr>  
</tbody></table> -->
<p style="text-align: center; font-size: 0.8em;"><i></i></p>
<br />
<br />
<br />
It gets a bit more interesting when you combine Bayes with the Binomial Theorem.<br />
Let's give a nerdy cell biologist example: Say you have two cell lines in culture (U2OS and HeLa for example) and you transfer both cell lines into a new flask. The next day you go back to the incubator and see that you have forgotten to label the flasks, so you don't know which is which. How can you find out? Here's what you could do: U2OS and HeLa don't look exactly the same under a microscope.<br />
<!-- <table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"> -->
<img src="{static}/images/hela.jpg", alt="hela", style="margin-left: auto; margin-right: auto; text-align: center;"/>
<!-- </td></tr>  
</tbody></table> -->
<!-- <p style="text-align: center; font-size: 0.8em;"><i></i></p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"> -->
<img src="{static}/images/u2os.jpg", alt="u2os", style="margin-left: auto; margin-right: auto; text-align: center;"/>
<!-- </td></tr>  
</tbody></table> -->
<p style="text-align: center; font-size: 0.8em;"><i></i></p>
It's not directly straight forward unless you have a lot of experience what the difference is, but image analysis software can measure a bunch of features for each cell line and give you numbers to work with. Let's say that a feature describing the shape (<i>s</i>) of a nucleus falls within a certain range <i>r&nbsp;</i>(the values don't matter) 20% of the time for U2OS cells and 23% of the time for HeLa cells. Now you take one image of 180 cells of one of the dishes and measure this shape value. In 51 cells the value for <i>s </i>falls in range <i>r</i>. Now we can use Bayes and the Binomial Theorem together to determine if we're looking at U2OS or HeLa!<br />
<br />
$$P(\text{HeLa}|51 \text{ out of } 180) = \dfrac{P(51 \text{ out of }180 | \text{HeLa}) \cdot{P(\text{HeLa})}}{P(51 \text{ out of } 180)}$$
<br />
<br />
This gives <br />
<br />
$$\dfrac{\displaystyle\binom{180}{51}\cdot{0.23^{51}}\cdot{(1-0.23)^{(180-51)}} \cdot{0.5}}{\text{the numerator again} + \displaystyle\binom{180}{51}\cdot{0.2^{51}}\cdot{(1-0.2)^{(180-51)}} \cdot{0.5}} = 0.9000$$
</script>
<br />
<br />
Which makes it 90.0% certain that you are looking at HeLa cells. I would be confident enough to label the flasks correctly now. Which I did... ahem.<br />
<br />
<br />
This blog post was inspired by this course on coursera.org: <a href="https://www.coursera.org/learn/datasciencemathskills">https://www.coursera.org/learn/datasciencemathskills</a>  

&#916;9
