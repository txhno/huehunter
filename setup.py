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
    url='https://github.com/txhno/huehunter',
    license='MIT',
    description='A tool that detects dominant colors in images.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "opencv-python-headless",
        "numpy",
        "Pillow",
        "webcolors",
        "scikit-learn",
    ],
)
