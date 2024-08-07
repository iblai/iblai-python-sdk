# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.user_catalog_item_memory_view import UserCatalogItemMemoryView

class TestUserCatalogItemMemoryView(unittest.TestCase):
    """UserCatalogItemMemoryView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCatalogItemMemoryView:
        """Test UserCatalogItemMemoryView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCatalogItemMemoryView`
        """
        model = UserCatalogItemMemoryView()
        if include_optional:
            return UserCatalogItemMemoryView(
                id = 56,
                student = '',
                platform = '',
                catalog_item = '',
                lessons = None,
                next_steps = None
            )
        else:
            return UserCatalogItemMemoryView(
                id = 56,
                student = '',
                platform = '',
        )
        """

    def testUserCatalogItemMemoryView(self):
        """Test UserCatalogItemMemoryView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
