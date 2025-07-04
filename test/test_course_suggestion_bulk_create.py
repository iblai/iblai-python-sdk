# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_suggestion_bulk_create import CourseSuggestionBulkCreate

class TestCourseSuggestionBulkCreate(unittest.TestCase):
    """CourseSuggestionBulkCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseSuggestionBulkCreate:
        """Test CourseSuggestionBulkCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseSuggestionBulkCreate`
        """
        model = CourseSuggestionBulkCreate()
        if include_optional:
            return CourseSuggestionBulkCreate(
                platform_key = '',
                suggestion_data = [
                    {
                        'key' : null
                        }
                    ],
                department_mode = True
            )
        else:
            return CourseSuggestionBulkCreate(
                platform_key = '',
                suggestion_data = [
                    {
                        'key' : null
                        }
                    ],
        )
        """

    def testCourseSuggestionBulkCreate(self):
        """Test CourseSuggestionBulkCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
