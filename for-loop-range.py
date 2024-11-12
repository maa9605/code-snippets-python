

	for i in range(1, len(flowerbed)-1): 
           if sum(flowerbed[i-1:i+2])==0 and n!=0:
              flowerbed[i] = 1
              n -= 1             
           
           if n == 0: 
              return True 
