class Solution(object):
    def find_target_pairs(arr,target):
        i = 0 # First pointer
        j = len(arr)-1 # Second pointer
        arr.sort()
        print(arr)
        while(i < j):
            diff = target - arr[j]
            if(diff < 0): #Eliminating the elements in array that are higher than target
                print("Outer index is larger than the target")
                j -= 1
            elif(arr[i] == diff):
                print("[" + str(arr[j]) + " , " + str(arr[i]) + "]")
                if(arr[i+1] == diff): # Additional logic to handle duplicates in sorted array
                    print("[" + str(arr[j]) + " , " + str(arr[i+1]) + "]")
                j -= 1
            elif(arr[i] > diff):
                i += 1
                j -= 1
            elif(arr[i] < diff):
                i += 1
    
    arr = [3,7,9,4,8,2,6,11,14,16,12,3,12]
    target = 15
    
    find_target_pairs(arr,target)
