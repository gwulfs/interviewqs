def merge_arrays(a, b):
    final = []
    a_i = 0
    b_i = 0
    for e in range(len(a+b)):
        if a_i == len(a) and b_i == len(b):
            return final
        elif a_i == len(a):
            final.append(b[b_i])
            b_i += 1
        elif b_i == len(b):
            final.append(a[a_i])
            a_i += 1
        else:
            if a[a_i] < b[b_i]:
                final.append(a[a_i])
                a_i += 1
            else:
                final.append(b[b_i])
                b_i += 1
    return final
