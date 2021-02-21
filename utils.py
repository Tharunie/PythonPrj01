def find_max(numberlist):
    maxi = numberlist[0]
    for number in numberlist:
        if maxi < number:
            maxi = number
    else:
        return maxi


