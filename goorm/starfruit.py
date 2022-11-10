summer, days, nums, pay = map(int, input().split())
if summer % days == 0:
    mok = summer // days -1
else:
    mok = summer // days
print(mok*nums*pay)