def solution(id_list, report, k):
    # report 중복 제거    
    report = list(set(report))
    # answer index 사용하기 위해서
    answer = [0 for x in id_list]
    # 신고 횟수 딕셔너리
    user= dict()
    # 신고횟수 초기화
    for id in id_list:
        user[id]= 0
    # 신고내용을 list로 받을것임
    dic_report = {id: [] for id in id_list}
  
  
    for i in report:
        #신고내용 분리
        a,b = i.split()
        # 자기자신 신고 불가능
        if(a==b):
            continue
        #신고 count
        user[b]+=1
        #신고내용 저장
        dic_report[a].append(b)
    """
    # report: {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
    # user: {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    # 이러한 방식으로 저장 되는데 report를 순차적으로 탐색하면서 value값을 검사해준다.
    # 신고 내용에 해당 되는 사용자가 신고 빈도수가 일정수치 이상 넘어가면 
    # 신고자에게 메일 발송 count
    """
    for cnt,value in enumerate(dic_report.values()):
        for v in value:
            if(user[v]>=k):
                answer[cnt]+=1

    return answer
