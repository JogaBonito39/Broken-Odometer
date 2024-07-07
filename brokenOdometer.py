#find distance traveled using velocity and time 
#distance = velocity * time
#speed interval just requires your speed at each interval you take it in
#example record speed for every 5 seconds, if you want a more accurate reading make the intervals shorter

class Odometer:
    def __init__(self, speed_list=[], time_list=[], time=0):
        self.speed_list = speed_list
        self.time_list = time_list
        self.time = time 
        delta_x = round(self.time_list[-1] - self.time_list[0])/ len(self.time_list)
        if delta_x == self.time and self.time > 0:
            delta_x = delta_x
        else:
            delta_x = self.time
        
        #print(f"{delta_x=}")
        
        left_sum = 0
        right_sum = 0
        itr = 0
        
        while itr <= len(self.speed_list)-2:
            #print('l', self.speed_list[itr])
            left_sum += self.speed_list[itr] * delta_x
            itr += 1
            
        itr = 1        
        while itr <= len(self.speed_list)-1:
            #print('r', self.speed_list[itr])
            right_sum += self.speed_list[itr] * delta_x
            itr += 1

        print(f"{left_sum} <= distance traveled in ft<= {right_sum}")
       
if __name__ == "__main__":
    
    print("record your speed in m/h in for every second interval of your choice")
    speed_list = []
    speed_list_str = None
    time = None
    while True:
        speed_list_str = input("enter your speeds seperate by spaces (type 'HELP' if needed): ")
        if speed_list_str == 'HELP':
            print("example speed list: 15 49 22 34")
        else:
            for speed in speed_list_str.split():
                #converting m/h to ft/s in order to have the time and the velocity in consistent units
                speed_list.append(round((int(speed)*5280)/3600))
            break
    while True:    
        time = input("enter your interval in seconds (s) of choice (type 'HELP' if needed): ")
        if time == 'HELP':
            print("example time inteval is 5: [5, 10, 15, 20, ...]")
        else:
            time = int(time)
            break
            
    time_list = []
    for i in range(0, len(speed_list)+1):
        time_list.append(time * i)
        
    print(f"speed array {speed_list}")
    print(f"time array {time_list}")
    
    Od = Odometer(speed_list, time_list, time)
