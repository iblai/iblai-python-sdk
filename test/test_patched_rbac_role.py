# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.patched_rbac_role import PatchedRbacRole

class TestPatchedRbacRole(unittest.TestCase):
    """PatchedRbacRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedRbacRole:
        """Test PatchedRbacRole
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedRbacRole`
        """
        model = PatchedRbacRole()
        if include_optional:
            return PatchedRbacRole(
                id = 56,
                name = '',
                platform = iblai.models.rbac_platform.RbacPlatform(
                    id = 56, 
                    key = '', 
                    name = '', ),
                platform_key = '',
                actions = [
                    ''
                    ]
            )
        else:
            return PatchedRbacRole(
        )
        """

    def testPatchedRbacRole(self):
        """Test PatchedRbacRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
