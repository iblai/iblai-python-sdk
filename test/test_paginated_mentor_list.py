# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_mentor_list import PaginatedMentorList

class TestPaginatedMentorList(unittest.TestCase):
    """PaginatedMentorList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedMentorList:
        """Test PaginatedMentorList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedMentorList`
        """
        model = PaginatedMentorList()
        if include_optional:
            return PaginatedMentorList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.mentor.Mentor(
                        name = '', 
                        unique_id = '', 
                        flow = null, 
                        slug = 'z', 
                        platform = '', 
                        allow_anonymous = True, 
                        metadata = null, 
                        enable_moderation = True, 
                        is_proactive = True, 
                        proactive_prompt = '', 
                        moderation_system_prompt = '', 
                        moderation_response = '', 
                        proactive_message = '', 
                        created_by = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedMentorList(
        )
        """

    def testPaginatedMentorList(self):
        """Test PaginatedMentorList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
