from distutils.core import setup

from easywatch import __version__


setup(
    name="easywatch",
    version=__version__,
    description="super simple directory monitoring",
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="https://github.com/Ceasar/easywatch",
    keywords=["directory", "polling", "monitoring"],
    packages=["easywatch"],
    classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    ],
)
