# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_platform_public_metadata import PatchedPlatformPublicMetadata

class TestPatchedPlatformPublicMetadata(unittest.TestCase):
    """PatchedPlatformPublicMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedPlatformPublicMetadata:
        """Test PatchedPlatformPublicMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedPlatformPublicMetadata`
        """
        model = PatchedPlatformPublicMetadata()
        if include_optional:
            return PatchedPlatformPublicMetadata(
                platform_key = '',
                platform_name = '',
                metadata = None,
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PatchedPlatformPublicMetadata(
        )
        """

    def testPatchedPlatformPublicMetadata(self):
        """Test PatchedPlatformPublicMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
