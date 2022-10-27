import io
from typing import TypeVar

TIO = TypeVar("TIO", bound=io.IOBase, covariant=True)


# @formatter:off
class FG:
    Black   = ";30"
    Red     = ";31"
    Green   = ";32"
    Yellow  = ";33"
    Blue    = ";34"
    Violet  = ";35"
    Cyan    = ";36"
    White   = ";37"
class BG:
    Black   = ";40"
    Red     = ";41"
    Green   = ";42"
    Yellow  = ";43"
    Blue    = ";44"
    Violet  = ";45"
    Cyan    = ";46"
    White   = ";47"
class Style:
    Default   = "0"
    Bold      = "1"
    Underline = "4"
    Reverse   = "7"
# @formatter:on


def tint(text: str,
         fg=None, bg=None, style=None):
    with io.StringIO() as s:
        tintIO(s, text, fg, bg, style)
        return s.getvalue()


def tintIO(s: TIO,
           text: str, fg=None, bg=None, style=None
           ) -> TIO:
    s.write("\033[")
    if style:
        s.write(style)
    if fg:
        s.write(fg)
    if bg:
        s.write(bg)
    s.write('m')
    s.write(text)
    s.write("\033[0m")
    return s
