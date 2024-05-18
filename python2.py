import random as r
import itertools
import time

""" Функции для упрощенной версии """

def generate_combinations(employees, exhibitions): # Алгоритмическая функция
    if exhibitions == 0:
        return [[]] if employees == 0 else []
    if employees == 0:
        return [[0] * exhibitions] if employees == 0 else []

    combinations = []
    for i in range(employees + 1):
        for combination in generate_combinations(employees - i, exhibitions - 1):
            combinations.append([i] + combination)
    return combinations

def itertools_combinations(employees, exhibitions): # С помощью функций Питона
    all_combinations = itertools.product(range(employees + 1), repeat=exhibitions)
    valid_combinations = [[*comb] for comb in all_combinations if sum(comb) == employees]
    return valid_combinations

def print_combinations(combinations):
    for i, combination in enumerate(combinations, start=1):
        padded_combination = combination + [0] * (T - len(combination))
        print(f"Вариант {i}: {padded_combination}")

""" Функции для усложненной версии """

def employees(x):
    global employee, employee_parameters
    cntplayers = 1
    string = ''

    for _ in range(x):
        employee.append(f'{r.choice("МЖ")}{cntplayers}')
        cntplayers += 1

    for j in employee:
        employee_parameters[j] = r.randint(0, 100)

    for i in employee_parameters.items():
        a, b = i
        string = f'{string}, {a} {b}'

    print('\nСотрудники:')
    print(string[2::])

def itertools_combinations_hard(employees, exhibitions):
    all_combinations = itertools.product(range(2), repeat=len(employees) * exhibitions)
    valid_combinations = []

    for comb in all_combinations:
        comb_matrix = [comb[i*len(employees):(i+1)*len(employees)] for i in range(exhibitions)]
        comb_matrix = [[employees[j] if comb_matrix[i][j] == 1 else None for j in range(len(employees))] for i in range(exhibitions)]
        
        # Ensure each employee is assigned to at most one exhibition
        flat_comb = [emp for sublist in comb_matrix for emp in sublist]
        if all(flat_comb.count(emp) <= 1 for emp in employees):
            valid_combinations.append(comb_matrix)
    
    filtered_combinations = []
    for comb in valid_combinations:
        filtered_comb = [[emp for emp in ex if emp is not None] for ex in comb]
        filtered_combinations.append(filtered_comb)
    
    return filtered_combinations

def print_hard_combinations(combinations):
    for i, combination in enumerate(combinations, start=1):
        print(f"Вариант {i}:")
        for j, exhibition in enumerate(combination, start=1):
            present_employees = [emp for emp in exhibition if emp != 0]
            print(f"  Выставка {j}: {present_employees if present_employees else 'никто'}")    
    

employee = []
employee_parameters = {}

K = int(input("Введите количество сотрудников: "))
T = int(input("Введите количество выставок: "))

a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
if a == 0:
    start1_time = time.time()
    combinations = generate_combinations(K, T)
    print_combinations(combinations)
    end1_time = time.time()
    
    start2_time = time.time()
    combinations_itertools = itertools_combinations(K, T)
    print_combinations(combinations_itertools)
    end2_time = time.time()

    print(f"Время выполнения алгоритмического метода: {end1_time - start1_time:.5f} сек")
    print(f"Время выполнения метода itertools: {end2_time - start2_time:.5f} сек")

    print(f"Разница по времени их выполнения: {abs((end1_time - start1_time) - (end2_time - start2_time)):.5f}")
if a == 1:
    print('\nДополнительным условием будет ограничение по рейтингу.\nСотрудники с рейтингом ниже 50 не будут допущены')
    employees(K)
    y = 0
    for i, n in enumerate(employee_parameters.items()):
        a, b = n
        if int(b) < 50:
            i -= y
            y += 1
            employee.pop(i)
    print(employee)
    ich = itertools_combinations_hard(employee, T)
    print_hard_combinations(ich)