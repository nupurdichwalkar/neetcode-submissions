class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills is None or len(bills) == 0:
            return True
        if bills[0] != 5:
            return False
        billCount = defaultdict(int)
        for bill in bills:
            billCount[bill] +=1
            remToReturn = bill - 5
            while remToReturn -10 >= 0 and billCount[10] > 0:
                billCount[10] -= 1
                remToReturn -= 10
            while remToReturn-5 >= 0 and billCount[5] > 0:
                billCount[5] -= 1
                remToReturn -= 5
            if remToReturn != 0:
                return False
            
        return True
#  billCount = 

# 5 - 1,
# 10 - 0,
# 20 - 1
# remToReturn = 0
