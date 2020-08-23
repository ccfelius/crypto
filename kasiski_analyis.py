# Letter	Count	 	Letter	Frequency
# E	21912	 	E	12.02
# T	16587	 	T	9.10
# A	14810	 	A	8.12
# O	14003	 	O	7.68
# I	13318	 	I	7.31
# N	12666	 	N	6.95

from nltk import word_tokenize, ngrams
import re
from more_itertools import take
from more_itertools import flatten

s = "Auge y bxwfcxc xl wrpk shbrt eiwemsttrnwr, mg kj awtrtgu ztyseg zr xl wrpk. Rwx" \
    " qrvyms hj pjrlvbrt vvvi bw pccjtw e pquc dk e pkgftk. Xug tfpgkrf kcmm mf erjaxh " \
    "pkgftkxrzk. Rwx guceet fexgj rwx qrujyvx lntu rd kinf. Jmbxsag nfd peavj rd kinf " \
    "zr bnwg eyyczi vv syrd se fvagrtg. Jfu ih guceet bx octi xl e fgtptm. Fbvy rwx " \
    "trtjmc mlnv jccww gjv ktlwniv ycw xug flt mlnv xcil mg uymjeh xpfu iai fgtptm ana " \
    "km raeaiv gi, uyg qkftk trqgjt llbwcb chx og rzax xb. Ukssrmai kft vmcjvpixbg vf " \
    "bxlgbxvp iai fgtptm mf erjaxh ptpnitrnnpqxl. " \
    "Hvhwcgxrg vpntl ss eiwemsttrnwr gnp sc ttwvgi mg aeefvp ih yfg rls vea jzbt mlr " \
    "uvagxx zgjqpzi ogkrtk se yfphx. Gvrycgl yfg r itr auktf xl e fgtptm xuck fxwif vyc " \
    "hxgegk ktlwnivq. Iai ptpnihkecgfxv qrvyms girf emi ui fgtptm. Zntzmjl trqgjt vea " \
    "wjc iai fcdc bxxuqu zjm hvhwcgxrg mvwh, ls gjvw rtraqk ptth rctf dmlrt'j ktlwnivq. " \
    "Hbrpg kft Verurp rbtugi fpl sanp yh feaa bcnl ef vyc cnqogi mu eigvvph br gjv " \
    "yailndvr, xm mf grqxec ptrazxh oa kpnbrt ccj iai xgpq. Rbtugiq iaeg ccjdp fvncgdgw " \
    "bh bcnl eeg tppvorf sw bhvr efkeeik ovrwhhf."

def interpunction(string):
    string = string.upper()

    # save on which indices there are non-alpha-numeric characters
    # delete non-alphabetic characters
    alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())

    indices = dict()
    counter = 0
    for i in string:
        if i not in alphabet:
            indices[counter] = i
        counter += 1

    return indices




def ngrams_list(string, n):

    # Remove spaces and non-alphanumeric characters
    string = re.sub(r'\W+', '', s).upper()

    # Create ngrams with nltk
    n_gram = ngrams(string, n)

    # Merge into a list with the ngrams
    gramlist = []
    for item in n_gram:
        gramlist.append("".join(item))

    return gramlist

def ngram_indices(ngrams):

    # Create dict with key = ngram and value = # occurences
    ngram_dict = dict()
    for i in ngrams:
        ngram_dict[i] = ngram_dict.get(i, 0) + 1
        ngram_dict = {k: v for k, v in sorted(ngram_dict.items(), key=lambda item: item[1], reverse=True)}

    # Count indices of ngrams
    ngram_idict = dict()
    for i in ngram_dict.keys():
        indices = []
        for j in range(len(ngrams)):
            if ngrams[j] == i:
                indices.append(j+1)

        ngram_idict[i] = indices

    return ngram_dict, ngram_idict

def empty_spaces(dict_ngram):
    spaces_dict = dict()
    for item_ in dict_ngram.items():
        item = item_[1]
        if len(item) > 1:
            list_spaces = []
            length = len(item)
            for i in range(length):
                counter = 0
                if counter < length:
                    counter += 1
                    nb = item[i]
                    temp = item[i+1:]
                    for j in temp:
                        val = j - nb
                        list_spaces.append(val)
            spaces_dict[item_[0]] = list_spaces

    return spaces_dict

def find_factors(num):

    # Derived from:
    # # Vigenere Cipher Hacker
    # # http://inventwithpython.com/hacking (BSD Licensed)

    if num < 2:
        return []  # numbers less than 2 have no useful factors

    factors = []  # the list of factors found

    # When finding factors, you only need to check the integers up to
    # MAX_KEY_LENGTH.
    for i in range(2, 10 + 1):  # don't test 1
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))

bigrams = ngrams_list(s, 2)
trigrams = ngrams_list(s, 3)

trigram_occurences, trigram_indices = ngram_indices(trigrams)
bigram_indeices = ngram_indices(bigrams)[1]

trigram_spaces = empty_spaces(trigram_indices)
print(trigram_spaces)
print(trigram_occurences)
print(trigram_indices)

count = 0
e_numbers = set([])
for i in trigram_spaces.values():
    if count < 30:
        count += 1
        for j in i:
            e_numbers.add(j)
    else:
        break

factors = []
for i in e_numbers:
    factors.extend(find_factors(i))

c = [item for item in factors]
d = {item:c.count(item) for item in c}
occurrences = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

# Take first X items of likely keylengths
n_items = take(3, occurrences.items())

suggested = ""
for item in range(len(n_items)):
    suggested = suggested + str(n_items[item][0]) + " "

suggested = suggested + " are possible keylengths"

print(suggested)

def frequency_analysis(string, key_length=1):

    # Remove spaces and non-alphanumeric characters
    string = re.sub(r'\W+', '', s).upper()
    l_string = list(string)
    freq_list = []

    for j in range(key_length):

        # make strings with keylengths
        l_string_ = l_string[j::key_length]

        # count frequencies of chars
        freq = dict()
        for i in l_string_:
            freq[i] = freq.get(i, 0) + 1
            freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

        freq_list.append(freq)

    return freq_list

result = frequency_analysis(s, 7)

keys = []
for i in result:
    print(i)
    keys.append(list(i.keys()))

print()

# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# Key is: ENCRYPT -> 4, 13, 2, 17, 24, 15, 19

def key_transform(key):
    shifts = []
    key = key.upper()
    key_ = list(key)
    alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())

    for k in key_:
        shifts.append(alphabet.index(k))

    return shifts


shifts = key_transform('encrypt')

def decrypt_vignere(inputs, shifts):
    alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
    dict_list = []

    counter = 0
    for i in inputs:
        message = dict()
        shift = shifts[counter]
        for j in i:
            index = alphabet.index(j)
            newindex = (index - shift) % 26
            new_char = alphabet[newindex]
            message[j] = new_char

        dict_list.append(message)
        counter += 1

    return dict_list

resultado = decrypt_vignere(keys, shifts)
for i in resultado:
    print(i)

def decrypted_text(dictlist, string, key_length):

    # Remove spaces and non-alphanumeric characters
    string = re.sub(r'\W+', '', s).upper()
    l_string = list(string)
    freq_list = []

    counter = 0
    for j in range(len(l_string)):
        convert = dictlist[counter]
        freq_list.append(convert[l_string[j]])
        if counter < key_length - 1:
            counter += 1
        else:
            counter = 0
    return freq_list


final = decrypted_text(resultado, s, 7)
interpunct = interpunction(s)

for i in interpunct.keys():
    final.insert(i, interpunct[i])

fin_sentence = "".join(final).lower()
fin = ". ".join(i.capitalize() for i in fin_sentence.split(". "))
print(fin)






