
from conway import ConwaysGame
import logging
import time
import numpy

ITERATIONS = 10

CLEAR = '\x1b[2J\x1b[H'

PULSAR = """\
............
............
XXX.........
............
.....XXX....
............
............
............
"""

def main():
    logging.basicConfig(level=logging.DEBUG)
    game = ConwaysGame.fromString(PULSAR)
    
    step_nr = 0
    while True:
        if step_nr:
            time.sleep(1)
        step_nr += 1
        print(CLEAR)
        live_cells = game.live_cells_count()
        print("Step {}# ========= {}".
                format(step_nr, live_cells))
        game.dump()
        game.next_step()
    


if __name__ == '__main__':
	main()
