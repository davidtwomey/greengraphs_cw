import yaml
import os


from ..greengrapher import Greengraph
from nose.tools import assert_raises, assert_equal



# Test Greengraph(object) class initialisation
def test_Greengraph():
	"""Tests the initialisation of Greengraph"""
	mygraph = Greengraph('London','Oxford')
	assert_equal(mygraph.start, 'London')
	assert_equal(mygraph.end, 'Oxford')
	
# Test Greengraph class method geolocate
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
		
