import math
def ex41():
	#The trigonometric functions cosine and sine of angle θ may be defined on the unit circle as follows: 
	#If (x, y) is a point on the unit circle, and if the ray from the origin (0, 0) to (x, y) makes an angle θ from the positive x-axis, 
	#(where counterclockwise turning is positive), then cosθ = x and sinθ = y

	p = [0.28366218546322625, -0.9589242746631385]
	print(f'For designated coordinates {p}')
	test = False
	for t in range(1,361):
		#  angle from 1 to 360
		trygfun = [(lambda t: math.cos(t))(t),(lambda t: math.sin(t))(t)]
		#two spaces after a period
		if round(p[0],2) == round(trygfun[0],2) and round(p[1],2) == round(trygfun[1],2):
			# True if coordinates of the designated point are in the set of values of trigonometric functions 
			test = True
	if test == True:
		print('a) p is in unit circle')
	else:
		print('a) p is not in unit circle')
			

	if (lambda a,b:a>0 and b>0)(p[0],p[1]) == True:
		print('b) coordinates of p are positive')
	else:
		print('b) coordinates of p are not positive')

	c = [(2,7),(-7,20),(5,30)]
	c.sort(key = lambda p: (-p[0], (p[1])))
	print('\n')
	print('c)',c)

	d = [(2,7),(-7,50),(5,30)]
	d.sort(key = lambda p: (math.fabs(p[0])+math.fabs(p[1])))
	print('d)',d)

def ex42():

	L = ['a1','b2','c3','d4','e5','f6','g7','h8','i9','j10']
	L_rev_req = []
	L_rev_iter = []
	begining = 2
	end = 7
	for num in range(len(L)):
		if num < begining:
			L_rev_iter.append(L[num])
		elif begining <= num <= end:
			L_rev_iter.append(L[end-num+begining])
		elif num > end:
			L_rev_iter.append(L[num])


	endpos = end
	pos = 0
	while pos < begining:
		L_rev_req.append(L[pos])
		pos=pos+1
	while begining <= pos <= end:
		L_rev_req.append(L[endpos])
		endpos=endpos-1
		pos=pos+1
	while len(L) > pos > end:
		L_rev_req.append(L[pos])
		pos=pos+1

	print(L)
	print(L_rev_iter)
	print(L_rev_req)

	if L_rev_req == L_rev_iter:
		print('Iterative and recursive versions are equale')


ex41()
print('\n\n_____________________________________________________________________________')
ex42()