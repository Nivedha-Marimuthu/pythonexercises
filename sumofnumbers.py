import lst as lst
import array as arr


def getSum(a):

    sum = 0
    for i in str(a):
        sum += int(i)
    return sum

a=8663
print(getSum(a))
