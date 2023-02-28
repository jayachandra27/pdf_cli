from setuptools import setup

# from main_1 import __version__

setup(
    name='downloader',

    url='https://github.com/jayachandra27/pdf_cli',
    author='Jay Reddy',
    author_email="jayachandra.s.reddy@gmail.com",
    install_requires=[
        'requests>=2.17.3',
        'lxml',
        'bs4>=0.0.1'
        'click>=6.7',
        'click-log==0.3.2',
        'setuptools==45'
    ],
    entry_points={
        'console_scripts': [
            'myapplication=downloader.main1:download'
        ]
    }
)