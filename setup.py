from setuptools import setup

setup(
    name='changelogger',
    version='0.1.0',
    py_modules=['changelogger'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        changelogger=changelogger:cli
    '''
)
