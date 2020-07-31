import math, os

message = {}

width = 160
height = 60
sizemult = 1
# sizemult = int(input('Font Size: (1-5, 1 is standard):\n>>>'))


letterHeight = 10 * sizemult
letterWidth = 8 * sizemult

lines = int(math.floor(height / ( letterHeight+sizemult )))
lettersPerLine = int(math.floor(width / (letterWidth+sizemult)))

print('Your message can have {} lines, each with up to {} characters. (with spaces)'.format(lines,lettersPerLine))
print('         \u001b[41m'+' '*lettersPerLine+'\u001b[0m')

for x in range(lines):
	message[x] = input('Line ' + str(x+1).zfill(2) + ': ').replace('. ','.').upper()
	if len(message[x]) > lettersPerLine:
		message[x] = message[x][0:lettersPerLine]
		print('\tMessage too long, cutting off to:\n\t\t'+message[x])

print('Okay! Would you like to decorate your text? [y/n]')
chh = input('>>> ')
linesinlines = []

def stretch(s):
    return ''.join([x*sizemult for x in s])

for bigline in range(lines):
	for line in range(10):
		thisline = ''
		for letter in message[bigline]:
			if letter == ' ':
				letter = 'space'
			elif letter == '.':
				letter = 'period'
			thisline = thisline + stretch(str(open('letters/'+letter).read()).split('\n')[line]+' ') + ('_ '*sizemult)
		extraspace = int(((width*2)-len(thisline))/2)
		# extraspace = 0
		for x in range(sizemult):
			linesinlines.append(thisline + ('_ '*extraspace))
	for x in range(sizemult):
		linesinlines.append('_ '*width)

for x in range(height - len(linesinlines)):
	linesinlines.append('_ '*width + '')

print(len(linesinlines))
f = open('output.py','w+')
f.write('# Add an @ symbol in place of an underscore to signify ink.\n# When you are done, hit control-x and floow the prompt at the bottom of the screen.\n# Thanks!\ndata = [\n')

c = 0
for x in linesinlines:
	c = c + 1
	if c == len(linesinlines):
		end = ''
	else:
		end = ','
	f.write('\'' + x + '\''+end+'\n')
f.write(']')
f.close()


if chh == 'y':
	os.system('nano output.py')

#remove spaces

cleared = []

import output

for x in output.data:
	cleared.append(x.replace(' ',''))

locs = {}

for y in range(width):
	locs[y] = []

for y in range(width):
	for x in range(len(cleared)):
		if cleared[x][y] == '@':
			locs[y].append(x)