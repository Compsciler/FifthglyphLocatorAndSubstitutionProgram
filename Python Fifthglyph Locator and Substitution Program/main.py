# Python program intrinsically contains 0 fifthglyphs
# Probably a distinct O(n) way to do it, this approach looks slow
from AsciiGoldAward import asciiGoldAward

capitalFifthglyph = chr(69)
fifthglyph = chr(101)
msg = input("Input: ")
msgWithModifications = msg
fifthglyphTotal = 0
stringPosition = 0
msgCharTotal = sum(1 for c in msg)
for c in msg:
	if c == capitalFifthglyph or c == fifthglyph:
		fifthglyphTotal += 1
		msgWithModifications = msgWithModifications[0: stringPosition] + "■" + msg[(stringPosition + 1): msgCharTotal]
	stringPosition += 1
print("Fifthglyph Total Count (maunally): " + str(fifthglyphTotal))
print("Fifthglyph Total Count (using Python Library built-in functions): " + str(msg.count(capitalFifthglyph) + msg.count(fifthglyph)))
if fifthglyphTotal >= 1:
	if fifthglyphTotal == 1:
		pluralAnnotation = "A fifthglyph was found in your post:"
	if fifthglyphTotal != 1:  # Substitution of -ls- block
		pluralAnnotation = "Fifthglyphs found in your post:"
	print(pluralAnnotation)
	for word in msgWithModifications.split():
		if "■" in word:
			print("  " + word)
	print("\n")
print("Input with modifications: " + msgWithModifications)

if fifthglyphTotal == 0:
	print("\n" + asciiGoldAward)