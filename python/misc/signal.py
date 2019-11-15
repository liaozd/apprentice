from blinker import signal


class Button(object):
    def __init__(self, label):
        self.label = label
        self.clicked = signal('clicked')

    def click(self, pos):
        self.clicked.send(self, pos=pos)

    def __str__(self):
        return 'Button({})'.format(self.label)


def on_click(sender, pos):
    print(f'on_click, sender: {sender}, pos: {pos}')


btn = Button('btn')

btn.clicked.connect(on_click)
btn.click((100, 200))
