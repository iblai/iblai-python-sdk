# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.rbac_group import RbacGroup

class TestRbacGroup(unittest.TestCase):
    """RbacGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RbacGroup:
        """Test RbacGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RbacGroup`
        """
        model = RbacGroup()
        if include_optional:
            return RbacGroup(
                id = 56,
                unique_id = '',
                platform = iblai.models.rbac_platform.RbacPlatform(
                    id = 56, 
                    key = '', 
                    name = '', ),
                platform_key = '',
                name = '',
                description = '',
                users = [
                    iblai.models.rbac_user.RbacUser(
                        id = 56, 
                        username = '', )
                    ],
                users_to_add = [
                    56
                    ],
                users_to_remove = [
                    56
                    ]
            )
        else:
            return RbacGroup(
                id = 56,
                unique_id = '',
                platform = iblai.models.rbac_platform.RbacPlatform(
                    id = 56, 
                    key = '', 
                    name = '', ),
                platform_key = '',
                users = [
                    iblai.models.rbac_user.RbacUser(
                        id = 56, 
                        username = '', )
                    ],
        )
        """

    def testRbacGroup(self):
        """Test RbacGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
