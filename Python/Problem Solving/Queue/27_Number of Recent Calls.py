class RecentCounter(object):

    def __init__(self):
        self.times = []
        

    def ping(self, t):

        self.times.append(t)
        began = t - 3000
        count = 0
        for i in self.times:
            if i >= began:
                count += 1

        return count
            
        

class RecentCounter(object):

    def __init__(self):
        self.times = []
        

    def ping(self, t):

        self.times.append(t)

        while self.times[0] < t - 3000:
            self.times.pop(0)

        return len(self.times)
    
# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()

print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
