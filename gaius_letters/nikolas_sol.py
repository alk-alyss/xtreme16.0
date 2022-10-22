crypted = 'U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd.'
decrypt = 'I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner.'

d = {decrypt[i]: crypted[i] for i in range(len(crypted))}

text = """M fdahq ime ragzp uz Dayq oazfmuzuzs tgzpdqpe ar xqffqde iduffqz nk Vgxuge Omqemd. Mxx ar ftqy iqdq qzodkbfqp iuft m Omqemd oubtqd iuft ftq wqk egebqofqp fa nq tue nudftpmk uz Vgxk.

Idufq m bdasdmy fa pqodkbf ftq xqffqde.

Azxk ftq mxbtmnqf otmdmofqde rday Mm fa Ll mdq qzodkbfqp. Gbbqdomeq mzp xaiqdomeq otmdmofqde mdq qzodkbfqp ftq emyq imk ituxq bdqeqdhuzs ftqud omeq. Zgynqde, ebmoqe, mzp ebqoumx otmdmofqde mdq mxx wqbf gzotmzsqp.

Efmzpmdp uzbgf
Kagd bdasdmy ygef dqmp ftq fqjf ar ftq xqffqde rday ftq efmzpmdp uzbgf iuft m ymjuygy ar Z=10000"""

text2 = '''otmdmofqde. Ftq uzbgf iuxx nq m efduzs uz m euzsxq xuzq.
            Efmzpmdp agfbgf
Kagd bdasdmy ygef bduzf ftq pqodkbfqp fqjf rad ftq uzbgf efduzs fa ftq efmzpmdp agfbgf.

Oazefdmuzfe mzp zafqe'''


def decrypting(text, d):
    output = ''.join([d[letter]] for letter in text)
    return output


print(decrypting(text,d))

