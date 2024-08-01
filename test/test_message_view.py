# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.message_view import MessageView

class TestMessageView(unittest.TestCase):
    """MessageView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageView:
        """Test MessageView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageView`
        """
        model = MessageView()
        if include_optional:
            return MessageView(
                count = 56,
                title = '',
                proactive_prompt = '',
                mentor_unique_id = '',
                previous = '',
                next = '',
                results = [
                    null
                    ]
            )
        else:
            return MessageView(
                count = 56,
                title = '',
                proactive_prompt = '',
                mentor_unique_id = '',
                previous = '',
                next = '',
                results = [
                    null
                    ],
        )
        """

    def testMessageView(self):
        """Test MessageView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
