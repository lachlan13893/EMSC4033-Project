# Gravity Maps using Spherical Harmonics
## Executive Summary
Gravity varies across the surface of the Earth as a function of mass concentration. To display these variations on a global scale we use gravity fields. One such method for generating gravity fields is to use mathematical functions called spherical harmonics. I use a python package called "pyshtools" to create functions process and display such gravity field estimates from publicly available spherical harmonic coefficients. Additionally, these functions can display the spherical harmonic degree of the model, and limit the processing of a model if its degree is too high or too low.

## Goals
1. To assess the size of spherical harmonic coefficient files and the required computational time
2. To process spherical harmonic coefficients files and plot the gravity field.
3. To limit the resolution of the gravity field such that processing time is reduced, and low resolution estimates are removed

## Background and Innovation
Water monitoring is an essential task for water management, and understanding the effects of global warming on the polar and glaciated regions of the planet. One technique that can be used to monitor water movement is the production of a temporal gravity field. To generate the temporal gravity field, we need to first have an understanding of the static gravity field.

A spherical harmonic solution is a mathematical function that can be used to display a gravity field. The resolution of the gravity field will depend predominantly on the "degree" of the spherical harmonic coefficients. One popular format for storing spherical harmonic coefficients is within a .gfc file. There are however two main issues with using such files. The first is that it can be difficult to find the spherical harmonic degree of the model. This means if the coefficients of an unknown model are processed, there is no way of knowing the resolution until the final plot is displayed. The second issue is that processing spherical harmonic coefficients can be a computationally time consuming process.

## Resources and Timeline
The Internation Centre for Global Earth Models (ICGEM) has a catalogue of gravity field models all based upon spherical harmonics. Each model comes with a downloadable file of spherical harmonic coefficients that can be used to plot up the gravity field. To do so in python we make use of the 'pyshtools' package.

I will be accessing a number of files for different models, and utilising the pyshtools package so that I can generate estimates of the gravity field based upon the coefficients included in each file.

This project is related to my honours project, in which I have generated estimates of the temporal gravity field using a different technique. This project will give me a better understanding of the alternative methods to estimate a gravity field.

## Testing, Validation, and Documentation
The three functions each display different answers.
File_Size(), must output the spherical harmonic degree, and a rough guide to the time it will take to process the coefficients.
Gravity_Field(), must process the coefficients from the input file, and generate an estimate of the gravity field, then save it as a .png
Gravity_Field_Limited(), must determine if the spherical harmonic degree lies within the bounds desired. The preset values are between degrees 200 and 2000. If the degree is within this range, the function must then process the coefficients from the input file, and generate an estimate of the gravity field, then save it as a .png\

These three functions achieve the three goals of the project, meeting the need for functions that can assess spherical harmonic degree from a .gfc file, compute a gravity field estimate from such a file, and compute a gravity field estimate from such a file above a certain resolution when computational power is limited.

These functions could later be built upon to show the difference between different spherical harmonic gravity field estimates.

