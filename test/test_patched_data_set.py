# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_data_set import PatchedDataSet

class TestPatchedDataSet(unittest.TestCase):
    """PatchedDataSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedDataSet:
        """Test PatchedDataSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedDataSet`
        """
        model = PatchedDataSet()
        if include_optional:
            return PatchedDataSet(
                id = '',
                platform = {
                    'key' : null
                    },
                name = '',
                prompt = '',
                source_url = '',
                source_file = '',
                status = 'pending',
                num_data_points = 56,
                train_split = 0,
                train_file = '',
                test_file = '',
                retry_attempts = 56,
                error_log = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PatchedDataSet(
        )
        """

    def testPatchedDataSet(self):
        """Test PatchedDataSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
