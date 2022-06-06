import pytest
from Code.dependencies import *
from Code.my_functions import *


def test_File_Size_Function():
    result = File_Size('Files/GEMT2.gfc')
    assert result != 50, " Function returns incorrect size"

def test_Gravity_Field_Function():
    result = Gravity_Field('Files/GEMT2.gfc')
    assert result != plt.fignum_exists(1), "Gravity field estimate not generated"

def test_Gravity_Field_Limited_Function():
    result = Gravity_Field_Limited('Files/GEMT2.gfc')
    grav_field = Gravity_Field('Files/GEMT2.gfc')
    assert result == grav_field, "Function has incorrectly determined spherical harmonic degree as out of bounds"