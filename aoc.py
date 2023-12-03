#!/usr/bin/python3
"""Display all days."""
from importlib import import_module

if __name__ == '__main__':
    for day in range(1, 26):
        try:
            solutions = import_module(str(day), '.')

            assert solutions.DEBUG == 0

            print(f'------ DAY {day} ------') 
            print('--- Part 1 ---')
            print(solutions.part_1())
            print('\n--- Part 2 ---')
            print(solutions.part_2())
            print()
        except ModuleNotFoundError:
            pass
