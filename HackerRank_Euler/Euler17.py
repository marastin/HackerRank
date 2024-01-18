numbers={0:"", 1:" One", 2:" Two",3:" Three", 4:" Four",5:" Five",6:" Six",7:" Seven", 8:" Eight",9:" Nine", 10:" Ten",11:" Eleven",12:" Twelve",13:" Thirteen",14:" Fourteen",15:" Fifteen",16:" Sixteen",17:" Seventeen",18:" Eighteen",19:" Nineteen", 20:" Twenty",30:" Thirty",40:" Forty",50:" Fifty",60:" Sixty",70:" Seventy",80:" Eighty",90:" Ninety"}

def convert(n):
    if n < 20:
        return numbers[n]
    elif n < 100:
        if n % 10 == 0:
            return numbers[n]
        else:
            return numbers[10 * (n // 10)] + convert(n % 10)
    elif n < 1000:
        return convert(n // 100) + " Hundred" + convert(n % 100)
    elif n < 1000000:
        return convert(n // 1000) + " Thousand" + convert(n % 1000)
    elif n < 1000000000:
        return convert(n // 1000000) + " Million" + convert(n % 1000000)
    else:
        return convert(n // 1000000000) + " Billion" + convert(n % 1000000000)
    

n = 1652
print(convert(n).strip())