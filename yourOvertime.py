hrs = input('Enter hours:')
rate = input('Enter rate:')

try:
    wh = float(hrs)
    oh = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if wh > 40 :
    reg = wh * oh
    otp = (wh - 40.0) * (oh * 0.5)
    xp = reg + otp
else:

    xp = wh * oh

print("Pay:",xp)
