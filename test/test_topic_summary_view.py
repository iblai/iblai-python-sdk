# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.topic_summary_view import TopicSummaryView

class TestTopicSummaryView(unittest.TestCase):
    """TopicSummaryView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TopicSummaryView:
        """Test TopicSummaryView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TopicSummaryView`
        """
        model = TopicSummaryView()
        if include_optional:
            return TopicSummaryView(
                total_topics = 56,
                topics_summary = [
                    iblai.models.topic_conversation.TopicConversation(
                        topic = '', 
                        conversation_count = 56, )
                    ]
            )
        else:
            return TopicSummaryView(
                total_topics = 56,
                topics_summary = [
                    iblai.models.topic_conversation.TopicConversation(
                        topic = '', 
                        conversation_count = 56, )
                    ],
        )
        """

    def testTopicSummaryView(self):
        """Test TopicSummaryView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
