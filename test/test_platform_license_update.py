# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.platform_license_update import PlatformLicenseUpdate

class TestPlatformLicenseUpdate(unittest.TestCase):
    """PlatformLicenseUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformLicenseUpdate:
        """Test PlatformLicenseUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformLicenseUpdate`
        """
        model = PlatformLicenseUpdate()
        if include_optional:
            return PlatformLicenseUpdate(
                license_id = 56,
                external_id = '',
                platform_key = '',
                platform_org = '',
                name = '',
                count = 56,
                started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                active = True,
                metadata = {
                    'key' : null
                    },
                source = '',
                transaction_id = '',
                change_type = 'update'
            )
        else:
            return PlatformLicenseUpdate(
        )
        """

    def testPlatformLicenseUpdate(self):
        """Test PlatformLicenseUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
