class piece:
	X, O = 'X', 'O'
	blank = ' '
	@staticmethod
	def other(p):
		return piece.O if p == piece.X else piece.X

class board:
	def __init__(self):
		self.grid = [[piece.blank for j in range(3)] for i in range(3)]
	def __str__(self):
		rows = [" | ".join(row) for row in self.grid[::-1]]
		board = " " + " \n---+---+---\n ".join(rows) + "\n"
		return board
	def move(self, move, p):
		if move < 1 or move > 9:
			raise Exception("invalid move: {}".format(move))
		
		# find that part of the grid
		m = move - 1
		i, j = m // 3, m % 3
		
		# make sure it's legal
		if self.grid[i][j] != piece.blank:
			raise InvalidMoveException("invalid move: {} (space already occupied)".format(move))

		# make the actual move
		self.grid[i][j] = p

	def playing(self):
		"""scan the board: True if game is still going, False otherwise"""
		runofXs = [piece.X] * 3
		runofOs = [piece.O] * 3

		runs = self._runs()
		for run in runs:
			if run == runofXs or run == runofOs:
				return False
		return True
	
	def winner(self):
		"""scan the board: True if game is still going, False otherwise"""
		runofXs = [piece.X] * 3
		runofOs = [piece.O] * 3

		runs = self._runs()
		for run in runs:
			if run == runofXs:
				return piece.X
			elif run == runofOs:
				return piece.O
		return None

	def _runs(self):
		rows = [[self.grid[i][j] for j in range(3)] for i in range(3)]
		cols = [[self.grid[i][j] for i in range(3)] for j in range(3)]
		dags = [[self.grid[i][i]   for i in range(3)],
				[self.grid[i][2-i] for i in range(3)]]
		return rows + cols + dags

class InvalidMoveException(Exception):
	"""Raised due to an invalid move"""