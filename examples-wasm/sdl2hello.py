"""Simple example for using sdl2 directly."""
import os
import sys
import ctypes
import sdl2

running=True

def setup():
    global running
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    window = sdl2.SDL_CreateWindow(b"Hello World",
                                   sdl2.SDL_WINDOWPOS_CENTERED,
                                   sdl2.SDL_WINDOWPOS_CENTERED,
                                   592, 460, sdl2.SDL_WINDOW_SHOWN)
    fname = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "resources", "hello.bmp")
    image = sdl2.SDL_LoadBMP(fname.encode("utf-8"))
    windowsurface = sdl2.SDL_GetWindowSurface(window)
    sdl2.SDL_BlitSurface(image, None, windowsurface, None)
    sdl2.SDL_UpdateWindowSurface(window)
    sdl2.SDL_FreeSurface(image)
    running = True

def loop():
    global running
    event = sdl2.SDL_Event()

    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
            return False
        break
    else:
        return True
    sdl2.SDL_Delay(10)

setup()

if __EMSCRIPTEN__:
    print(__file__)
    aio.steps.append(loop)

else:
    while running:
        loop()
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()


