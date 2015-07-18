from distutils.core import setup
import py2exe, sys

def finish():
    sys.argv.append("py2exe")
    setup(windows=["C:\Python27\MangaFox\MangaFoxScript.pyw"])
