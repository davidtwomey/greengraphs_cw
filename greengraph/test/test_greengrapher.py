from ..greengrapher import Greengraph

from nose.tools import assert_raises, assert_equal

# Test greengraph(object) class initialisation
def test_Greengraph():
	mygraph = Greengraph('London','Oxford')
	assert_equal(mygraph.start, 'London')
	assert_equal(mygraph.end, 'Oxford')
	
