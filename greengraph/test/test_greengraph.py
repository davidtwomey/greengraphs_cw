import yaml
import os
import numpy as np

from ..greengrapher import Greengraph
from nose.tools import assert_raises, assert_equal, assert_almost_equal



# Test Greengraph(object) class initialisation
def test_Greengraph():
	"""Tests the initialisation of Greengraph"""
	mygraph = Greengraph('London','Oxford')
	assert_equal(mygraph.start, 'London')
	assert_equal(mygraph.end, 'Oxford')
	
# Test Greengraph(object) class method geolocate
def test_geolocate_valid():
	with open(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
		fixtures =yaml.load(fixture_file)['geolocate']
	for fix in fixtures
		location = fix.pop('location')
		anslat = fix.pop('ans_lat')
		anslong = fix.pop('ans_long')
		answer = (ans_lat, ans_long)
		geo = Greengraph(0.0, 0.0)
		assert_equal(geo.geolocate(location), answer)

# Test Greengraph(object) class method location_sequence
def test_location_sequence():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
		fixtures = yaml.load(fixture_file)['location_sequence']
	for fix in fixtures:
		start = fix.pop('start')
		end = fix.pop('end')
		steps = fix.pop('steps')
		answer = fix.pop('answer')
		geo = Greengraph(0.0, 0.0)
		return_val = geo.location_sequence(geo.geolocate(start), geo.geolocate(end), steps)
		answer = np.vstack(answer)
		assert(np.array_equal(return_val, answer))
		
