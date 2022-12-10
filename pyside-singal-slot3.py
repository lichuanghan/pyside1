import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot


class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal((int, str), (str,), (bool,))

    def __init__(self, parent=None):
        super().__init__(parent)

        self.speak[(int, str)].connect(self.say_something)
        self.speak[str].connect(self.say_something)
        self.speak[bool].connect(self.say_something)

    # define a new slot that receives a C 'int' or a 'str'
    # and has 'say_something' as its name
    @Slot(int, str)
    @Slot(str)
    @Slot(bool)
    def say_something(self, arg):
        if isinstance(arg, bool):
            print("This is a bool:", arg)
        elif isinstance(arg, (int,str)):
            print("This is a tuple:", arg)
        elif isinstance(arg, str):
            print("This is a str:", arg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()

    # emit 'speak' signal with different arguments.
    # we have to specify the str as int is the default
    someone.speak[int, str].emit(10, "hee lll")
    someone.speak[str].emit("Hello everybody!")
    someone.speak[bool].emit(True)
