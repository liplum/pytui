from . import colors


class ColorStr:
    def __init__(self, txt: str, *, fg=None, bg=None, style=None):
        self.txt = txt
        self.fg = fg
        self.bg = bg
        self.style = style

    def __str__(self):
        return self.txt

    def __repr__(self):
        return repr(self.txt)

    def __len__(self):
        return len(self.txt)

    def get(self) -> str:
        return colors.tint(self.txt, fg=self.fg, bg=self.bg, style=self.style)

    def append(self, txt: str):
        self.txt += txt

    def __add__(self, other) -> "ColorStr":
        return ColorStr(self.txt + str(other), fg=self.fg, bg=self.bg, style=self.style)

    def __mul__(self, times: int) -> "ColorStr":
        return ColorStr(self.txt * times, fg=self.fg, bg=self.bg, style=self.style)


class Palette:
    def __init__(self, fg=None, bg=None, style=None):
        self.fg = fg
        self.bg = bg
        self.style = style

    def tint(self, txt: str) -> ColorStr:
        return ColorStr(txt, fg=self.fg, bg=self.bg, style=self.style)
