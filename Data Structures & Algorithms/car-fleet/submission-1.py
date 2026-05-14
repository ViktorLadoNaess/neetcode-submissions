class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        print(cars)
        fleet = 0
        slowest_time_ahead=0
        for ps, sp in cars:
            finish_time=(target-ps)/sp
            if finish_time>slowest_time_ahead:
                fleet+=1
                slowest_time_ahead = finish_time
        return fleet
            