'''
Minimum Items to Remove
Given an array of item prices, find the minimum number of items to
remove so that the sum of any k items does NOT exceed a given threshold.
Note: If number of items < k, no removal needed.
Example: prices = [3, 2, 1, 4, 6, 5], k = 3, threshold = 14
The max sum of any 3 items = 6+5+4 = 15 > 14
Remove 6 → max sum = 5+4+3 = 12 ≤ 14 → Answer: 1 
'''
def minRemovals(prices, k, threshold):
    n = len(prices)#size of price array
    #edge case
    #if size of array is less than number of elements to check i.e, k
    if n < k:
        return 0
    #sorting prices in descending order
    prices.sort(reverse = True)
    removals = 0
    while n>= k:
        if sum(prices[:k]) <= threshold:
            return removals
        #remove largest element
        prices.pop(0)
        removals += 1
    return removals
prices = [3, 2, 1, 4, 6, 5]
k = 3
threshold = 14
print(minRemovals(prices,k,threshold))#op = 1