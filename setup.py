from distutils.core import setup
import setuptools

__version_info__ = ('0', '0', '5')
__version__ = '.'.join(__version_info__)


setup(
    name="easywatch",
    version=__version__,
    description="super simple directory monitoring",
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="https://github.com/Ceasar/easywatch",
    keywords=["directory", "polling", "monitoring"],
    packages=["easywatch"],
    install_requires=["watchdog"],
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
