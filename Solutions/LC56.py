#56. Merge Intervals

class Solution:
    def merge(self, intervals):
        
        intervals = sorted(intervals)
        current_Intervals = intervals[0]
        result = []

        for i in range(len(intervals)):

            if current_Intervals[1] >= intervals[i][0] and current_Intervals[0] <= intervals[i][1]:
                current_Intervals = [min(current_Intervals[0], intervals[i][0]), max(current_Intervals[1], intervals[i][1])]

            else:
                result.append(current_Intervals)
                current_Intervals = intervals[i]

            if i == len(intervals) - 1:
                result.append(current_Intervals)
        
        return result