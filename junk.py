decimal_ft = 10.26547842
print("Decimal Feet:", decimal_ft)
ft = int(decimal_ft)
print("Feet: (left of decimal) --> ",ft)
dec_inches = decimal_ft - ft
print("Decimal Inches: (right of decimal) -->", dec_inches)
print("Convert to 1/12ths... ")
incht = dec_inches / 0.08333
print("inches in 1/12ths:",incht)
inches = int(incht)
print("Inches: ---> ", inches)
inches_remainder = incht - inches
print("Inches Remainder:",inches_remainder)
print("Determine fraction...")
if inches_remainder < 0.15:
    frac = ""
elif inches_remainder >= 0.15 and inches_remainder < 0.35:
    frac = "1/4"
elif inches_remainder >= 0.35 and inches_remainder < 0.65:
    frac = "1/2"
elif inches_remainder >= 0.65 and inches_remainder < 0.85:
    frac = "3/4"
elif inches_remainder >= 0.85:
    frac = ""
    inches + 1

print("Fraction: --> ",frac)

print("Decimal Feet", decimal_ft, "  to ft/in -->  ", ft,inches,frac)

