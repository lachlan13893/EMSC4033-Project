Begin by importing pyshtools and matplotlib.pyplot to the dependencies.py file

Upload .gfc files containing harmonic coefficients to the Files folder

# my_functions.py
## File_Size function
Define the file size function
First the spherical harmonic coefficient file was loaded
Print statement detailing the spherical harmonic degree was written
Print statements regarding rough computational guide was inserted. This was based upon spherical harmonic degree

## Gravity_Field function
Define the Gravity Field function
First the spherical harmonic coefficient file was loaded
The coefficient file was then expanded, such that plotting was possible
The plot of the gravity field was generated
Titles, labels, and colourbar were added
Additionally a grid was added, to make the longitude and latitude of the map clearer

## Gravity_Field_Limited function
Again the Gravity_Field_Limited function was defined. The steps entailed start as a copy of the Gravity_Field function
Once a copy of the Gravity_Field function was made, it was modified
The first modification was to stop the function if the spherical harmonic coefficient was sufficiently low (under degree 200). This was to prevent a low resolution solution from being made.
The second was to stop the function if the spherical harmonic coefficient exceeded degree 2000. This was to reduce computation time.

# LachlanProjectCode.ipynb
This file was written to use each of the three functions for a given coefficient file
The first is to measure the spherical harmonic degree of the file
The second is to generate the gravity field solutions using the spherical harmonic model coefficients
The third is to only return the gravity field solution if it is within an upper and lower spherical harmonic degree range
The input required is the name and file location of the coefficient file to be plotted

# Test.ipynb
This file contains several tests for the three functions