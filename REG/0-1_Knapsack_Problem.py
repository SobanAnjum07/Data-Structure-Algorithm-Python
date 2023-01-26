def KS(n, C, v, w):
	if n==0 or C <= 0:
		return 0, []
	if w[n-1] >= C:
		return KS(n-1, C, v, w)
	exKSv, exKSs = KS(n-1, C, v, w)
	inKSv, inKSs = KS(n-1, C-w[n-1], v, w)
	if exKSv >= inKSv + v[n-1]:
		return exKSv, inKSs
	else:
		inKSv = inKSv + v[n-1]
		inKSs.append(n)
		return inKSv, inKSs

def main():
    prices = [2, 3, 3, 4, 4, 5, 7, 8, 8]
    weights = [3, 5, 7, 4, 3, 9, 2, 11, 5]
    ov, os = KS(9, 15, prices, weights)
    print("Max benifit", ov)
    print("Optimal set", os)
    
main()

