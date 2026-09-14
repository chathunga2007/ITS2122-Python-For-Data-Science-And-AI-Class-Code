def normalize_scores(*args ,scaling_factor=1.0):
    return[arg * scaling_factor for arg in args]

print(normalize_scores(10, 20, 30))
print("--------------------------")
print(normalize_scores(10, 20, 30, scaling_factor=2.0))