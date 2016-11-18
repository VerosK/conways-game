
import numpy
import sys
import random

DEFAULT_SIZE = (20,20)

class ConwaysGame:
    def __init__(self, shape=DEFAULT_SIZE, data=None):
        """
        Inicializuje matici bunek.

        Pokud  `data` neni None, uvodni stav je inicializovan z nich.
        Jinak se vygeneruje prazdna matice o velikost `shape`
        """
        if data is None:
            self._data = numpy.zeros(shape=shape, dtype=bool)
        else:
            assert len(data.shape) == 2, data.shape
            self._data = data

    def add_random_cells(self, count=None):
        """Ozivi nahodne `count` bunek.   
        Pokud je `count` == None, ozivi 20% bunek
        """
        _d = self._data
        if count is None:
            count = 20 * _d.shape[0] * _d.shape[1] // 100

        for i in range(count):
            cell_address = []
            for axe,axe_size in enumerate(_d.shape):
                axe_position = random.randint(0,axe_size-1)
                cell_address.append(axe_position)

            cell_address = tuple(cell_address)
            _d[cell_address] = True
                
    def live_cells_count(self):
        return numpy.count_nonzero(self._data)

    def _number_of_neighbourds(self, x, y):
        count = 0
        _d = self._data
        for dx in (-1, 0, +1):
            for dy in (-1, 0, +1):
                if dx == dy == 0: continue
                _x, _y = x + dx, y + dy
                if _x < 0: continue
                if _y < 0: continue
                if _x >= _d.shape[0]: continue
                if _y >= _d.shape[1]: continue
                if _d[_x][_y]:
                    count += 1
        return count

    def _count_new_state(self, x, y):
        """Spocitat a vrati novy stav bunky na `x`, `y`
        """
        state_now = self._data[x][y]
        neighbourds = self._number_of_neighbourds(x,y)
        if state_now:   # I'm alive
            if neighbourds < 2: return False
            if 2 <= neighbourds <= 3: return True
            if 4 <= neighbourds: return False
        else:   # I'm dead now
            if neighbourds == 3: return True
            return False

    def next_step(self):
        """
        Udela dalsi iteraci a ulozi ji do data
        """
        shape = self._data.shape
        _new_cells = numpy.zeros(
                dtype=bool, shape=shape)
        #
        for x in range(shape[0]):
            for y in range(shape[1]):
                new_state = self._count_new_state(x, y)
                _new_cells[x][y] = new_state
        self._data = _new_cells

    def dump(self, fileobj=sys.stdout):
        """
        Vypise hru do `fileobj`
        """
        _d = self._data
        for x in range(_d.shape[0]):
            for y in range(_d.shape[1]):
                if _d[x][y]:
                    fileobj.write('[]')
                else: 
                    fileobj.write('_ ')
            fileobj.write('\n')

    @classmethod
    def fromString(kls, datastring="...\nXXX\n...\n", live='X'):
        "Nainicializuje hru z retezce"
        lines = datastring.split('\n')
        shape = [0,0]
        for ln in lines:
            if not ln: continue
            if len(ln) > shape[1]: shape[1] = len(ln)
            shape[0] += 1
        data = numpy.zeros(dtype=bool, shape=tuple(shape))
        #
        y = 0
        for ln in lines:
            if not ln: continue
            for x,c in enumerate(ln):
                if c == live:
                    data[y][x] = True
            y += 1
        return kls(data=data)
