class my_markov_chain:
	def __init__(self, initial_state):
		self.curr_state = initial_state

	def step(self, probability):
		if self.curr_state == "rain":
			if probability < 0.4166666666666667:
				self.curr_state = "sunny"
			elif probability < 0.5833333333333334:
				self.curr_state = "hail"
		elif self.curr_state == "hail":
			if probability < 1.0:
				self.curr_state = "snow"

	def next(self):
		if self.curr_state == "rain":
			return ['sunny', 'hail']
		elif self.curr_state == "hail":
			return ['snow']
		else:
			return []
