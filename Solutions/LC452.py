class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(reverse = True)

        count = 1
        currX = points[0][0]

        for x, y in points:
            if y < currX:
                currX = x
                count += 1
                
        return count