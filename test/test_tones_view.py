# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.tones_view import TonesView

class TestTonesView(unittest.TestCase):
    """TonesView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TonesView:
        """Test TonesView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TonesView`
        """
        model = TonesView()
        if include_optional:
            return TonesView(
                id = 56,
                description = ''
            )
        else:
            return TonesView(
                id = 56,
        )
        """

    def testTonesView(self):
        """Test TonesView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()