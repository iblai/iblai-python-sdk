# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.question_request import QuestionRequest

class TestQuestionRequest(unittest.TestCase):
    """QuestionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuestionRequest:
        """Test QuestionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuestionRequest`
        """
        model = QuestionRequest()
        if include_optional:
            return QuestionRequest(
                username = '',
                initial_questions = [
                    iblai.models.input_question.InputQuestion(
                        text = '', 
                        difficulty_level = 1, 
                        possible_answers = [
                            iblai.models.intial_question_answer.IntialQuestionAnswer(
                                text = '', )
                            ], )
                    ],
                question_count = 56,
                subject = ''
            )
        else:
            return QuestionRequest(
                username = '',
                initial_questions = [
                    iblai.models.input_question.InputQuestion(
                        text = '', 
                        difficulty_level = 1, 
                        possible_answers = [
                            iblai.models.intial_question_answer.IntialQuestionAnswer(
                                text = '', )
                            ], )
                    ],
                subject = '',
        )
        """

    def testQuestionRequest(self):
        """Test QuestionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
