from setuptools import setup, find_packages

setup(
    name='HueHunter',
    version='0.2.0',
    author='Roshan Warrier',
    author_email='roshanwarrierwork@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'huehunter=huehunter.huehunter:main',
        ],
    },
    url='http://pypi.python.org/pypi/HueHunter/',
    license='LICENSE.txt',
    description='A tool that detects dominant colors in images.',
    long_description=open('README.md').read(),
    install_requires=[
        "opencv-python-headless",
        "numpy",
        "Pillow",
        "webcolors",
        "scikit-learn",
    ],
)
