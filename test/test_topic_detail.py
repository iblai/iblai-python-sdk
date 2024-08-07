# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.topic_detail import TopicDetail

class TestTopicDetail(unittest.TestCase):
    """TopicDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TopicDetail:
        """Test TopicDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TopicDetail`
        """
        model = TopicDetail()
        if include_optional:
            return TopicDetail(
                id = 56,
                total_topics = 56,
                number_of_messages = 56,
                number_of_conversations = 56,
                user_sentiment = '',
                user_ratings = '',
                name = '',
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                platform = 56
            )
        else:
            return TopicDetail(
                id = 56,
                total_topics = 56,
                number_of_messages = 56,
                number_of_conversations = 56,
                user_sentiment = '',
                user_ratings = '',
                name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testTopicDetail(self):
        """Test TopicDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
