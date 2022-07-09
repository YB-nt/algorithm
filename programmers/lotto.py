def solution(lottos, win_nums):
    count =0
    zero_count =0
    # win_nums = list(set(win_nums)
    for num in lottos:
        if(num != 0 and num in win_nums):
            count+=1
        if(num==0):
            zero_count +=1
    
    lotto_best = 6-(zero_count+count)+1
    if(zero_count>=6):
        lotto_worst=6
    else:
        lotto_worst = (6-count)+1
    result = [lotto_best,lotto_worst]
            
        
    return result 


lottos1 =[44, 1, 0, 0, 31, 25]
win_nums1 = [31, 10, 45, 1, 6, 19]
lottos2 = [0, 0, 0, 0, 0, 0]
win_nums2 = [38, 19, 20, 40, 15, 25]
result1 = [3, 5]
result2= [1, 6]
lottos3 = [45, 4, 35, 20, 3, 9]
win_nums3 = [20, 9, 3, 45, 4, 35]
result3 = [1, 1]


print(solution(lottos1,win_nums1) == result1)
print(solution(lottos2,win_nums2) == result2)
print(solution(lottos3,win_nums3) == result3)

