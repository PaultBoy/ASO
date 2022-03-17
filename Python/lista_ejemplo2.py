lst=[]
#[1,6,11,16,21,26...,96]
for item in range(0,101,5):
    if item % 10 == 0:
        lst.append(item)
print(lst)