from sty import fg, RgbFg

black = RgbFg(0, 0, 0)
white = RgbFg(255, 255, 255)
red = RgbFg(255, 0, 0)
green = RgbFg(0, 255, 0)
blue = RgbFg(0, 0, 255)
grey = RgbFg(128, 128, 128)
aqua = RgbFg(0, 255, 255)
teal = RgbFg(0, 128, 128)
yellow = RgbFg(255, 255, 0)
magenta = RgbFg(255, 0, 255)
maroon = RgbFg(128, 0, 0)
olive = RgbFg(128, 128, 0)
navy = RgbFg(0, 0, 128)
crimson = RgbFg(175, 0, 42)
orange = RgbFg(255, 165, 0)

colours = {"black":black, "white":white, "red":red, "green":green, "blue":blue, "grey":grey, "gray":grey, "aqua":aqua, "teal":teal, "yellow":yellow, "magenta":magenta, "pink":magenta, "maroon":maroon, "olive":olive, "navy":navy, "crimson":crimson, "orange":orange}

def cprint(string="", icolour="white", iend="\n"):
  global colours
  fg.set_style("x", colours[icolour])
  print(fg.x + string + fg.rs, end=iend)
