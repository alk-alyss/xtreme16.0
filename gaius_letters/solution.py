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


def decrypt(text, crypto):
    letters = {chr(ord('a') + i): crypto[i][0] for i in range(26)}
    for i in range(26):
        letters[chr(ord('A') + i)] = crypto[i][0]
    print(letters)


# t1 = '''M fdahq ime ragzp uz Dayq oazfmuzuzs tgzpdqpe ar xqffqde iduffqz nk Vgxuge Omqemd. Mxx ar ftqy iqdq qzodkbfqp iuft m Omqemd oubtqd iuft ftq wqk egebqofqp fa nq tue nudftpmk uz Vgxk.
#
# Idufq m bdasdmy fa pqodkbf ftq xqffqde.
#
# Azxk ftq mxbtmnqf otmdmofqde rday Mm fa Ll mdq qzodkbfqp. Gbbqdomeq mzp xaiqdomeq otmdmofqde mdq qzodkbfqp ftq emyq imk ituxq bdqeqdhuzs ftqud omeq. Zgynqde, ebmoqe, mzp ebqoumx otmdmofqde mdq mxx wqbf gzotmzsqp.'''

# print(decrypt(t1))
# print(crypto)
print(decrypt('', crypto))
