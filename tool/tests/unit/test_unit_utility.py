import imp
import os
import sys

module_name = 'eventslib'
here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
eventslib = imp.load_module(module_name, fp, pathname, description)


class TestUnitUtility:
    def test_unit_utility_target_date_is_valid(self):
        assert eventslib.Utility.target_date_is_valid('2016-12-01')

    def test_unit_utility_target_date_is_valid_false(self):
        assert not eventslib.Utility.target_date_is_valid('2016-12-01-12:01')
