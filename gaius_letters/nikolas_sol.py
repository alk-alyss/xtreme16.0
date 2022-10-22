crypted = 'U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd.Efmzpmdp uzbgf agfbgf Oazefdmuzfe mzp zafqe'
decrypt = 'I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner.Standard input output Constraints and notes'
cypted = crypted.lower()
decrypt = decrypt.lower()
# d = {decrypt[i]: crypted[i] for i in range(len(crypted))}
d = {crypted[i]: decrypt[i] for i in range(len(crypted))}
for i in range(10):
    d[str(i)] = str(i)
# d['q'] = 'q'
# d['z'] = 'z'
# d['x'] = 'x'
# d['j'] = 'j'
# for i in ['\n', ',', '=', 'l']:
#     d[i] = i
d['j'] = 'x'
d['v'] = 'j'
d['l'] = 'l'

m = d.copy()
for i, v in m.items():
    d[i.upper()] = v.upper()

print(d)
text = """M fdahq ime ragzp uz Dayq oazfmuzuzs tgzpdqpe ar xqffqde iduffqz nk Vgxuge Omqemd. Mxx ar ftqy iqdq qzodkbfqp iuft m Omqemd oubtqd iuft ftq wqk egebqofqp fa nq tue nudftpmk uz Vgxk.

Idufq m bdasdmy fa pqodkbf ftq xqffqde.

Azxk ftq mxbtmnqf otmdmofqde rday Mm fa Ll mdq qzodkbfqp. Gbbqdomeq mzp xaiqdomeq otmdmofqde mdq qzodkbfqp ftq emyq imk ituxq bdqeqdhuzs ftqud omeq. Zgynqde, ebmoqe, mzp ebqoumx otmdmofqde mdq mxx wqbf gzotmzsqp.

Efmzpmdp uzbgf
Kagd bdasdmy ygef dqmp ftq fqjf ar ftq xqffqde rday ftq efmzpmdp uzbgf iuft m ymjuygy ar Z=10000 otmdmofqde. Ftq uzbgf iuxx nq m efduzs uz m euzsxq xuzq.

Efmzpmdp agfbgf
Kagd bdasdmy ygef bduzf ftq pqodkbfqp fqjf rad ftq uzbgf efduzs fa ftq efmzpmdp agfbgf.

Oazefdmuzfe mzp zafqe"""

decrypted_explanation = """a trove was found in rome containing hundreds of letters written by julius caesar. all of them were encrypted with a caesar cipher with the key suspected to be his birthday in july.

write a program to decrypt the letters.

only the alphabet characters from aa to ll are encrypted. uppercase and lowercase characters are encrypted the same way while preserving their case. numbers, spaces, and special characters are all kept unchanged.

standard input
your program must read the text of the letters from the standard input with a maximum of n=10000 characters. the input will be a string in a single line.

standard output
your program must print the decrypted text for the input string to the standard output.

constraints and notes"""


def decrypting(t, d):
    output = ''.join([d[letter] for letter in t])
    return output


def main():
    text = input()
    output = ''
    for i in text:
        if i not in d.keys():
            output += i
        else:
            output += d[i]
    print(output)


if __name__ == '__main__':
    main()
