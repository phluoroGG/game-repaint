from collections import namedtuple

Color = namedtuple('RGB', 'red, green, blue')
colors = {}


class RGB(Color):
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)


RED = RGB(200, 0, 0)
BLUE = RGB(0, 0, 200)
GREEN = RGB(0, 200, 0)
YELLOW = RGB(200, 200, 0)
AQUA = RGB(0, 200, 200)
PURPLE = RGB(200, 0, 200)
BANANA = RGB(200, 200, 100)
PINK = RGB(200, 100, 200)
SKY = RGB(100, 200, 200)
GRAY = RGB(100, 100, 100)
colors['red'] = RED
colors['blue'] = BLUE
colors['green'] = GREEN
colors['yellow'] = YELLOW
colors['aqua'] = AQUA
colors['purple'] = PURPLE
colors['banana'] = BANANA
colors['pink'] = PINK
colors['sky'] = SKY
colors['gray'] = GRAY
