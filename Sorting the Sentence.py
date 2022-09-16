class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split(" ")
        final=""
        for i in range(len(arr)):
            min=i
            for j in range(i+1, len(arr)):
                if arr[j][-1]<arr[min][-1]:
                    min=j
            arr[i], arr[min]= arr[min], arr[i]
            
            final+=arr[i][:-1] + " "
    
        return final[:-1]
                