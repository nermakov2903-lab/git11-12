import random

def generate_array(n=10, a=0, b=100):
    return [random.randint(a, b) for _ in range(n)]
