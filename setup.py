from setuptools import setup

from main import __version__

setup (
    name="downloader"
    version=__version__

    url = 'https://github.com/jayachandra27/pdf_cli'
    author="Jay Reddy"

    py_modules=["main"]
)