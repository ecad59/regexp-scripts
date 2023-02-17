import re

#test = "Hey dudee"
test = ""
r = re.compile(test, re.IGNORECASE | re.UNICODE)

#k = "HèŶ Dûdéè"
k = ""

k1 = re.sub(
    r'[àâä]', "a", k, re.IGNORECASE | re.UNICODE)
k2 = re.sub(
    r'[ÀÂÄ]', "A", k1, re.IGNORECASE | re.UNICODE)
k3 = re.sub(
    r'[éèêë]', "e", k2, re.IGNORECASE | re.UNICODE)
k4 = re.sub(
    r'[ÉÈÊË]', "E", k3, re.IGNORECASE | re.UNICODE)
k5 = re.sub(
    r'[ïî]', "i", k4, re.IGNORECASE | re.UNICODE)
k6 = re.sub(
    r'[ÏÎ]', "I", k5, re.IGNORECASE | re.UNICODE)
k7 = re.sub(
    r'[ôö]', "o", k6, re.IGNORECASE | re.UNICODE)
k8 = re.sub(
    r'[ÔÖ]', "O", k7, re.IGNORECASE | re.UNICODE)
k9 = re.sub(
    r'[ùûü]', "u", k8, re.IGNORECASE | re.UNICODE)
k10 = re.sub(
    r'[ÙÛÜ]', "U", k9, re.IGNORECASE | re.UNICODE)
k11 = re.sub(
    r'[ÿŷ]', "y", k10, re.IGNORECASE | re.UNICODE)
k12 = re.sub(
    r'[ŸŶ]', "Y", k11, re.IGNORECASE | re.UNICODE)
k13 = re.sub(
    r'[ç]', "c", k12, re.IGNORECASE | re.UNICODE)
k14 = re.sub(
    r'[Ç]', "C", k13, re.IGNORECASE | re.UNICODE)

if r.match(k14) or r.search(k14):
  # your code here ...
else:
  # your code here ...
