import random
from enum import Enum

class Advantage(Enum):
    none = 0
    advantage = 1
    disadvantage = 2

def rollDn(n):
    return int(random.random() * n + 1) 

def rollD20(advantage = Advantage.none):
    if (advantage == Advantage.none):
        return rollDn(20)
    elif (advantage == Advantage.advantage):
        return max(rollD20(), rollD20())
    elif (advantage == Advantage.disadvantage):
        return min(rollD20(), rollD20())

class Histogram():
    def __init__(self, buckets, cumulative = False):
        self.buckets = buckets
        self.counts = [0] * len(self.buckets)
        self.cumulative = cumulative
    
    def add(self, value):
        for (index, bucket) in enumerate(self.buckets):
            if (self.cumulative == False):
                if (value >= bucket):
                    if (index == len(self.buckets) - 1):
                        self.counts[index] += 1
                        return
                    elif (value < self.buckets[index + 1]):
                        self.counts[index] += 1
                        return
            else:
                if (value <= bucket):
                    self.counts[index] += 1

    def calcProportions(self):
        totalCounts = 0
        props = []
        if (self.cumulative):
            totalCounts = self.counts[-1]
        else:
            for (index, bucket) in enumerate(self.buckets): 
                totalCounts += self.counts[index]
        for count in self.counts:
            props.append(count / totalCounts)
        return props

    def printProportions(self):
        for (index, prop) in enumerate(self.calcProportions()): 
            print("{}: {}\n".format(self.buckets[index], prop))

    def printCounts(self):
        totalCounts = 0
        for (index, bucket) in enumerate(self.buckets): 
            totalCounts += self.counts[index]
            print("{}: {}\n".format(bucket, self.counts[index]))
        print("Total Counts: {}\n".format(totalCounts))