# -*- coding: utf-8 -*-

from distutils.core import setup
setup(
    name = "Spreadsheet-Table-for-ReportLab",
    version = "0.0.1",
    author = "Tomasz Świderski",
    author_email = "contact@tomaszswiderski.com",
    description = ("Spreadsheet Table class for use with ReportLab platypus."),
    license = "BSD",
    keywords = "report lab spreadsheet table platypus",
    url = "https://github.com/tomaszswiderski/Spreadsheet-Table-for-ReportLab",
    packages=['spreadsheettable'],
    package_dir={'spreadsheettable': 'src'}
)