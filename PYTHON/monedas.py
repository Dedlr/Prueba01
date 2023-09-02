def calculateCoins(n):

    coins = [50, 20, 10, 5, 2, 1]  
    count = []  

    for coin in coins:
        num = n // coin
        count.append(num)
        n -= num * coin

    return count


print('51 ---> ',calculateCoins(51))
print('3 --->  ',calculateCoins(3))   
print('5 --->  ',calculateCoins(5))   
print('16 ---> ',calculateCoins(16))  
print('100 --->',calculateCoins(100)) 