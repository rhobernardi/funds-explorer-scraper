from setuptools import setup
setup(
    name = 'investments',
    version = '0.1.0',
    packages = ['fiis'],
    entry_points = {
        'console_scripts': [
            'fiis = fiis.__main__:main',
        ]
    })
