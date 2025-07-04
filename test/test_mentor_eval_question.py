# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.mentor_eval_question import MentorEvalQuestion

class TestMentorEvalQuestion(unittest.TestCase):
    """MentorEvalQuestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentorEvalQuestion:
        """Test MentorEvalQuestion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentorEvalQuestion`
        """
        model = MentorEvalQuestion()
        if include_optional:
            return MentorEvalQuestion(
                id = 56,
                content = '',
                sample_answer = ''
            )
        else:
            return MentorEvalQuestion(
                id = 56,
                content = '',
        )
        """

    def testMentorEvalQuestion(self):
        """Test MentorEvalQuestion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
