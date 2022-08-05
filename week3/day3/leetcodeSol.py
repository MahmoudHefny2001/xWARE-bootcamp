salary = [4000,3000,1000,2000]
def average(list[]) -> float:
        sum = 0
        minimum = salary[0]
        maximum = salary[0]
        for i in salary:
            if(minimum > i):
                minimum = i
        for i in salary:
            if(maximum < i ):
                maximum = i

        for i in salary :
            sum += i

        avg = float((minimum + maximum + sum ) / len(salary))
        print(avg)

average(salary)
