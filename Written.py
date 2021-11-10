import util
test = util.Counter()

test[('A', 'Y')] = 5
print(test[('A', 'Y')])
test[('A', 'Y')] +=1 
print(test[('A', 'Y')])
test[('B', 'W')] += 1
print(test[('B', 'W')])
print(test[('C', 'Z')]) 
print(test)
print(test[['C', 'Z']])
