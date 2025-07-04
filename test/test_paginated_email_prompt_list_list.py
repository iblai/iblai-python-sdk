# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_email_prompt_list_list import PaginatedEmailPromptListList

class TestPaginatedEmailPromptListList(unittest.TestCase):
    """PaginatedEmailPromptListList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedEmailPromptListList:
        """Test PaginatedEmailPromptListList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedEmailPromptListList`
        """
        model = PaginatedEmailPromptListList()
        if include_optional:
            return PaginatedEmailPromptListList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.email_prompt_list.EmailPromptList(
                        id = 56, 
                        sender_email = '', 
                        sender_name = '', 
                        subject = '', 
                        content_summary = '', 
                        mentor_name = '', 
                        mentor_email = '', 
                        is_processed = True, 
                        inserted_at = '', )
                    ]
            )
        else:
            return PaginatedEmailPromptListList(
                count = 123,
                results = [
                    iblai.models.email_prompt_list.EmailPromptList(
                        id = 56, 
                        sender_email = '', 
                        sender_name = '', 
                        subject = '', 
                        content_summary = '', 
                        mentor_name = '', 
                        mentor_email = '', 
                        is_processed = True, 
                        inserted_at = '', )
                    ],
        )
        """

    def testPaginatedEmailPromptListList(self):
        """Test PaginatedEmailPromptListList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
