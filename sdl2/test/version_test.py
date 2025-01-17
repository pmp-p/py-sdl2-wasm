import sys
import ctypes
import pytest
import sdl2
from sdl2 import dll, __version__, version_info


def test_SDL_version():
    v = sdl2.SDL_version(0, 0, 0)
    assert v.major == 0
    assert v.minor == 0
    assert v.patch == 0

def test_SDL_GetVersion():
    v = sdl2.SDL_version()
    sdl2.SDL_GetVersion(ctypes.byref(v))
    assert type(v) == sdl2.SDL_version
    assert v.major == 2
    assert v.minor == 0
    assert v.patch >= 5

def test_SDL_VERSIONNUM():
    assert sdl2.SDL_VERSIONNUM(1, 2, 3) == 1203
    assert sdl2.SDL_VERSIONNUM(4, 5, 6) == 4506
    assert sdl2.SDL_VERSIONNUM(2, 0, 0) == 2000
    assert sdl2.SDL_VERSIONNUM(17, 42, 3) == 21203

def test_SDL_VERSION_ATLEAST():
    assert sdl2.SDL_VERSION_ATLEAST(1, 2, 3)
    assert sdl2.SDL_VERSION_ATLEAST(2, 0, 0)
    assert sdl2.SDL_VERSION_ATLEAST(2, 0, 1)
    assert not sdl2.SDL_VERSION_ATLEAST(2, 0, 100)

def test_SDL_GetRevision():
    rev = sdl2.SDL_GetRevision()
    # If revision not empty string (e.g. Conda), test the prefix
    if len(rev):
        if dll.version >= 2016:
            assert rev[0:4] == b"http"
        else:
            assert rev[0:3] == b"hg-"

def test_SDL_GetRevisionNumber():
    if sys.platform in ("win32",) or dll.version >= 2016:
        # HG tip on Win32 does not set any revision number
        assert sdl2.SDL_GetRevisionNumber() >= 0
    else:
        assert sdl2.SDL_GetRevisionNumber() >= 7000
