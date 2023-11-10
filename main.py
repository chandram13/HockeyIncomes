# Marvish Chandra

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def hockeySalary(salary, escrowRate,yearsContracted):
    findDiscount = salary * (escrowRate / 100)

    findSalary = (salary - findDiscount) * yearsContracted

    print(findSalary)

hockeySalary(400000,8.8,5)

