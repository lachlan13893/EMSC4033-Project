from .dependencies import *
    
### Define Functions ###
def File_Size(input):
    '''A function to determine the spherical harmonic degree of the input,
         and assess whether the estimation will be quick or slow'''
    
    ### Read the Coefficients from the File ###
    Coefficients = pyshtools.SHGravCoeffs.from_file(input, format='icgem')
    print("Coefficient File:", input)
    print("Degree =", Coefficients.lmax)

    ### Insert print statements to display degree and whether the estimate will be quick or slow ###
    if Coefficients.lmax > 2000:
        print("Spherical Harmonic degree is Very Large. Estimate will take a long time")
    if 1000 < Coefficients.lmax < 2000:
        print("Spherical Harmonic degree is Large. Estimate will take a some time")
    if 200 < Coefficients.lmax < 1000:
        print("Spherical Harmonic degree is Moderate. Estimate will be reasonably quick")
    if Coefficients.lmax < 200:
        print("Spherical Harmonic degree is Small. Estimate will take be very quick")

def Gravity_Field(input):
    '''A function to generate the gravity field estimate from the input file coefficients'''
    
    ### Based Upon Resolution or Specific named file, Select input ###
    resolution = input
    input_file = resolution
    if resolution == 'Low':
        input_file = 'GEMT2.gfc'
    if resolution == 'Moderate':
        input_file = 'GOCO06s.gfc'
    if resolution == 'High':
        input_file = 'EIGEN6C2.gfc'
    if resolution == 'Very High':
        input_file = 'XGM2019e_2159.gfc'
        

    ### Insert Time Warning for Higher Resolutions ###
    if resolution == 'Very High' or resolution == 'High':
        print("Please Wait. You have selected a higher resolution estimate. This may take some time")

    ### Read the Coefficients from the File ###
    Coefficients = pyshtools.SHGravCoeffs.from_file(input, format='icgem')
    #print("Coefficient File:", input)
    #print("Degree =", Coefficients.lmax)


    ### Define Figure Size ###
    pyshtools.utils.figstyle(rel_width=2.5)

    ### Expand the Coefficient File and Plot the Gravity Field ###
    Expand_Coefficients = Coefficients.expand(lmax=Coefficients.lmax)
    Gravity_Field = Expand_Coefficients.plot_phi(cmap='RdBu_r', cb_label='Anomaly (Gal)', grid=True, 
                        title=input, xlabel='Longitude', ylabel='Latitude', cmap_limits=[-0.0022,0.0022], show=False)
    
    ### Save Image ###
    plt.savefig("Gravity_Field.png", dpi=600, num=1)

def Gravity_Field_Limited(input):
    '''A function to generate the gravity field estimate from the input file coefficients.
       However, files that have a high spherical harmonic degree or a low resolution will not generate an estimate'''
    ### Based Upon Resolution or Specific named file, Select input ###
    resolution = input
    input_file = resolution
    if resolution == 'Low':
        input_file = 'GEMT2.gfc'
    if resolution == 'Moderate':
        input_file = 'GOCO06s.gfc'
    if resolution == 'High':
        input_file = 'EIGEN6C2.gfc'
    if resolution == 'Very High':
        input_file = 'XGM2019e_2159.gfc'
        
    ### Read the Coefficients from the File ###
    Coefficients = pyshtools.SHGravCoeffs.from_file(input, format='icgem')
    #print("Coefficient File:", input)
    #print("Degree =", Coefficients.lmax)

    ### Insert Assertion tests to remove files that are too small or too large ###
    if Coefficients.lmax > 2000:
        print("Spherical Harmonic degree is too large")
        
    elif Coefficients.lmax < 200:
        print("Spherical Harmonic degree is too small")
    
    else:
        ### Define Figure Size ###
        pyshtools.utils.figstyle(rel_width=2.5)

        ### Expand the Coefficient File and Plot the Gravity Field ###
        Expand_Coefficients = Coefficients.expand(lmax=Coefficients.lmax)
        Gravity_Field = Expand_Coefficients.plot_phi(cmap='RdBu_r', cb_label='Anomaly (Gal)', grid=True, 
                            title=input, xlabel='Longitude', ylabel='Latitude', cmap_limits=[-0.0022,0.0022], show=False)

        ### Save Image ###
        plt.savefig("Gravity_Field.png", dpi=600, num=2)