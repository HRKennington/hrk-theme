import pathlib

__MAJOR__ = 0
__MINOR__ = 1
__MICRO__ = 3
__VERSION__ = (__MAJOR__, __MINOR__, __MICRO__)
__version__ = '.'.join(str(n) for n in __VERSION__)
__github_url__ = 'http://github.com/HRKennington/hrk-theme'
THEME_PATH = pathlib.Path(__file__).parent.as_posix()
