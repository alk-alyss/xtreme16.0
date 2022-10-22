import random

"""
0-1 Knapsack problem
--------------------
Given weights and values of n items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
greedy solution do not work:
W = 5, items = 3
wt = [1, 2, 3]
val = [6, 10, 12] ratio (val/wt) = [6, 5, 4]
greedy solution = 6 (1) + 10 (2) = 16 (3),
optimal = 10 (2) + 12 (3) = 22 (5)
Method 1: Recursion by Brute-Force algorithm OR Exhaustive Search
-----------------------------------------------------------------
A simple solution is to consider all subsets of items and calculate the total weight and
value of all subsets.
Consider the only subsets whose total weight is smaller than W.
From all such subsets, pick the maximum value subset.
Time Complexity: O(2^n)
1) Optimal Substructure:
------------------------
To consider all subsets of items,
there can be two cases for every item:
(1) the item is included in the optimal subset,
(2) not included in the optimal set
So, the maximum value that can be obtained from n items is max of following two values.
1) Maximum value obtained by n-1 items and W weight (excluding nth item).
2) Value of nth item plus maximum value obtained by n-1 items
and W minus weight of the nth item (including nth item).
if there is item W-wt[n-1] > 0
knapsack(W, wt, val, n) = max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1),
knapsack(W, wt, val, n-1))
else
knapsack(W, wt, val, n) = knapsack(W, wt, val, n-1)
If weight of nth item is greater than W, then the nth item
cannot be included and case 1 is the only possibility.
Time complexity of solution is exponential (2^n)
2) Overlapping Subproblems
--------------------------
Since suproblems are evaluated again, this problem has Overlapping Subprolems property.
So the 0-1 Knapsack problem has both properties of a DP problem.
Time Complexity: O(nW)
where n is the number of items and W is the capacity of knapsack
if wt[i-1] <= w:
K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
else:
K[i][w] = K[i-1][w]
W = 7, items=4
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
val wt | 0 1 2 3 4 5 6 7 = W
--- -- | --- --- --- --- --- --- --- ---
- | 0 0 0 0 0 0 0 0
[ 1] 1 | 0 1 1 1 1 1 1 1 1 = max(0, 1 + 0)
[ 4] 3 | 0 1 1 4 5 5 5 5 4 = max(1, 4 + 0)
[ 5] 4 | 0 1 1 4 5 6 6 9 5 = max(5, 5 + 0)
[ 7] 5 | 0 1 1 4 5 7 8 9 7 = max(6, 7 + 0)
solution = K[n][W] = 9
what items:
9 = 9 or K[4][7-5] + 7 --> item x4=0
9 = 5 or K[3][7-4] + 5 --> item x3=1
4 = 1 or K[2][3-3] + 4 --> item x2=1
item x1=0
"""


# ---
# A naive recursive implementation of 0-1 Knapsack problem
# Returns the max value in a knapsack of capacity W
# Time Complexity: O(2^n)
# -----------------------
def knapsack(W, wt, val, n):
    # base case, no item left or no more weight
    if n == 0 or W <= 0: return 0
    # If weight of the nth item is more than W,
    # then this item cannot be included in the optimal solution
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    # return the maximum of two cases:
    # 1. n item included
    # 2. not included
    return max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
               knapsack(W, wt, val, n - 1))


# ---
# DP for 0-1 Knapsack problem
# Returns the max value in a knapsack of capacity W
# Tabulation (bottom up)
# Time Complexity: O(n*W), pseudopolynomial
# ------------------------------------------

def knapsackDP_tab(W, wt, val):
    n = len(wt)
    K = [[0] * (W + 1) for _ in range(n + 1)]
    # build table K[][] bottom up
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
    return K[n][W]


# ---
# Memoization (Top Down)
# ----------------------
def knapsackDP_mem(W, wt, val, n, mem=None):
    if mem is None:
        mem = {}
    if (n, W) in mem:
        return mem[(n, W)]
    # base conditions
    if n == 0 or W <= 0: return 0
    # can I take item n-1 ?
    if wt[n - 1] > W:
        mem[(n, W)] = knapsackDP_mem(W, wt, val, n - 1)
        return mem[(n, W)]
    else:
        # elif wt[n-1] <= W:
        mem[(n, W)] = max(val[n - 1] + knapsackDP_mem(W - wt[n - 1], wt, val, n - 1),
                          knapsackDP_mem(W, wt, val, n - 1))
        return mem[(n, W)]


if __name__ == '__main__':
    W = 7
    wt = [1, 2, 4, 16]
    val = [1, 1, 1]
    print('val =', ''.join([str(x).rjust(4) for x in val]))
    print('wt =', ''.join([str(x).rjust(4) for x in wt]))
    print('W =', W)
    print(' total val =', knapsack(W, wt, val, len(wt)))
    print('DP tab val =', knapsackDP_tab(W, wt, val))
    print('DP mem val =', knapsackDP_mem(W, wt, val, len(wt)))
