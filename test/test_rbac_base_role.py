# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.rbac_base_role import RbacBaseRole

class TestRbacBaseRole(unittest.TestCase):
    """RbacBaseRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RbacBaseRole:
        """Test RbacBaseRole
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RbacBaseRole`
        """
        model = RbacBaseRole()
        if include_optional:
            return RbacBaseRole(
                id = 56,
                name = '',
                platform_key = '',
                actions = [
                    ''
                    ]
            )
        else:
            return RbacBaseRole(
                id = 56,
                name = '',
                platform_key = '',
                actions = [
                    ''
                    ],
        )
        """

    def testRbacBaseRole(self):
        """Test RbacBaseRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
