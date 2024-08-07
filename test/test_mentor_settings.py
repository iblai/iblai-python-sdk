# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.mentor_settings import MentorSettings

class TestMentorSettings(unittest.TestCase):
    """MentorSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MentorSettings:
        """Test MentorSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MentorSettings`
        """
        model = MentorSettings()
        if include_optional:
            return MentorSettings(
                id = 56,
                display_name = '',
                profile_image = '',
                initial_message = '',
                suggested_message = '',
                theme = 'dark',
                user_message_color = '',
                mentor_bubble_color = '',
                align_mentor_bubble = 'left',
                mentor = '',
                mentor_slug = '',
                mentor_unique_id = '',
                metadata = '',
                mentor_visibility = None,
                enable_image_generation = True,
                enable_web_browsing = True,
                enable_code_interpreter = True,
                custom_css = '',
                allow_anonymous = '',
                mentor_description = '',
                suggested_prompts = '',
                proactive_message = '',
                mentor_tools = '',
                can_use_tools = '',
                llm_temperature = '',
                llm_provider = '',
                llm_name = '',
                proactive_prompt = ''
            )
        else:
            return MentorSettings(
                id = 56,
                mentor = '',
                mentor_slug = '',
                mentor_unique_id = '',
                metadata = '',
                allow_anonymous = '',
                mentor_description = '',
                suggested_prompts = '',
                proactive_message = '',
                mentor_tools = '',
                can_use_tools = '',
                llm_temperature = '',
                llm_provider = '',
                llm_name = '',
                proactive_prompt = '',
        )
        """

    def testMentorSettings(self):
        """Test MentorSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
