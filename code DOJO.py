def load_file():
	input_file = open('DOJO Input string.txt', 'r')
	Votes = []
	for i in range(0, 100):
		Votes.append(input_file.readline())
		Votes[i] = Votes[i].rstrip()
	return (Votes)

def print_result(Votes):
	for i in range(0, 100):
		print (Votes[i])

v = load_file()
print_result(v)