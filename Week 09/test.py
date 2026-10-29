import pdb

def calculate(a, b):
    result = a + b
    return result

x = 100
y = "20"

pdb.set_trace()

answer = calculate(x, y)

print("Answer:", answer)