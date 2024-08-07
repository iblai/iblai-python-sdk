# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.per_learner_last_access import PerLearnerLastAccess

class TestPerLearnerLastAccess(unittest.TestCase):
    """PerLearnerLastAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerLearnerLastAccess:
        """Test PerLearnerLastAccess
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerLearnerLastAccess`
        """
        model = PerLearnerLastAccess()
        if include_optional:
            return PerLearnerLastAccess(
                data = iblai.models.per_learner_last_access_data.PerLearnerLastAccessData(
                    course_last_accessed = null, 
                    last_accessed = '', )
            )
        else:
            return PerLearnerLastAccess(
        )
        """

    def testPerLearnerLastAccess(self):
        """Test PerLearnerLastAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
