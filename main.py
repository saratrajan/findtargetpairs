class Solution(object):
    def find_target_pairs(arr,target):
        i = 0
        j = len(arr)-1
        arr.sort()
        print(arr)
        while(i < j):
            diff = target - arr[j]
            if(diff < 0):
                print("Outer index is larger than the target")
                j -= 1
            elif(arr[i] == diff):
                print("[" + str(arr[j]) + " , " + str(arr[i]) + "]")
                j -= 1
            elif(arr[i] > diff):
                i += 1
                j -= 1
            elif(arr[i] < diff):
                i += 1
    
    arr = [3,7,9,4,8,2,6,11,14,16,12]
    target = 15
    
    find_target_pairs(arr,target)
