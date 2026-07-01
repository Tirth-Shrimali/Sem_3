""" 

"""

class TextEditor:
    def __init__(self):
        self.stack = []

    def type(self, ch):
        self.stack.append(ch)

    def undo(self):
        if self.stack:
            self.stack.pop()

    def getText(self):
        return "".join(self.stack)


editor = TextEditor()

editor.type('H')
editor.type('e')
editor.type('l')
editor.type('l')
editor.type('o')

print("Current Text:", editor.getText())

editor.undo()
print("After Undo:", editor.getText())