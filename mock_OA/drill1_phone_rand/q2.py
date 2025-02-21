class UndergroundSystem:

    # (1042-1112am) 30mins ovpn
    # (2/21/25)(1116-1126am)(Fri) done
    
    def __init__(self):
        self.checkin_data = {} # {id: (stationName, time)}
        self.travel_times = defaultdict(list) # {(startstation, endstation): [total_time, count]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_data[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation, starttime = self.checkin_data.pop(id)
        travel_time = t - starttime
        
        # if no key, initialize it
        if (startstation, stationName) not in self.travel_times:
            self.travel_times[(startstation, stationName)] = [0, 0]
            
        # update total travel time and count
        self.travel_times[(startstation, stationName)][0] += travel_time
        self.travel_times[(startstation, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count

    
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)