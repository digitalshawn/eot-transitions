# End of Term Transitions

Mohamed Aturban (Old Dominion University)

Justin Littman (George Washington University)

Jessica Ogden (University of Southampton)

Yu Xu (University of Southern California)

Shawn Walker (University of Washington)

## Project Background
This project came about as part of the Archives Unleashed 3.0 event hosted at the Internet Archive Feb 23-24, 2017. The group came together around an interest in using the End of Term web archives to assess change in the web presence of each presidential administration - at the time of transition. We hoped to use multiple ways of characterising six government domains over a three month period around the  2001/2005/2009/2013/2017 transitions. The goal was to assess whether the rate and type of change between different administrations. The following is a sketch of what we did and some of our preliminary findings.

## Metrics for measuring change
The team brainstormed various achievable metrics for observing change in the web presence of each administration.
* Side-by-Side Visual
* Simhash Distance
* Edit Distance
* Link Structure

## Regresssion Analysis
We propose three possible mechanisms that can explain the variations in the rate of change of governmental websites during the period of term transition.

Independent variable 1: The date that is after the presidential inaguration (coded as 1, otherwise coded as 0)
Indenpedent variable 2: The abolsute number of the time distance to the inauguration date (a count variable)
Independent variable 3: Power transitions between the two parties (coded as 1, otherwise coded as 0)

There are two measures for the rate of change: 1. The simhash score; 2. The tf-idf score.

Methods: we estimated fixed-effects models by using the raw scores for time-variant variables across waves. By focusing merely on intra-level variation, our fixed-effects models account for unobserved heterogeneity between observations and control for the effects of stable characteristics／factors on the dependent variables (Allison, 2009). By doing this, we are able to make a stronger causal claim.

Results: 
1. Power transistions between the two parties reduces the rate of change of the Whitehouse webiste. But the transitions lead to an increase in the change rate of the websites of EPA, HHS, and VA.
2. Distance to the inauguration date increase the rate of change of the Whitehouse website.

## Broad Findings

## Future directions
1. Explaining why power transitions can generate differtial effects on the rate of change of different governmental websites.


