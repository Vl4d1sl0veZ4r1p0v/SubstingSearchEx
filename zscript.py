query = 'abccdbccabcc'[::-1]
l, r = 0, 0
z_list = [0] * len(query)
for i in range(1, len(query)):
	if i <= r:
	    z_list[i] = min(r - i + 1, z_list[i - l])
	while i + z_list[i] < len(query) \
		and query[z_list[i]] == query[i + z_list[i]]:
	    z_list[i] += 1
	if i + z_list[i] - 1 > r:
	    l = i
	    r = i + z_list[i] - 1
print(z_list)
