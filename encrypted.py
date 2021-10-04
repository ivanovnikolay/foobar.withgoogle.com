import base64

encrypted = "ElESGwwFA10dTktVTEYeGxMAGkhKRgkNBgcDCQAeHBNGTlVGQUsdHQ4KAQQdTlpBSQoAAEEcHRhITFtZTh8PDR0DAkcMBQ5IQEFeCBUJBwoQA0MLBx9ITFtZTgMPAgAFDUsKTkdPSxMYCxQIGhxBRhROThgOCgReRVZGCAAJQQ5USUwYBQ9YTgs= "
my_eyes = str.encode("ivanoff.nikolay")
decoded = base64.b64decode(encrypted)
decrypted = ""
for i in range(0, len(decoded)):
    decrypted += chr((my_eyes[i%len(my_eyes)] ^ decoded[i]))

print(decrypted)