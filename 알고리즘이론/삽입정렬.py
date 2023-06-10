arr = [2, 1, 3, 5, 4]


def insertion_sort(arr:list):
    for end in range(1, len(arr)): # 1 / 2 / 3 / 4 
        for i in range(end, 0, -1): # 1, / 2, 1 / 3, 2, 1 / 4, 3, 2, 1
            if arr[i - 1] > arr[i]:  
                arr[i - 1], arr[i] = arr[i], arr[i - 1] # swap 
    return arr


# 이전 단계에서 모두 정렬되었다는 점을 활용하면, 불필요한 비교작업을 제거할 수 있음. 
# [1, 2, 3, 5] 에 4가 추가된다면, 5는 4보다 크기때문에 swap이 필요하지만 3은 4보다 작기때문에 swap이 필요없다
# 그리고 3보다 앞에 있는 숫자들은 이전 단계에서 모두 정렬해놓았기 때문에 당연히 3보다 작고, 4와 비교하는 것은 무의미하다.
# 따라서 새롭게 추가된 값보다 작은 값들을 만나는 순간까지만, 내부 반복문을 수행하면 좋다.
# O(N) 의 시간복잡도를 달성하는 코드
def insertion_sort(arr:list):
    for end in range(1, len(arr)): 
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1] # swap 
            i -= 1

    return arr


# swap 작업 X 코드
def insertion_sort(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end] # 삽입할 element
        i = end 
        while i > 0 and arr[i - 1] > to_insert: # 앞의 값이 삽입할 값보다 클 경우, 앞의 값을 뒤로 밀다가 최초로 작은 값을 만나는 순간, 그 뒤에 삽입할 값을 삽입하기!
            arr[i] = arr[i - 1] # 뒤로 밀기
            i -= 1
        arr[i] = to_insert 


insertion_sort(arr)
print(arr)