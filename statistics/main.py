import stats

my_list = [1, 0, 23, 44, 65, 867, 12, -45, 23 ,23 ,655, 402, -1, -10, 2323, 44, 10072, -9876, 459, -459, 459, 459, -900, 17, 19, 101, 3]
stat_calc = stats.Statistics()
print(my_list)
print('Sorted List:', stat_calc.sort_list(my_list))
print('Minimum:', stat_calc.min(my_list))
print('Maximum:', stat_calc.max(my_list))
print('Mean:', stat_calc._mean(my_list))
print('Mean Deviation:', stat_calc.mean_deviation(my_list))
print('Median:', stat_calc.median(my_list))
print('Variance:', stat_calc.variance(my_list))
print('Standard Deviation:', stat_calc.stdv(my_list))
print('Nr. of occurences:', stat_calc.count(n=459, numbers=my_list))
print('Sum of items:', stat_calc.sum(my_list))
print('Prime numbers:', stat_calc.prime(my_list))
print('Range:', stat_calc.range(my_list))
print('Length:', stat_calc.length(my_list))