# Example:
# U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd.
# result :
# I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner.
from collections import defaultdict
original_input = "U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd."
output = "I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner."

crypto = defaultdict(list)
for i, char in enumerate(original_input):
    crypto[char].append(output[i])
print(crypto)
