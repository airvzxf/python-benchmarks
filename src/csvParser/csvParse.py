import csv
#~ from profilehooks import coverage
from profilehooks import timecall
#~ from profilehooks import profile
#~ from memory_profiler import profile

#~ @coverage
#~ @profile
@timecall
def travelDistance():
	totalDistance = 0

	fileId = open("travel.log")
	content = fileId.readlines()
	fileId.close()

	for entry in csv.reader(content):
		frequence,travelFrom,travelTo,distance = entry

		#print ("processed: %s->%s (%s km): %s times" % (travelFrom, travelTo, distance, frequence))
		totalDistance += int(distance) * int(frequence)

	print ("Travelling distance is %i km" % totalDistance)

if __name__ == '__main__':
	travelDistance()
