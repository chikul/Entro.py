from setuptools import setup, find_packages


VERSION = "0.6.0"

REQUIREMENTS = []

setup(
    name="entro-py",
    version=VERSION,
    author="Pavel Chikul",
    author_email="pavel.tsikul@taltech.ee",
    license="MIT",
    url="https://github.com/chikul/Entro.py",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["entro_py"],
    install_requires=REQUIREMENTS,
)
