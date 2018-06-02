d={2:74,4:56,7:23}

largest=[(k,v) for v,k in d.items()]
print largest
print max(largest)[0]


sorting_key=sorted(d.items(),key=lambda x:x[0])
print sorting_key


sorting_value=sorted(d.items(),key=lambda x:x[1])
print sorting_value


