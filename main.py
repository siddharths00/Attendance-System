import random
random.seed(772)
N = random.randint(20,50)
k = random.randint(5,15)
m = random.randint(5,15)

curr_attend = []
actual_attend = []

def check(list,N,m,actual_attend):
    n = len(list)
    nn = len(list)
    check_list = list.copy()
    for i in range(0,nn-m):
        idx = random.randint(0,n)
        check_list.remove(list[idx])
        n = n-1

    fraud = []

    for i in range(0,m):
        idx = check_list[i]
        if actual_attend[idx] == 0:
            fraud.append(idx)
    return fraud

for i in range(0,N):
    curr_attend.append(random.randint(0,1))
    actual_attend.append(random.randint(0,1))

voted_for = []
votes_cnt = []
for  i in range(0,N):
    for j in range(0,N):
        if i == j:
            voted_for[i].append(1)
        else :
            voted_for[i].append(random.randint(0,1))
        votes_cnt[j] += voted_for[i][j]

list1 = []
list2 = []

for i in range(0,N):
    if votes_cnt[i] >= k:
        list1.append(i)
    elif curr_attend[i] == 1:
        list2.append(i)

fraud = check(list1,N,m,actual_attend)
cnt = len(fraud)
if cnt > 0:
    for i in range(0,cnt):
        idx = fraud[i]
        for j in range(0,N):
            if voted_for[idx][j] == 1:
                votes_cnt[j] = votes_cnt[j]-1
                if j in list1 and votes_cnt[j] < k:
                    list2.append(j)
                    list1.remove(j)
#check list now
for i in range(0,len(list2)):
    idx = list2[i]
    if actual_attend[idx] == 1:
        continue
    for j in range(0,N):
            if voted_for[idx][j] == 1:
                votes_cnt[j] = votes_cnt[j]-1
                if j in list1 and votes_cnt[j] < k:
                    list2.append(j)
                    list1.remove(j)
