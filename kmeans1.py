import csv
import random
import math
import operator

def loadDataset(filename,split, k, centroid=[], testSet=[]):
	with open(filename, 'rb') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		center = int(k)
		for x in range(len(dataset)-1):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])
			if random.random()< split and len(centroid) < center:
					centroid.append(dataset[x])
#			else :
			testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def main():
	centroid=[]
	testSet=[]
	distance = []
	split = 0.67
	k = raw_input("input amount centroid : ")
	loadDataset('iris.data',split, k,  centroid, testSet)

	print 'centroid set: ' + repr(len(centroid))
	print 'Test set: ' + repr(len(testSet))

	for y in range(len(testSet)):
		for x in range (len(centroid)):
			length = len(testSet[y])-1
			dist = euclideanDistance(centroid[x], testSet[y], length)
			distance.append((centroid[x], dist))
		distance.sort(key=operator.itemgetter(1))
		neighbors = []
		neighbors.append((testSet[y], distance))
	

	for y in range(len(testSet)):
			print distance[y]  


#	for y in range(len(testSet)):
#		print distance[y]

main()
