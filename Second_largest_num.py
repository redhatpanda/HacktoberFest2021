lst=input("Enter a sentence:\n ").split()

len_list=[]
for i in lst:
    len_list.append(len(i))
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if len_list[j]>len_list[j+1]:
            t=len_list[j]
            len_list[j]=len_list[j+1]
            len_list[j+1]=t

            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
mx=max(len_list)
m=0
n=0
for i in len_list:
    if i<mx:
        m=i
        n=len_list.index(m)
print("The second largest word(s) is/are :\n")
for i in range(len(len_list)):
    if len_list[i]==m:
        print(lst[i])
