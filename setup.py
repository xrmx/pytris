import setuptools

setuptools.setup(
    name="pytris",
    version="0.1.0",
    url="https://github.com/pycorso-its/pytris",

    author="Riccardo Magliocchetti",
    author_email="riccardo.magliocchetti@gmail.com",

    description="A simple Tic-tac-toe implementation",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
)
