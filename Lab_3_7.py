set1 = {1,7,1,4,'g','a','p','p',21,0,23,77,'s','y'}
set2 = {0,7,21,'a','s','q',0,'a'}

print(set1)
print(set2)
tpl1 = tuple(set1 & set2)
print(tpl1)
tpl2 = tuple(set1 - set2)
print(tpl2)
print(tpl1[:3])

for i in set2 :
    if str(i).isdigit() :
        print(i, end=' ')
print()
print(tpl1[-1::-1])
print(tpl2[-1::-1])
tlp_lst1 = list(tpl1)
tlp_lst2 = list(tpl2)
print(tlp_lst1)
print(tlp_lst2)