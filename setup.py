# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:45:08 2021

@author: sshir
"""

from setuptools import setup
from os import path



VERSION = '0.0.6'
DESCRIPTION = 'Items recommendation for a specific user'


setup(
    name="easyreport",
    version=VERSION,
    author="Kishore",
    author_email="<kishoresshankar@gmail.com>",
    description=DESCRIPTION,
    
    keywords=['python', 'recommendation algorithm', 'recommender', 'recommendation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    py_modules = ['report']
)
