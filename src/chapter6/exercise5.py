word = 'X-DSPAM-Confidence: 0.8475 '
f = word.find(':')
f1 = word[f+1:]
f2 = float(f1)
print(f2)
