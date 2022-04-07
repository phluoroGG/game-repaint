from collections import namedtuple, OrderedDict

Color = namedtuple('RGB', 'red, green, blue')
colors = {}


class RGB(Color):
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)


RED = RGB(200, 0, 0)
BLUE = RGB(0, 0, 200)
GREEN = RGB(0, 200, 0)
YELLOW = RGB(200, 200, 0)
TEAL = RGB(0, 200, 200)
PURPLE = RGB(200, 0, 200)
G = RGB(200, 200, 200)
Q = RGB(200, 200, 100)
W = RGB(200, 100, 200)
E = RGB(100, 200, 200)
colors['red'] = RED
colors['blue'] = BLUE
colors['green'] = GREEN
colors['yellow'] = YELLOW
colors['teal'] = TEAL
colors['purple'] = PURPLE
colors['g'] = G
colors['q'] = Q
colors['w'] = W
colors['e'] = E
