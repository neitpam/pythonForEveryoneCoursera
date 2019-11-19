hrs = input('Enter hours:')
rate = input('Enter rate:')

try:
    wh = float(hrs)
    oh = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
def computepay (wh, oh):
    if wh > 40 :
        reg = wh * oh
        otp = (wh - 40.0) * (oh * 0.5)
        xp = reg + otp
        return xp
    else:

        xp = wh * oh

xp = computepay(wh,oh)
print(xp)
