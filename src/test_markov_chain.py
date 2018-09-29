class my_markov_chain:
	def __init__(self, initial_state):
		self.curr_state = initial_state

	def step(self, probability):
		if self.curr_state == a:
			if probability < 0.4166666666666667:
				self.curr_state = b
			elif probability < 0.5833333333333334:
				self.curr_state = c
		elif self.curr_state == b:
			if probability < 1.0:
				self.curr_state = c

