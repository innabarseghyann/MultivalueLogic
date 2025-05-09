#Fullness theorem 1

def j(i, x, k):
    return (k - 1) if x == i else 0


def fullness_1(*args, k, base_function, level):
    index = len(args) - level - 1
    x_next = args[index]

    indent = "  " * level  # For cleaner visual indentation in output

    if level == len(args) - 1:
        print(f"{indent}Base case at level {level}, args = {args}")
        result = base_function(args)
        print(f"{indent}→ base_fn({args}) = {result}")
        return result
    else:
        print(f"{indent}Level {level}, evaluating index {index}, x_next = {x_next}")
        results = []
        for i in range(k):
            new_args = list(args)
            new_args[index] = i
            print(f"{indent}  Trying i = {i} at index {index} → new_args = {new_args}")
            rec_val = fullness_1(*new_args, k=k, base_function=base_function, level=level + 1)
            score = min_2(j(i, x_next, k), rec_val, k)
            print(f"{indent}  j({i}, {x_next}, {k}) = {j(i, x_next, k)}, rec_val = {rec_val}, min = {score}")
            results.append(score)
        final = max(results)
        print(f"{indent}→ Level {level} max = {final}")
        return final


#Fullness theorem 2

def rolling_mod_max(x, k):
    return max((x + i) % k for i in range(k))

def j_2(x, i, k):
    skip_alpha = k - 1 - i
    return (1 + max((x + alpha) % k for alpha in range(k) if alpha != skip_alpha))%k

def f(s, i, x, k):
    return (s + 1 + max(j(i, x, k), k - 1 - s))%3

def opposite(x, k):
    return max(f(k - 1 - i, i, x, k) for i in range(k))

def min_2(x, y, k):
    return opposite(max(opposite(x, k), opposite(y, k)), k)

def fullness_2(*args, k, base_function, level):
    index = len(args) - level - 1
    x_next = args[index]

    indent = "  " * level  # For cleaner visual indentation in output

    if level == len(args) - 1:
        print(f"{indent}Base case at level {level}, args = {args}")
        result = base_function(args)
        print(f"{indent}→ base_fn({args}) = {result}")
        return result
    else:
        print(f"{indent}Level {level}, evaluating index {index}, x_next = {x_next}")
        results = []
        for i in range(k):
            new_args = list(args)
            new_args[index] = i
            print(f"{indent}  Trying i = {i} at index {index} → new_args = {new_args}")
            rec_val = fullness_2(*new_args, k=k, base_function=base_function, level=level + 1)
            score = min_2(j_2(x_next, i, k), rec_val, k)
            print(f"{indent}  j({i}, {x_next}, {k}) = {j_2(x_next, i, k)}, rec_val = {rec_val}, min = {score}")
            results.append(score)
        final = max(results)
        print(f"{indent}→ Level {level} max = {final}")
        return final


#First Sheffer's function fullness

def sheffer(x, y, k):
    return (max(x % k, y % k) + 1) % k

def max_for_sheffer(x, y, k):
    # Start with the initial value
    res = sheffer(x, y, k)

    # Apply sheffer to the result k times
    for _ in range(k - 1):  # Do this for k-1 times since the first is already applied
        res = sheffer(res, res, k)

    return res

def increment(x, k):
    return sheffer(x, x, k)

def add(x, y, k):
    res = x
    for _ in range(y):  # Increment x by 1, y times
        res = increment(res, k)
    return res


def rolling_mod_max_for_sheffer(x, k):
    return max(add(x, i, k)  for i in range(k))

def j_for_sheffer(x, i, k):
    skip_alpha = k - 1 - i
    return (1 + max(add(x, alpha, k) % k for alpha in range(k) if alpha != skip_alpha))%k

def f_for_sheffer(s, i, x, k):
    return add(increment(s, k), max(j(i, x, k), k - 1 - s), k)%k

def opposite_for_sheffer(x, k):
    return max(f_for_sheffer(k - 1 - i, i, x, k) for i in range(k - 1))

def min_for_sheffer(x, y, k):
    return opposite_for_sheffer(max_for_sheffer(opposite_for_sheffer(x, k), opposite_for_sheffer(y, k), k), k)

def sheffer_fullness(*args, k, base_function, level):
    index = len(args) - level - 1
    x_next = args[index]

    indent = "  " * level  # For cleaner visual indentation in output

    if level == len(args) - 1:
        print(f"{indent}Base case at level {level}, args = {args}")
        result = base_function(args)
        print(f"{indent}→ base_fn({args}) = {result}")
        return result
    else:
        print(f"{indent}Level {level}, evaluating index {index}, x_next = {x_next}")
        results = []
        for i in range(k):
            new_args = list(args)
            new_args[index] = i
            print(f"{indent}  Trying i = {i} at index {index} → new_args = {new_args}")
            rec_val = sheffer_fullness(*new_args, k=k, base_function=base_function, level=level + 1)
            score = min_for_sheffer(j_for_sheffer(x_next, i, k), rec_val, k)
            print(f"{indent}  j({i}, {x_next}, {k}) = {j_for_sheffer(x_next, i, k)}, rec_val = {rec_val}, min = {score}")
            results.append(score)
        final = max(results)
        print(f"{indent}→ Level {level} max = {final}")
        return final


#Second Sheffer's Function Fullness

def sheffer_2(x, y, k):
    return (min(x % k, y % k) + 1 )% k

def sheffer_3(x, y, k):
    for _ in range(k - 1):  # Do this for k-1 times since the first is already applied
        res = sheffer_2(res, res, k)
    return res

def sheffer_1(x, y, k):
    result = k - 1 - (sheffer_3(k - 1 - x, k - 1 - y))
    return result

def max_for_sheffer_1(x, y, k):
    # Start with the initial value
    res = sheffer(x, y, k)

    # Apply sheffer to the result k times
    for _ in range(k - 1):  # Do this for k-1 times since the first is already applied
        res = sheffer(res, res, k)

    return res

def increment_1(x, k):
    return sheffer(x, x, k)

def add_1(x, y, k):
    res = x
    for _ in range(y):  # Increment x by 1, y times
        res = increment(res, k)
    return res


def rolling_mod_max_for_sheffer_1(x, k):
    return max(add(x, i, k)  for i in range(k))

def j_for_sheffer_1(x, i, k):
    skip_alpha = k - 1 - i
    return (1 + max(add(x, alpha, k) % k for alpha in range(k) if alpha != skip_alpha))%k

def f_for_sheffer_1(s, i, x, k):
    return add(increment(s, k), max(j(i, x, k), k - 1 - s), k)%k

def opposite_for_sheffer_1(x, k):
    return max(f_for_sheffer_1(k - 1 - i, i, x, k) for i in range(k - 1))

def min_for_sheffer_1(x, y, k):
    return opposite_for_sheffer(max_for_sheffer(opposite_for_sheffer(x, k), opposite_for_sheffer(y, k), k), k)

def sheffer_fullness_1(*args, k, base_function, level):
    index = len(args) - level - 1
    x_next = args[index]

    indent = "  " * level  # For cleaner visual indentation in output

    if level == len(args) - 1:
        print(f"{indent}Base case at level {level}, args = {args}")
        result = base_function(args)
        print(f"{indent}→ base_fn({args}) = {result}")
        return result
    else:
        print(f"{indent}Level {level}, evaluating index {index}, x_next = {x_next}")
        results = []
        for i in range(k):
            new_args = list(args)
            new_args[index] = i
            print(f"{indent}  Trying i = {i} at index {index} → new_args = {new_args}")
            rec_val = sheffer_fullness_1(*new_args, k=k, base_function=base_function, level=level + 1)
            score = min_for_sheffer_1(j_for_sheffer_1(x_next, i, k), rec_val, k)
            print(f"{indent}  j({i}, {x_next}, {k}) = {j_for_sheffer(x_next, i, k)}, rec_val = {rec_val}, min = {score}")
            results.append(score)
        final = max(results)
        print(f"{indent}→ Level {level} max = {final}")
        return final

def base_fn(args):
    prod = 1
    for x in args:
        prod *= x
    return prod % 3
# Example usage
result = sheffer_fullness_1(*[2, 2, 1], k=3, base_function=base_fn, level=0)
#print(min_for_sheffer(0, 0, 3))
print(f"\nFinal result: {result}")
#print(opposite_for_sheffer(2, 3))
#print(add(2, 1,3))
#print(max_for_sheffer(1, 3, 4))


