# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.catalog_auto_increment_update_request import CatalogAutoIncrementUpdateRequest

class TestCatalogAutoIncrementUpdateRequest(unittest.TestCase):
    """CatalogAutoIncrementUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CatalogAutoIncrementUpdateRequest:
        """Test CatalogAutoIncrementUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CatalogAutoIncrementUpdateRequest`
        """
        model = CatalogAutoIncrementUpdateRequest()
        if include_optional:
            return CatalogAutoIncrementUpdateRequest(
                key = '',
                org = '',
                number_type = ''
            )
        else:
            return CatalogAutoIncrementUpdateRequest(
                number_type = '',
        )
        """

    def testCatalogAutoIncrementUpdateRequest(self):
        """Test CatalogAutoIncrementUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
