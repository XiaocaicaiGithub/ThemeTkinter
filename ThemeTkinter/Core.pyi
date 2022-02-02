from tkinter import Tk
from tkinter import ttk as Widgets


class Window(Tk):
    def __init__(self, Caption: str = None, Size: tuple[int, int] | list[int, int] = None,
                 Position: tuple[int, int] | list[int, int] = None, MinSize: tuple[int, int] | list[int, int] = None,
                 MaxSize: tuple[int, int] | list[int, int] = None,
                 Resizable: tuple[bool, bool] | list[bool, bool] = None, Center: bool = True,
                 LoadThemes: bool = True): pass

    def SetDisplay(self, Display: bool) -> None: pass

    def SetCaption(self, Caption: str) -> None: pass

    def SetSize(self, Size: tuple[int, int] | list[int, int]) -> None: pass

    def SetPosition(self, Position: tuple[int, int] | list[int, int]) -> None: pass

    def SetMinSize(self, MinSize: tuple[int, int] | list[int, int]) -> None: pass

    def SetMaxSize(self, MaxSize: tuple[int, int] | list[int, int]) -> None: pass

    def SetResizable(self, Resizable: tuple[bool, bool] | list[bool, bool]) -> None: pass

    def SetTheme(self, Group: str, Type: str) -> None: pass

    def LoadThemes(self) -> None: pass

    def Center(self) -> None: pass

    @staticmethod
    def SetFrame(self, Frame: Widgets.Frame) -> None: pass
