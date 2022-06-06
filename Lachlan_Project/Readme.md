# Gravity Field Generator
This directory contains all the necessary software to generate an solution to the Earth's gravity field. The field solutionsa are generated using the pyshtools package, and can utilise any .gfc file containing spherical harmonic coefficients.

The three functions contained within perform three seperate actions.
1. The first function outputs the spherical harmonic degree, and a guide to computational time for the input coefficient file
2. The second function generates a gravity field based upon the spherical harmonic coefficients contained within the input file
3. The third function is the same as the second with two additional features. First, each solution generated must exceed a minimum spherical harmonic coefficient, and hence have a minimum resolution. Secondly there is a maximum degree, minimising computational time.

In this directory is the LachlanProjectCode.ipynb file, used to generate the gravity fields.
Each function requires an input value. This value can either be a resolution (Low, Moderate, High, Very High), or the path to a spherical harmonic coefficient file in .gfc format (e.g. 'Files/Tongji-Grace02k.gfc')

There is also a Test.py file that contains a number of tests for the functions contained within the directory

These tests can be run using the Test.ipynb file, also in this directory

The "Code" folder contains the dependencies and functions themselves.

The "Files" folder contains the spherical harmonic models, taken from the ICGEM.

The "Project" folder contains the project plan and report, pertaining to the intent and generation of the functions.