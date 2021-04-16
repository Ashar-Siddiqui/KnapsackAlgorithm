rw = 15
objects = [1, 2, 3, 4, 5, 6, 7]
profits = [5, 10, 15, 7, 8, 9, 4]
weights = [1, 3, 5, 4, 1, 3, 2]

newprofit = []
pw = []

for i in range(len(profits)):
    pw.append(profits[i]/weights[i])

#pw.sort(reverse = True)

for i in range(len(pw)):
    indx = pw.index(max(pw))
    if rw >= weights[indx]:
        rw = rw - weights[indx]
        newprofit.append(profits[indx])
        pw.pop(indx)
        profits.pop(indx)
        weights.pop(indx)
        objects.pop(indx)
        
    elif weights[indx] > rw:
        newprofit.append( (rw/weights[indx]) * profits[indx])
        rw = rw - rw
        pw.pop(indx)
        profits.pop(indx)
        weights.pop(indx)
        objects.pop(indx)



print(sum(newprofit))


