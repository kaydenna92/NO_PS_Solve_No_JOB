def merge_sort(arr:list): 
    if len(arr) < 2: # 더이상 쪼갤 수 없으면 return
        return arr
    
    # 분할로직
    mid = len(arr) / 2
    low_arr = merge_sort(arr[:mid]) 
    high_arr = merge_sort(arr[mid:])

    # 병합로직
    merged_arr = [] # 병합 결과를 담을 리스트
    l = h = 0 
    while l < len(low_arr) and h < len(high_arr): 
        if low_arr[l] < high_arr[h]: # 대, 소 비교
            merged_arr.append(low_arr[l])  
            l += 1
        
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:] 
    merged_arr += high_arr[h:]

    return merged_arr