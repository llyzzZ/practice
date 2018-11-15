def dayUp(df):
    dayup = 1
    for i in range(365):
        if i%7 in (0, 6):
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
dayday = pow(1.01, 365)
while dayUp(dayfactor) < dayday:
    dayfactor += 0.01
print("工作日的力量：{:.3f}".format(dayfactor))