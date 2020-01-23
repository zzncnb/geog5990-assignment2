#drunk class
import csv

#Open up the 'drunk.plan.txt' file to load the map.
tMap = []
f = open('drunk.plan.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
	rowlist=[]
	for value in row:
		rowlist.append(int(value))
	tMap.append(rowlist)
f.close()



# Assume that the starting point is at the center of the pub
def get_Start_Point():
	pubX = []
	pubY = []
	for x in range(0, len(tMap)):
		for y in range(0, len(tMap[x])):
			if tMap[x][y] == 1:
				pubX.append(x)
				pubY.append(y)
	pubX = list(set(pubX))
	pubY = list(set(pubY))

	return [pubX[int(len(pubX) / 2)], pubY[int(len(pubY)/2)]]


# Class for drunks.
class Drunk():
	startPoint = get_Start_Point()  # Class attribute: staring point's coordinate.

	townMap = tMap  # Class attribute: map.

# "self" represents object. If stores data inside an object, stores it inside self.
	def __init__(self, identifier):   # Initialize an object for drunk which is identifier.
		self.identifier = identifier  # Instance attribute: Drunk's Id: 10, 20, ...., 240, 250.
		self.passPoints = [self.startPoint]  # Pass points for a drunk.
		self.home = self.get_Home_Coordinate(self.identifier)  # The coordinates for drunk's home.

	def get_Identifier(self):
		return self.identifier

    # Get home's coordinate for drunks. Since drunk's home is a square which consists with lost of the point.
    # Assume the point with the shortest distance to srarting point as the home's corrdinate point for drunks.
	def get_Home_Coordinate(self, identifier):
		homePoints = []
		for x in range(0, len(self.townMap)):
			for y in range(0, len(self.townMap[x])):
				if self.townMap[x][y] == identifier:
					homePoints.append([x, y])

		minDistance = self.get_Distance_to_Start(homePoints[0])
		minDistancePoint = homePoints[0]

		for point in homePoints:
			if minDistance > self.get_Distance_to_Start(point):
				minDistance = self.get_Distance_to_Start(point)
				minDistancePoint = point

		return minDistancePoint


  # Get the straight distance from the starting point.
	def get_Distance_to_Start(self, point):
		return pow(pow(point[0] - self.startPoint[0],2)+pow(point[1] - self.startPoint[1], 2), 0.5)


  # Go back to the points where it pass through.
	def move(self):   
		for point in self.passPoints:   # Start point in passPoints. Begins with start points and use 'get_point_to' to get next point. Then use the same methods for next point.
			if self.get_Point_to(point)[1] != 1: #The rule for going back home is hitting the home. If the distance to home is not equal to 1, drunks will keep walking and append the points they pass through to passPoints.
				self.passPoints.append(self.get_Point_to(point)[0])
			elif self.get_Point_to(point)[1] == 1: # If distance equals to 1 means it's time to break and quit the for loop.Append the the points to passPoints.
				self.passPoints.append(self.get_Point_to(point)[0])
				break
		return self.passPoints   # return to all the points in passPoints.


	#Get the distance to drunk's home.
	def get_Distance_to_Home(self, point):
		return pow(pow(self.home[0] - point[0],2)+pow(self.home[1] - point[1], 2), 0.5)
		

	# The algortihm portion. It decides movvement directions for drunks.
	def get_Point_to(self,point):
		directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Drunk's possible walking direction.
		canGoPoints=[]
		for direction in directions:
			if (self.townMap[point[0] + direction[0]][point[1] + direction[1]] == 0 
				or self.townMap[point[0] + direction[0]][point[1] + direction[1]] == 1) and self.passPoints.count([point[0] + direction[0], point[1] + direction[1]]) == 0:
				canGoPoints.append([point[0] + direction[0], point[1] + direction[1]]) # Get the can go points for next movement that are 0 or 1. These points are not stored in passPoints.

		nextPoint = canGoPoints[0]  # Assume the closest point to drunk's home is the first point in canGopoints.
		minDistance = self.get_Distance_to_Home(nextPoint) # Calculates the distance from this point to drunk's home and assume this is the shortest distance to drunk's home.

		for point in canGoPoints:
			if minDistance > self.get_Distance_to_Home(point): # If there's a point that is closer to drunk's home than assumption.
				minDistance = self.get_Distance_to_Home(point) # Get the distance from that point to drunk's home for further comparison.
				nextPoint = point  # Switch to the point with shortest distance to drunk's home.
		return [nextPoint, minDistance] # Go back to the point with the shortest distance home which is the next point for drunk's next step.