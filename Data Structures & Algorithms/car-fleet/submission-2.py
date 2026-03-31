class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        d = {}

        for i in range(len(position)):
            d[position[i]] = speed[i]
        position.sort(reverse = True)
        print(position, d)
        time = []
        for i in range(len(position)):
            print(target, position[i], d[position[i]])
            t = (target - position[i]) / d[position[i]]
            time.append(t)
        
        print(time)


        s = [time[0]]
        for i in range(1, len(time)):
            if time[i] > s[-1]:
                s.append(time[i])

        return len(s)


        


        






        