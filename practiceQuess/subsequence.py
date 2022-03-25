def product(n):
    mul = 1
    while(n>0):
        rem = n%10
        mul = mul*rem
        n = n//10

    return mul

def printArrayList(arrL):
    arrL.pop(0)
    sum = 0
    for ele in arrL:
        sum = sum + product(int(ele))

    print(sum)

def getSequence(Str):

	# If string is empty
	if(len(Str) == 0):

		empty = []
		empty.append("")
		return empty

	ch = Str[0]

	subStr = Str[1:]

	subSequences = getSequence(subStr)

	res = []

	for val in subSequences:
		res.append(val)
		res.append(ch + val)

	return res


Str = "323"
printArrayList(getSequence(Str))