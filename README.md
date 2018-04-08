# Blav
Blav is a tool for the blind to navigate around. It uses a Qualcomm Dragonboard 410c for sensors and other data.

## How it was made
* The dragonboard collects data like webcam, distance, etc. and determines which direction to walk in using Machine Learning and Image Processing.
* The hasura backend is used to communicate between the dragonboard and the computer. It has a flask-restful api deployed.

## How does it detect
* Using image processing, we detect certain points on the 'sidewalks'. 
* Then, we run regression over it to get a polynomial.
* The angle of intersection between these two polynomials determines which direction to turn in. 

## Difficulties we ran into
* The dragonboard was a huge pain to get working as there isn't much documentation on it. The Hasura APIs had little to none documentation, which made it very hard to set up. 
* The biggest challenge we ran into was getting the dragonboard to output current through its GPIO pins. It sounds easy, but with almost no documentation about a certain include error, we took hours to resolve that.

## What's next
We would love to get this out in the real world and make our algorithm much more reliable.
![Lines of regression](https://github.com/vivek3141/NavigationForBlind/blob/master/Documentation/road.PNG)



