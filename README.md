# Planning for drunks
https://github.com/zzncnb/geog5990-assignment2

Build the animation model to show where drunks walk when they are trying to get home.

## Usages

The model has been used to generate the route for 25 drunks with Unique ID number to get back to their home with same ID number. 

## Code status and development roadmap
This code is developed and tested. 

When running the drunkplan.py, it will open up a tkinter window to run the animation model. All the drunks will walk to their home as required. When running the model, it will create a density map as text file to draw the density of drunks passing through each point on the map. 

Code is stored into the folder named drunk. There are 4 files inside the folder named drunk which are: density.txt, drunk.plan.txt, drunk.py and drunkplan.py. 

drunk.plan.txt file is downloaded from the the website as the source data to load the map. It is a 300 x 300 pixel raster file of the town plan. Each line in the file is a line in the raster image, starting at the top left corner. The background is denoted by the number zero, the pub by one's and the house by the other numbers. 

URL for download the data: https://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/drunk.plan 

URL for viewing the GIF verison of the town plan map: https://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/drunk.gif

density.txt is the desnsity map that is created to show the density of drunks passing through each point on the map. 

drunk.py is created to store passPoints for drunk's start point and all the point when walking to their home.

drunkplan.py is created to help drunks walk back to their home. 

Roadmap for running the model. 

1. Pull in the data file and finds out the pub point and the home points.
2. Draws the pub and homes on the screen.
3. Models the drunks leaving their pub and reaching their homes, and stores how many drunks pass through each point on the map.
4. Draws the density of drunks passing through each point on a map.
5. saves the density map to a file as text. 

Roadmap for basic algorithm:
* Each drunk (who will have numbers between 0 and 250 assigned before leaving the pub), move the drunk randomlyh left/right/up/down in a loop that picks randomly the way it will go. When it hits the correctly numbered house, stop the process and start with the next drunk. At each step for each drunk, add one to the desity for that point on the map. 


Roadmap for Algorithm in the model:

1. drunk. py

* Drunks' start point is the center of the pub.
* First, drunks will get their home coordinate. Since the home is a square, it is needed to pick the point with shortest distance to start point as the home's coordinate point. 
* Drunks start from start point. It's time to make decision on which direction to walk (It should be either 0 or 1 ). Find which point is closest to home and put that point into passPoints (passPoints is an empty list).
Originally, passPoints only has start point inside it. Assume, the start point picks next point as B, passPoints  becomes (Start point, A), and then make judgement on point A.  The rest can be done in the same method till the distance for drunks to their home is 1 which means drunks are standing at the point that is next to the point of their homes. In this way, the passPoints stores all the points that drunks walk to their homes. 

2. drunkplan.py

* Using 10, 20, ....., 250 as initialize objects for drunks. Then every object uses the move funtion to get their route points to their home. 

* When getting the route for each drunk,  it's time to refresh the steps needed to drunk's home because the walking steps are different for drunks. For example, some drunks need 130 steps to get back to their home and others need 200 steps.  For the procedure of of refreshing the steps, it requires to refresh according to the maximum steps needed to drunk's home. For example: if refreshes at 130 steps when the maximum steps needed for some drunks to home is 200 steps, drunks with 200 steps home can't get back to their home. In this way, if it refreshes at 200 steps, it only needs to let all the drunks with 130 steps home stay at home and keep refreshing the portion of steps from 131 to 200. In this case, all the drunks will be able to finish their walk to their home when the refresh finishes. 


## Acknowledgements

The model development is instructed by the guidence of the assignemt webpage from course GEOG5990M in University of Leeds.

## LICENCE
Please see the standard Apache 2.0 open source LICENCE.
