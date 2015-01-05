def _letter_to_number(text):
	text = text.upper()
	text = text.replace("ONE","1")
	text = text.replace("TWO","2")
	text = text.replace("THREE","3")
	text = text.replace("FOUR","4")
	text = text.replace("FIVE","5")
	text = text.replace("SIX","6")
	text = text.replace("SEVEN","7")
	text = text.replace("EIGHT","8")
	text = text.replace("NINE","9")
	text = text.replace("ZERO","0")
	return text

def _phone_grab(text,tolerance=10):
	"""
	This is the bulk of the work, tolerance is the number of characters that are checked before
	it is assumed that the numbers input up this point are not part of a number.
	Note: Tolerance is a total, so it's not reset every time another digit is found.
	"""
	phone = []
	counter = 0
	found = False
	for ind,letter in enumerate(text):
		if letter.isdigit():
			phone.append(letter)
			found = True
		else:
			if found:
				counter += 1
			if counter > tolerance and found:
				phone = []
				counter = 0
				found = False

def _most_common(lists):
	indexes = []
	results = {k: 0 for k in range(len(lists))}
	for ind,elem in enumerate(lists):
		indexes.append( [elem for elem in xrange(0,ind)] + [elem for elem in xrange(ind+1,len(lists))] )
	for ind,elem in enumerate(lists):
		for index in indexes[ind]:
			if elem == lists[index]:
				results[ind] += 1
	return results 

def grab(text):
	text = _letter_to_number(text)
	possible_numbers = []
	for tol in xrange(10,17): possible_numbers.append( _phone_grab(text,tolerance=tol) )
	results = _most_common(possible_numbers)
	max_val = 0
	max_index = 0
	for ind,val in enumerate(possible_numbers):
		if results[ind] > max_val:
			max_val = results[ind]
			max_index = ind
	return possible_numbers[max_index]
