# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# MySolution
text = "X-DSPAM-Confidence:    0.8475"
text = text.replace(' ','')
start = text.find(':')
num = float(text[(start+1):])
print(num)