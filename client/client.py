from noughtsandcrosses import board, piece, InvalidMoveException
from human import humanplayer

def main():
	b = board()
	ps = {
		piece.X: humanplayer(piece.X),
		piece.O: humanplayer(piece.O)
	}
	print("player X: aiplayer")
	print("player O: humanplayer")

	move = None
	error = None
	p = piece.X

	print("begin!")
	while b.playing():
		print("\n{}".format(b))

		print("{}s turn".format(p))
		ps[p].update(move)
		move = ps[p].move()
		
		try:
			b.move(move, p)
		except InvalidMoveException as e:
			error = e
			break

		p = piece.other(p)

	if error:
		print(error)
	else:
		print(b)
		p[pi].update(move)
		print("game over!")

if __name__ == '__main__':
	main()