def move_up(A,i,j,walls):
	'''Utility function if you move up'''
       	final = 0.0
	try:
		if (i+1,j) not in walls:
			val = A[i+1][j]
			final += 0.8*val
		else:
			raise IndexError


	except IndexError:
		final += 0.8*A[i][j]

	try:
		if (i,j+1) not in walls:
			val = A[i][j+1]
			final += 0.1*A[i][j+1]
		else:
			raise IndexError
	except IndexError:
		final += 0.1*A[i][j]

	try:
		if (i,j-1) not in walls:
			if j==0:
				final += 0.1*A[i][j]
			else:
				val = A[i][j-1]
				final+=0.1*A[i][j-1]
		else:
			raise IndexError
	except IndexError:
		final += 0.1*A[i][j]

	return final

def move_down(A,i,j,walls):
	'''Utility function if you move down'''
	final=0.0
	try:
		if (i-1,j) not in walls:
			val=A[i-1][j]
                        # ask about this!!! TODO 
			if i==0:
				final+=0.8*A[i][j]
			else:
				final+=0.8*A[i-1][j]
		else:
			raise IndexError

	except IndexError:
		final+=0.8*A[i][j]

	try:
		if (i,j+1) not in walls:
			val=A[i][j-1]
			final+=0.1*A[i][j+1]
		else:
			raise IndexError
	except IndexError:
		final+=0.1*A[i][j]

	try:
		if (i,j-1) not in walls:
			val=A[i][j-1]
			if j==0:
				final+=0.1*A[i][j]
			else:
				final+=0.1*A[i][j-1]
		else:
			raise IndexError
	except IndexError:
		final+=0.1*A[i][j]

	return final



def move_right(A,i,j,walls,flag=False):
	'''Utility function if you move right'''
	final=0.0
	try:
		if (i,j+1) not in walls:
			val=A[i][j+1]
			final+=0.8*A[i][j+1]
			if flag:
				print(final)
		else:
			raise IndexError

	except IndexError:
		final+=0.8*A[i][j]

	try:
		if (i+1,j) not in walls:
			val=A[i+1][j]
			final+=0.1*A[i+1][j]
			if flag:
				print(final)
		else:
			raise IndexError
	except IndexError:
		final+=0.1*A[i][j]


	try:
		if (i-1,j) not in walls:
			val=A[i-1][j]
			if i==0:
				final+=0.1*A[i][j]
			else:
				final+=0.1*A[i-1][j]
		else:
			raise IndexError
			
	except IndexError:

		final+=0.1*A[i][j]


	return final

def move_left(A,i,j,walls):
	'''Utility function if you move left'''
	final=0.0
	try:
		if (i,j-1) not in walls:
			val=A[i][j-1]
			if j==0:
				final+=0.8*A[i][j]
			else:
				final+=0.8*A[i][j-1]
		else:
			raise IndexError

	except IndexError:
		final+=0.8*A[i][j]

	try:
		if (i+1,j) not in walls:
			val=A[i+1][j]
			final+=0.1*A[i+1][j]
		else:
			raise IndexError
	except IndexError:
		final+=0.1*A[i][j]

	try:
		if (i-1,j) not in walls:
			val=A[i-1][j]
			if i==0:
				final+=0.1*A[i][j]
			else:
				final+=0.1*A[i-1][j]
		else:
			raise IndexError
	except IndexError:
		final+=0.1*A[i][j]
	return final


def VI(A, start_state, end_states, walls, step_reward):
	'''Value Iteration Algortihm'''

	# actions = {0:"north", 1:"east", 2:"south", 3:"west"}

	U = [[0 for i in range(len(A[0]))] for j in range(len(A))]
	tolerance = 0.01
	iter = 0

	while 1:
		#Run Until Convergance
		iter += 1
		new = [[0 for i in range(len(A[0]))] for j in range(len(A))]

		for i in range(len(A)):
			for j in range(len(A[i])):
                                # print "& ",
				if (i,j) in end_states or (i,j) in walls:
					new[i][j] = A[i][j]
                                        # if (i,j) in walls:
                                            # print 100,
                                        # else:
                                            # print "%.3f" % (new[i][j] + 52),
				else:
					#Add step reward
					new[i][j] = step_reward + A[i][j]
					v1 = move_up(U,i,j,walls)
					v2 = move_down(U,i,j,walls)
					v3 = move_right(U,i,j,walls)
					v4 = move_left(U,i,j,walls)
					#Pick max of 4 options
					new[i][j] += max([v1,v2,v3,v4])
                                        # if max([v1,v2,v3,v4]) == v1:
                                            # print "%.3f" % (new[i][j] + 42),
                                        # elif max([v1,v2,v3,v4]) == v3:
                                            # print "%.3f" % (new[i][j] + 32),
                                        # elif max([v1,v2,v3,v4]) == v2:
                                            # print "%.3f" % (new[i][j] + 22),
                                        # elif max([v1,v2,v3,v4]) == v4:
                                            # print "%.3f" % (new[i][j] + 12),
                        # print

		to_stop=True
		for i in range(len(U)):
			for j in range(len(U[i])):
                                if abs(U[i][j]-new[i][j]) > 0.01 * abs(U[i][j]):
					to_stop=False

				U[i][j]=new[i][j]

		if to_stop==True:
			break
	return U


if __name__ == "__main__":
	'''Input'''
	first_inp=raw_input()
	n, m = int(first_inp.split()[0]), int(first_inp.split()[1])
	A = []
	start_states = []
	end_states = {}
	walls = {}
	for i in range(n):
		s = [float(i) for i in raw_input().split()]
		A.append(s)

	second_inp=raw_input()
	E = int(second_inp.split()[0])
	W = int(second_inp.split()[1])

	for i in range(E):
		temp = raw_input().split()
		end_states[int(temp[0]), int(temp[1])] = 1

	for i in range(W):
		temp=raw_input().split()
		walls[int(temp[0]), int(temp[1])] = 1

	temp = raw_input().split()
	start_state = (int(temp[0]), int(temp[1]))
	step_reward = float(raw_input())

        for i in range(n):
            walls[i, -1] = 1;
            walls[i, m] = 1;
        for i in range(m):
            walls[-1, i] = 1;
            walls[n, i] = 1;

	ans = VI(A, start_state, end_states, walls, step_reward)

        for i in range(len(ans)):
                for j in range(len(ans[i])):
                        print "%.3f" % ans[i][j],
                print
