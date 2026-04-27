'''
Given a string of '|' (walls) and '*' (items), and a list of query pairs [i, j],
for each query return the number of items ('*') between the NEAREST '|' boundaries
within the range [i, j].

Example:
s = "|**|*|"
queries = [[1,5], [1,6], [3,6]]
→ Output: [2, 3, 1]
Query [1,5]: between indices 1-5 → "|**|*" → 2 items in first closed section
Query [1,6]: all sections → 2 + 1 = 3
Query [3,6]: "|*|" → 1 item

'''
def platesBetweenCandles(s, queries):
    n = len(s)
    
    # Step 1: prefix sum of '*'
    prefix = [0] * n
    count = 0
    for i in range(n):
        if s[i] == '*':
            count += 1
        prefix[i] = count

    # Step 2: nearest left '|'
    left = [-1] * n
    last = -1
    for i in range(n):
        if s[i] == '|':
            last = i
        left[i] = last

    # Step 3: nearest right '|'
    right = [-1] * n
    last = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last = i
        right[i] = last

    # Step 4: answer queries
    result = []
    for l, r in queries:
        l -= 1
        r -= 1
        start = right[l]
        end = left[r]

        if start == -1 or end == -1 or start >= end:
            result.append(0)
        else:
            result.append(prefix[end] - prefix[start])

    return result
s = "|**|*|"
queries = [[1,5], [1,6], [3,6]]
print(platesBetweenCandles(s, queries))