# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.chat_history_session_id import ChatHistorySessionId

class TestChatHistorySessionId(unittest.TestCase):
    """ChatHistorySessionId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatHistorySessionId:
        """Test ChatHistorySessionId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatHistorySessionId`
        """
        model = ChatHistorySessionId()
        if include_optional:
            return ChatHistorySessionId(
                id = ''
            )
        else:
            return ChatHistorySessionId(
                id = '',
        )
        """

    def testChatHistorySessionId(self):
        """Test ChatHistorySessionId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
