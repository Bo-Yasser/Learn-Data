class Solution(object):
    def largestAltitude(self, gain):

        max_altitude = 0
        altitude = 0
        for i in range(len(gain)):
            altitude += gain[i]
            if altitude > max_altitude:
                max_altitude = altitude
            
        return max_altitude

b = Solution()    
gain = [-5,1,5,0,-7]
print(b.largestAltitude(gain))