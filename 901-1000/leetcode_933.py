class RecentCounter:
    
    def __init__(self):
        self.times = []

    def ping(self, t: int):
        i = 0
        while i < len(self.times):
            if self.times[i] + 3000 < t:
                i += 1
            else:
                break
        self.times = self.times[i:]
        self.times.append(t)
        return len(self.times)            