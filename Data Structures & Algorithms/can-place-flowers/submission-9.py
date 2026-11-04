class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) < 3:
            if 1 in flowerbed:
                if n < 1:
                    return True
                else:
                    return False
            else:
                if n < 2:
                    return True
                else:
                    return False


        for i in range(len(flowerbed)):
                if (i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                if (i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                if (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
        
        if n <= 0:
            return True
        else:
            return False

         
                    
            

            

        return can_plant