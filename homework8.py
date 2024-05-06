# Завдання 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

#Завдання 2
import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'  # регулярний вираз для пошуку дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total_profit = sum(func(text))
    return total_profit

# Завдання 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Invalid key. Please try again."
        except IndexError:
            return "Index out of range. Please try again."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return contacts[name]
