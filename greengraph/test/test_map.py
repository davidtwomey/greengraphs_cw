import yaml
import os
import numpy as np
import StringIO
import mock
import requests

from mock import patch
from matplotlib import image as im

from ..greengraph import Greengraph
from ..map import Map
from nose.tools import assert_equal, assert_false, assert_raises


# Test Map(object) class initialisation
@patch('requests.get')
@patch('matplotlib.image.imread')
def test_map(mock_imread,mock_get):
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_map.yaml')) as fixture_file:
		fixtures = yaml.load(fixture_file)['init']
		for fix in fixtures:
			lat = fix.pop('lat')
			long = fix.pop('long')
			url = fix.pop('url')
			map = Map(lat,long)
			param = fix.pop('params')
			mock_get.assert_called_with(url,params=param)

#Test Map(object) class method green()	
@patch('requests.get')
@patch('matplotlib.image.imread')
def test_green(mock_imread,mock_get):
    with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_map.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_green']        
        pixel_dim = 400 #standardised for this test
        pixel_array = np.zeros((pixel_dim, pixel_dim, 3))
        mock_map = Map(51.,1.)

        for fixture in fixtures:
            threshold = fixture.pop('threshold')
            colour = fixture.pop('pixel_colour')
            
            if(colour == "green"):
                pixel_array[:,:,1] = 1
                mock_map.__setattr__('pixels',pixel_array)
                assert(mock_map.green(threshold).all())
            elif(colour == "red"):
                pixel_array[:,:,0] = 1
                mock_map.__setattr__('pixels',pixel_array)
                assert_equal(mock_map.green(threshold).all(),False)
            elif(colour == "blue"):
                pixel_array[:,:,2] = 1
                mock_map.__setattr__('pixels',pixel_array)
                assert_equal(mock_map.green(threshold).all(),False)
            
#Test Map(object) class	method count_green()
@patch('requests.get')
@patch('matplotlib.image.imread')
def test_count_green(mock_imread,mock_get):
    mock_map = Map(20.,15.)
    for px in range(1,100):
        pixels = ([[0.,1.,0.]] * px) + ([[1.,1.,1.]] * (100-px))
        pixels = np.array(pixels, dtype='float32')
        pixels = pixels.reshape(10,10,3)
        mock_map.pixels = pixels
        assert_equal(mock_map.count_green(), px)

#Test Map(object) class method show_green()
#@mock.patch.object(requests,'get')
#@mock.patch.object(im,'imread')
#@mock.patch.object(im,'imsave')
@patch('requests.get')
@patch('matplotlib.image.imread')
@patch('matplotlib.image.imsave')
def test_show_green(mock_imsave,mock_imread,mock_get):
    MockMap = Map(20.123,15.123)
    for px in range(1,100): 
        pixels = ([[0,1,0]] * px) + ([[0,0,0]] * (100-px))
        pixels = np.array(pixels)
        pixels = pixels.reshape(10,10,3)
        MockMap.pixels = pixels
        MockMap.show_green()
        assert np.array_equal(mock_imsave.call_args[0][1],pixels)
    assert_equal(mock_imsave.call_args[1], {'format':'png'})






