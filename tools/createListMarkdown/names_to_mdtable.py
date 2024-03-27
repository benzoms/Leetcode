names = '''
Valid Palindrome	
Two Sum II Input Array Is Sorted	
3Sum	
Container With Most Water	
Trapping Rain Water
'''
diffs = '''
Easy
Medium
Medium
Medium
Hard
'''
names = names.strip().split('\n')
diffs = diffs.strip().split('\n')

prefix = '''
| Status | Problem | Difficulty |
| --- | --- | --- |
'''

print(prefix,end='')
for index, prob in enumerate(names):
    temp = f'| **X** | {prob.strip()} | {diffs[index]} |'
    print(temp)
