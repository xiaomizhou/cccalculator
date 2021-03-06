# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup,find_packages



def get_long_description():
    descr = []
    for fname in ('README.md',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='cccalculator',
    version='0.0.3',
    description="cyclomatic complexity calculator for python file",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords='cyclomatic complexity python',
    author='Li Wang',
    author_email='wangli0829@gmail.com',
    url='https://github.com/xiaomizhou/cccalculator',
    license='MIT license',
    install_requires=["tree_sitter"],
    requires=["tree_sitter"],
    packages=find_packages(),
    include_package_data=True,
    # py_requires=["cccalculate"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)
