# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp_word = inp.upper()
inp_word = inp_word.rstrip()
print inp_word