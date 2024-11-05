# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.chat_session_with_message import ChatSessionWithMessage

class TestChatSessionWithMessage(unittest.TestCase):
    """ChatSessionWithMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatSessionWithMessage:
        """Test ChatSessionWithMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatSessionWithMessage`
        """
        model = ChatSessionWithMessage()
        if include_optional:
            return ChatSessionWithMessage(
                session_id = '',
                mentor = iblai.models.chartsession_mentor.ChartsessionMentor(
                    name = '', 
                    mentor_tenant = '', 
                    description = '', 
                    profile_image = '', 
                    created_by = '', 
                    unique_id = '', 
                    proactive_prompt = '', ),
                messages_count = 56,
                messages = [
                    iblai.models.chat_history.ChatHistory(
                        id = 56, 
                        message = null, 
                        inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        title = '', 
                        feedback = null, 
                        document_sources = null, )
                    ]
            )
        else:
            return ChatSessionWithMessage(
                session_id = '',
                mentor = iblai.models.chartsession_mentor.ChartsessionMentor(
                    name = '', 
                    mentor_tenant = '', 
                    description = '', 
                    profile_image = '', 
                    created_by = '', 
                    unique_id = '', 
                    proactive_prompt = '', ),
                messages_count = 56,
                messages = [
                    iblai.models.chat_history.ChatHistory(
                        id = 56, 
                        message = null, 
                        inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        title = '', 
                        feedback = null, 
                        document_sources = null, )
                    ],
        )
        """

    def testChatSessionWithMessage(self):
        """Test ChatSessionWithMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
