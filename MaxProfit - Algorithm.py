import numpy as np
capacity = 7
V = [2, 2, 4, 5, 3]
W = [3, 1, 3, 4, 2]

main_frame = np.zeros((len(V)+1,capacity+1),dtype = int)

# main_frame[0,2:] = range(1,capacity+1)

# main_frame[2:,0] = W

# print(main_frame)

for i in range(1,len(W)+1):
	w = W[i-1]
	v = V[i-1]

	for x in range(1,capacity + 1):
		
		best_pre = main_frame[i-1,x]
		option = main_frame[i-1,x-w]
		# print(w,best_pre,option)
		main_frame[i,x] = best_pre
		
		if x >= w and v + option > best_pre:
			main_frame[i,x] = v + option

print(main_frame)
final = []
x = capacity
for i in range(len(W),1,-1):
	w = W[i-1]
	v = V[i-1]

	

	option = main_frame[i-1,x-w]
	best_pre = main_frame[i-1,x]

	if main_frame[i,x] != best_pre:
		final.append((w,v))
		x = x+ (int(best_pre >= option) * (-w))
	
print(final)
# 		# if x < w:
# 		# 	pass
# 		# else:
# 		# 	if x >= (w + option):
# 		# 		print(w,option)
# 		# 		main_frame[i+1,x+1] = max(v + option,best_pre)
# 		# 	else: 
# 		# 		main_frame[i+1,x+1] = max(v,best_pre)











