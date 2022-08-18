class Season:
    def __init__(self):
        self.data = ['봄', '여름', '가을', '겨울']
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            cur_season = self.data[self.index]
            self.index += 1
            return cur_season
        else:
            raise StopIteration
    

org_season = Season()

for i in org_season:
    print(i)
    
ir = iter(org_season)
print(next(ir))