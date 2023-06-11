# 병합 정렬 Logic
# 두 부분배열을 합친 크기와 같은 배열을 새로 만들기
# 두 부분배열의 맨 앞 요소끼리 비교하여 더 작은 값을 새로만든 배열에 넣기
# 값이 빠진 배열의 다음 비교대상은 다음 값이다.
# 두 부분배열 중 한 부분 배열의 값이 전부 빠지면, 새로운 배열에 남은 부분배열값을 붙인다.

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


# 최적화 
# 병합 결과를 담을 새로운 배열을 매번 생성하여 return하지 않고,
# 인덱스 접근을 이용해 입력 배열을 계속 업데이트하면 메모리 사용량을 줄일 수 있다.
# in-place sort

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))