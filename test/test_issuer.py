# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.issuer import Issuer

class TestIssuer(unittest.TestCase):
    """Issuer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Issuer:
        """Test Issuer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Issuer`
        """
        model = Issuer()
        if include_optional:
            return Issuer(
                name = '',
                org = '',
                entity_id = '',
                signatories = {
                    'key' : ''
                    },
                url = '',
                icon_image = '',
                allowed_template_tags = None
            )
        else:
            return Issuer(
                name = '',
                org = '',
                entity_id = '',
                signatories = {
                    'key' : ''
                    },
                url = '',
                icon_image = '',
        )
        """

    def testIssuer(self):
        """Test Issuer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
