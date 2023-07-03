a = "ZCZC-UXU-TFR-R18007ST_45-0910BR5-KIND3RWS-"
b = "ZCZC-WIR-TO{3018W0R+00T5-09UT115-K_EV/NWS-"
c = "ZCZC-WXRCTOR-0D_007+004OR_O1011E@KIND/N}S-"
d = ""

for x in range(len(a)):
    chars = [a[x], b[x], c[x]]
    uniq = list(set(chars))
    if len(uniq) == 1:
        d += uniq[0]
        continue
    if chars.count(uniq[0]) == 1:
        d += uniq[0]
    else:
        d += uniq[1]

print(d)

