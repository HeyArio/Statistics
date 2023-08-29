import numpy as np

class Statistics:

    def __init__(self):
        pass

    @staticmethod
    def sort_list(numbers):
        return sorted(numbers)

    @staticmethod
    def min(numbers):
        mini = float('inf')
        for i in numbers:
            if i <= mini:
                mini = i
        return mini
    
    @staticmethod
    def max(numbers):
        maxi = float('-inf')
        for i in numbers:
            if i >= maxi:
                maxi = i
        return maxi
    
    @classmethod
    def _mean(cls, numbers):

        return round(cls.sum(numbers)/len(numbers))
    
    @classmethod
    def mean_deviation(cls, numbers):
        res = 0
        for i in numbers:
            res = i - cls._mean(numbers) + res
        return round(res/len(numbers), 2)
    
    @staticmethod
    def median(numbers):
        numbers_list= sorted(numbers)
        if len(numbers)%2 != 0:
            return numbers_list[len(numbers)//2]
        else:
            mid = (numbers_list[len(numbers)//2 - 1] + numbers_list[len(numbers)//2])/2
            return mid
        

    @classmethod
    def variance(cls, numbers):
        res = 0
        for i in numbers:
            res = res + (i - cls._mean(numbers)) ** 2

        return round(res/len(numbers), 2)
    
    @classmethod
    def stdv(cls, numbers):
        return round((cls.variance(numbers)) ** (1/2), 2)
    
    @staticmethod
    def sum(numbers):
        res = 0
        for i in numbers:
            res += i
        return res
    
    @staticmethod
    def _prime(n):
        count = 0
        for i in range(2, n//2 + 1):
            if n%i==0:
                count += 1
        if count >= 1:
            return False
        else:
            return True

    @classmethod
    def prime(cls, numbers):
        res = []
        for i in numbers:
            if cls._prime(i) and i!=1 and i!=2 and i>0:
                res.append(i)
        return np.unique(sorted(res))
    
    @classmethod
    def range(cls, numbers):
        return cls.max(numbers) - cls.min(numbers)
    
    @staticmethod
    def length(numbers):
        j = 0
        for i in numbers:
            j += 1
        return j
    
    @staticmethod
    def count(n, numbers):
        c = 0
        if n in numbers:
            for i in numbers:
                if i == n:
                    c += 1
            return c
        
        else:
            print(f'Sorry {n} is not currently in our list.')
    