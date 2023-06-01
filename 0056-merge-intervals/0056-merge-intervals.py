class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        # print(intervals)
        if len(intervals) <= 1:
            return intervals
        
        holder_arr = []
        curr_interval = [intervals[0][0]]
        curr_closer = intervals[0][1]
        
        for i in range(1, len(intervals)):
            print(intervals[i-1], intervals[i])
            curr_interval[0] = min(intervals[i][0],curr_interval[0])
            
            if intervals[i][0] > curr_closer:
                print("here", intervals[i][0],intervals[i-1][1])
                curr_closer = max(intervals[i-1][1], curr_closer)
                curr_interval.append(curr_closer)
                holder_arr.append(curr_interval)
                curr_interval = [intervals[i][0]]
                curr_closer = intervals[i][1]
            else:
                curr_closer = max(intervals[i][1], curr_closer)
                # max(i[1], curr_closer
        
        curr_interval.append(curr_closer)
        holder_arr.append(curr_interval) 
        return holder_arr
#         #Easy return if intervals length == 1:
        
#         holder_arr = [[1,18]]
#         curr_interval = [1]
#         closer = 18
#         curr_interval.append(closer)
#         input = [[1,3],[2,6],[5,10],[5,18]]
#                               i
#                            j  >  r
#         holder_arr = [[i-1,i][i-1,i],
        
#         overlap - True
#         new_arr = [[0,1][1,2][2,3]]
                      
                      
#               ##############        
#         Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

#         holder_arr = [[1,6],[8,10][15,18]]
                      
#         curr_interval = [15]
#         curr_closer = 18
#         for i in range(1, intervals)
#         [[1,3],[2,6],[8,10],[15,18]]

#                              i
#                 if i[0] grater than prev closer i-1[1]:
#                       curr_closer = 10 ...> i-1[1]
#                       curr_interval.append curr_closer
#                       holder_arr. append(curr_interval)
#                       curr_interval = [i[0]]
#                       curr_closer = i[1]
#                 else:
#                       curr_closer = i[1]
                     
#         curr_interval.append curr_closer
#         holder_arr. append(curr_interval)
                      
                      
#         ######
#         [[1,4],[4,5]]
#         holder_arr = []
#         curr_interval = [1]
#         curr_closer = [5]
                      
#         for i in range(1, intervals):
#                       if i[0] grater than prev closer i-1[1]:
#                       curr_closer = 10 ...> i-1[1]
#                       curr_interval.append curr_closer
#                       holder_arr. append(curr_interval)
#                       curr_interval = [i[0]]
#                       curr_closer = i[1]
#                 else:
#                       curr_closer = i[1]
                      
#         curr_interval.append curr_closer
#         holder_arr. append(curr_interval)
#                       return holdeer_arr


#         [[1,4][2,3][4,10]]
#     h   holder_arr = []
#         curr_interval = [1]
#         closer = 4
        
        
#         for i in range(1, intervals):
#                 curr_interval[0] = min([i[0]],curr_interval[0])
# #                       if i[0] grater than prev closer i-1[1]:
# #                       curr_closer = 10 ...> i-1[1]
# #                       curr_interval.append curr_closer
# #                       holder_arr. append(curr_interval)
# #                       curr_interval = [i[0]]
# #                       curr_closer = i[1]
# #                 else:
# #                       curr_closer = max(i[1], curr_closer
                   
        
        

###
                      
        