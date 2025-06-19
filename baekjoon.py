n = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)

P = []
for x in A:
    idx = sorted_A.index(x)
    P.append(idx)
    sorted_A[idx] = -1

print(*P)