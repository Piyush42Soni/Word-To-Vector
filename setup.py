from setuptools import setup, find_packages

setup(
    name='Word_to_Vector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'gensim',
        'POT',
        'sklearn',
        'numpy',
        'pandas',
        'chardet'
    ],
)