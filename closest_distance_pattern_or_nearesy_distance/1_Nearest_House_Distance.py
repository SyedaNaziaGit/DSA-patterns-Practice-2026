'''
Docstring for 1_Nearest_House_Distance
Consider the positive xaxis as straight road on which N houses are located, On a rainy day , M people are out on a walk, 
when the rain starts ,each person runs towards the nearest house to them.Sp=o that they donot get wet. 
You are given the position of each house, the width of eacg house and position of each person when the rain started, 
in seperate integer arrays. find and return an integer value representing the sum of distance travelled by all the people  
to reach the house nearest to them, 
input1= an integer value N, representing numbers of houses,
input2=an integer -position of each house, 
input3 =integer-width of each house on the road, 
input4=integervalue M,number of people on road, 
input5= an integer array- position of each person
Example:
input1 = 4
input2 = {8,15,2,12}
input3 = {2,3,3,1}
input4 = 5
input5 = {9,1,11,13,19}
output = 5
'''
def totalDistance(input1, input2, input3, input4, input5):
    N = input1 #number of houses
    house_positions = input2
    house_widths = input3
    M = input4 #num of people on road
    people_positions = input5
    
    total_distance = 0
    #creating house intervals-Each house forms an interval on the x-axis
    houses = []
    for i in range(N):
        left = house_positions[i]
        right = house_positions[i] + house_widths[i]
        houses = houses.append((left,right))
    #for each person -For every person, calculate the distance to each house interval.
    for person in people_positions:
        min_dist = float('inf')
        for left,right in houses:
            #If the person lies inside the interval, distance is zero
            if left <= person <= right:
                min_dist = 0
                break
            #compute the distance to the nearest boundary and take the minimum among all houses
            elif person < left:
                min_dist = min(min_dist, left-person)
            else:
                min_dist = min(min_dist,person-right)
        #sum these minimum distances for all people
        total_distance += min_dist
    return total_distance
#time complexity - O(m*n) - as for every person we check for each houses
