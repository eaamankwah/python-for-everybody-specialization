text = "X-DSPAM-Confidence:     0.8475"
firstsig = text.find('0')
lastsig = text.find('5',firstsig)
decimal = text[firstsig : lastsig+1 ]
decimal.strip()
print decimal

