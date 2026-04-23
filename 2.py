import random
import time

def getRandomDate(startdate, enddate):
    print("printing random date between", startdate, "and", enddate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endTime = time.mktime(time.strptime(enddate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("random date = ", getRandomDate("1/1/2016", "12/12/2018"))