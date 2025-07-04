# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.document_settings_response import DocumentSettingsResponse

class TestDocumentSettingsResponse(unittest.TestCase):
    """DocumentSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSettingsResponse:
        """Test DocumentSettingsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSettingsResponse`
        """
        model = DocumentSettingsResponse()
        if include_optional:
            return DocumentSettingsResponse(
                retrain_interval_days = 56
            )
        else:
            return DocumentSettingsResponse(
        )
        """

    def testDocumentSettingsResponse(self):
        """Test DocumentSettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
