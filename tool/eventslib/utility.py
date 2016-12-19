import re


class Utility(object):
    @classmethod
    def target_date_is_valid(cls, start_date):
        """ Tests date stamp for validity """
        canary = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        if canary.match(start_date):
            return True
        else:
            return False
