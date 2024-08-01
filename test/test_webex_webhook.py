# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.webex_webhook import WebexWebhook

class TestWebexWebhook(unittest.TestCase):
    """WebexWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebexWebhook:
        """Test WebexWebhook
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebexWebhook`
        """
        model = WebexWebhook()
        if include_optional:
            return WebexWebhook(
                data = {
                    'key' : null
                    },
                resource = ''
            )
        else:
            return WebexWebhook(
                data = {
                    'key' : null
                    },
                resource = '',
        )
        """

    def testWebexWebhook(self):
        """Test WebexWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
