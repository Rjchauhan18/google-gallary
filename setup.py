from setuptools import setup, find_packages

setup(
    name='googlegallary',
    version='0.4.0',
    author='Rahul chauhan',
    packages=['googlegallary'],
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    python_requires='>=3.6'
)
