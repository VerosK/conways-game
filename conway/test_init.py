
from game import ConwaysGame
import numpy
import pytest


@pytest.mark.parametrize('xsize', [3, 5, 10])
@pytest.mark.parametrize('ysize', [3, 5, 10, 0])
def test_init_empty(xsize, ysize):
	"__init__ should return empty board "
	game = ConwaysGame(shape=[xsize, ysize])
	live_count = game.live_cells_count()
	assert live_count == 0

@pytest.mark.parametrize('xsize', [5, -1])
@pytest.mark.parametrize('ysize', [5, -1])
def test_init_size(xsize, ysize):
	"We shouldn't create negative size array"
        shape = [xsize, ysize]

        if xsize <= 0 or ysize <= 0:
            with pytest.raises(ValueError):
                game = ConwaysGame(shape=shape)
        else:
            game = ConwaysGame(shape=shape)
