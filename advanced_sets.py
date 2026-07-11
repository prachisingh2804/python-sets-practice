# ==============================
# Python Sets - Advanced Concepts
# Author: Prachi Singh
# ==============================

A = {1, 2, 3}
B = {3, 4, 5}

# Union
print("Union:", A.union(B))

# Intersection
print("Intersection:", A.intersection(B))

# Difference
print("Difference:", A.difference(B))

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Subset
C = {1, 2}
print("Is C subset of A?", C.issubset(A))

# Superset
print("Is A superset of C?", A.issuperset(C))
