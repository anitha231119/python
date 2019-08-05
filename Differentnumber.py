def test_distinct(data):
if len(data)==len(set(data)):
   return true
else:
   return false
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))
