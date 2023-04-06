import random
import numpy as np
random.seed(772)
# N = random.randint(20,50) # Number of students
# k = random.randint(5,15) # Number of votes a student needs
# m = random.randint(5,15) # Number of roll calls that will be made by instructor

N=15
k=4
m=4

# This is the list of students who claim to be present(70)
curr_attend = []

# This is the actual list of students present(50)
actual_attend = []

def check(list,N,m,actual_attend):
    n = len(list)
    n2 = len(list)
    check_list = list.copy()
    for i in range(0,n2-m):
        idx = random.randint(0,n-1)
        # print("Remove ", idx, " From ", "\n", check_list)
        # try:

        # check_list.remove(idx)
        check_list.pop(idx)

        # except:
        #     print("================ERROR================")
        #     print("Remove ", idx, " From ", "\n", check_list)
        #     return
        n = n-1
    # Here check_list will have m students who the instructor plans to roll call
    
    fraud = []

    # Now the instructor will roll call these m students
    print("CHECKING ", check_list)
    print()
    print()
    print()
    for i in range(0,m):
        idx = check_list[i]
        if actual_attend[idx] == 0:
            # If the students have self voted but are not actually present, then they are frauds
            fraud.append(idx)

    return fraud

# Iterate over all the students
for i in range(0,N):

    # Randomly assign whether students will be present or absent
    # In the future we can set probability of students who are absent

    # This pres value is 1 if the student is actually present and 0 otherwise
    pres = random.randint(0,1)
    if(pres==1):
        actual_attend.append(1)
        curr_attend.append(1)
    else:
        # In the future we can set probability of students who will mark attendance falsely
        actual_attend.append(0)
        curr_attend.append(random.randint(0,1))
    
    
# This array is a 2d array which stores who each student voted for in a 0/1 format(Adjacency Matrix)
# In the future, adjacency list can also be implemented
voted_for = np.zeros((N,N))

# This is a 1d array which stores the number of votes that a student got
votes_cnt = np.zeros((N))

# This is a 1d array which stores 1 if the student self voted and 0 otherwise
self_vote = []
# For each student pair, randomly assign 1 if i voted for j and 0 otherwise
# We have assumed that each student will definitely vote for themselves
for  i in range(0,N):
    for j in range(0,N):
        if i == j:
            voted_for[i][j]=0
            if(actual_attend[i]==1):
                # Here we are assuming that every student will self vote
                # In the future we can include the probability of people who are actually present
                # but did not self vote
                self_vote.append(1)
            else:
                # Here too we can include probability of people who mark falsely
                self_vote.append(random.randint(0,1))
        else :
            voted_for[i][j]=random.randint(0,1)
        votes_cnt[j] += voted_for[i][j]

list1 = []
list2 = []

# In list 1 we  have people who have self voted and have more than k of their friends voting for them.
# In list 2 we have people who have self voted but did not have k votes.
for i in range(0,N):
    if votes_cnt[i] >= k and self_vote[i]==1:
        list1.append(i)
    elif self_vote[i]==1:
        list2.append(i)

# Returns the 
fraud = check(list1,N,m,actual_attend)
cnt = len(fraud)

# Key will have ids of students and values will represent the number of wrong votes that they cast
penalty_students=dict()
for i in range(N):
    penalty_students[i]=0

print("Entering List 1")
print("=====================INITIAL===================")
print(list1)
print(list2)
print("=====================INITIAL===================")
print()
print("=====================Self Vote===================")
print(self_vote)
print()
for i in range(cnt):
    idx = fraud[i]
    
    for j in range(0,N):
        # Finding all students who voted for this fraud student
        if voted_for[j][idx]==1:
            penalty_students[j]+=1

        # Reducing the vote count of those students that this fraud student voted for
        if voted_for[idx][j] == 1:
            votes_cnt[j] = votes_cnt[j]-1

            # If the student j gets his vote count reduced to less than k then push him to list 2
            if j in list1 and votes_cnt[j] < k:
                list2.append(j)
                list1.remove(j)
    print(list1)
    print(list2)

# The instructor will necessarily call out all students from list 2
l=len(list2)
for i in range(0,l):
    idx = list2[i]
    if actual_attend[idx] == 1:
        continue
    
    for j in range(0,N):
        # Finding all students who voted for this fraud student
        if voted_for[j][idx]==1:
            penalty_students[j]+=1

        # Reducing the vote count of those students that this fraud student voted for
        if voted_for[idx][j] == 1:
            votes_cnt[j] = votes_cnt[j]-1

            # If the student j gets his vote count reduced to less than k then push him to list 2
            if j in list1 and votes_cnt[j] < k:
                list2.append(j)
                list1.remove(j)
                l+=1
    print(list1)
    print(list2)
for i in range(N):
    print(i,end="\t")
print()
print()
print()
print("Actual Attendance")
for i in range(N):
    print(actual_attend[i], end="\t")

print()
print()
print()
print("Current Attendance")
for i in range(N):
    print(curr_attend[i], end="\t")
print()
print()
print()
print("Frauds")
for i in range(len(fraud)):
    print(fraud[i], end="\t")
print()
print()
print()
print("Penalty")
print(penalty_students)
print()
print()
print()
print("Voted For")
print(voted_for)

# The instructor will necessarily call out all students from list 2
# for i in range(0,len(list2)):
# i=0
# while len(list2)>0:
#     idx = list2[i]
#     if actual_attend[idx] == 1:
#         continue
    
#     for j in range(0,N):
#         # Finding all students who voted for this fraud student
#         if voted_for[j][idx]==1:
#             penalty_students[j]+=1

#         # Reducing the vote count of those students that this fraud student voted for
#         if voted_for[idx][j] == 1:
#             votes_cnt[j] = votes_cnt[j]-1

#             # If the student j gets his vote count reduced to less than k then push him to list 2
#             if j in list1 and votes_cnt[j] < k:
#                 list2.append(j)
#                 list1.remove(j)

