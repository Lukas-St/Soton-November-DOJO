def load_file():
	input_file = open('DOJO Input string.txt', 'r')
	Votes = []
	for i in range(0, 100):
		line = input_file.readline().rstrip()
		Votes.append([])
		for j in range(0,99):
			Votes[i].append(line[j])
		#Votes[i] = Votes[i].rstrip()
	return (Votes)

def print_result(Votes):
	for i in range(0, 100):
		print (Votes[i])

v = load_file()
type(v[1][1])
print_result(v)