"""
실패 코드 모음.
"""
#1
report = list(set(report))
answer = []
user= dict()
report_history = dict()

for id in id_list:
    user[id]= 0

for i in report:
    temp =[]
    a,b = i.split()
    
    if(a==b):
        continue
    user[b]+=1
    if(a in report_history.keys()):
        temp.append(report_history[a])
        temp.append(b)
        report_history[a] = temp
    else:
        report_history[a]=b

for id in id_list:
    result = 0
    print(id)
    if(isinstance(user[id], list)):
        for u in user[id]:
            if(u>=k):
                if(id in report_history[id]):
                    result+=1
                    print("result")
    else:
        print()
        print(user[id])
    answer.append(result)

"""
처음에는 이러한 방식으로 리스트를 사용해서 문제를 풀려고 하였으나, 
신고자에게 사후보고?count 를 해주는 방법에서 생각이 나지 않아서 다른 방법을 찾아봄
"""

#2
report = list(set(report))
answer = []
user= dict()

for id in id_list:
    user[id]= 0

dic_report = {id: [] for id in id_list}


for i in report:
    a,b = i.split()
    if(a==b):
        continue
    user[b]+=1
    dic_report[a].append(b)

# print("report:", dic_report)
# print("user:",user)
for key,value in user.items():
    if(value>=k):
        for r_key,r_value in dic_report.items():
            if(key in r_value):
                
                
"""
report를 딕셔너리를 이용해서 count를 관리 하게 되면 편리하게 된다라고 체감하게됨,
딕셔너리 탐색과정에서 삐끗하였다..ㅎ
"""
