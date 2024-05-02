import math
def diff(r1,g1,b1,r2,g2,b2):
	d = math.sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)
	acc = (((int(d) - 0) * 100) / 461.7) + 0
	return round(acc,2)
