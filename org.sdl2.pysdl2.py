import time
import aio



class tui:
    # use direct access, it is absolute addressing on raw terminal.
    out = sys.__stdout__.write

    # save cursor
    def __enter__(self):
        self.out("\x1b7\x1b[?25l")
        return self

    # restore cursor
    def __exit__(self, *tb):
        self.out("\x1b8\x1b[?25h")

    def __call__(self, *a, **kw):
        self.out("\x1b[{};{}H{}".format(kw.get("z", 12), kw.get("x", 40), " ".join(a)))


def draw():
    import time

    def box(t,x,y,z):
        lines = t.split('\n')
        fill = "─"*len(t)
        if z>1:
            print( '┌%s┐' % fill, x=70, z=z-1)
        for t in lines:
            print( '│%s│' % t, x=70, z=2)
            z+=1
        print( '└%s┘' % fill, x=70, z=z)

    with tui() as print:
        # draw a clock
        t =  "%2d:%2d:%2d ☢ 99%% " % time.localtime()[3:6]
        box(t,x=70,y=0,z=2)


async def render_ui():
    while True:
        draw()
        await asyncio.sleep(1)
        sys.stdout.flush()


def setup():
    global setup

async def loop():
    while not aio.loop.is_closed():
        draw()
        await aio.sleep(1)

