/*
``python``
class Solution:
    
    def average(self, salary: List[int]) -> float:
       sum = 0
       minimum = salary[0]
       maximum = salary[len(salary)]
       for i in salary:
            if(minimum > i):
                minimum = i
       for i in salary:
            if(maximum < i ):
                maximum = i
                
       for i in salary :
            sum += i
        
       avg = ((minimum + maximum + sum ) / len(salary))
       return avg
*/
TO be Edited
