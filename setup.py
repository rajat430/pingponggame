from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name = 'pong-game',
    version = '1.0.0',
    description = 'Example PyPI package',
    py_modules = ["main","Ball","Paddle","ScoreBoard"],
    package_dir = {'': 'src'},
    author = 'JFrog',
    author_email = 'jfrog@jfrog.com',
    long_description = long_description,
    long_description_content_type = "text/markdown",
)
