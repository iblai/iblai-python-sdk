# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_periodic_agent_list import PaginatedPeriodicAgentList

class TestPaginatedPeriodicAgentList(unittest.TestCase):
    """PaginatedPeriodicAgentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPeriodicAgentList:
        """Test PaginatedPeriodicAgentList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPeriodicAgentList`
        """
        model = PaginatedPeriodicAgentList()
        if include_optional:
            return PaginatedPeriodicAgentList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    iblai.models.periodic_agent.PeriodicAgent(
                        id = 56, 
                        mentor = iblai.models.mentor.Mentor(
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
                            safety_system_prompt = '', 
                            safety_response = '', 
                            enable_safety_system = True, 
                            proactive_message = '', 
                            created_by = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        title = '', 
                        username = '', 
                        description = '', 
                        prompt = '', 
                        task = iblai.models.periodic_task.PeriodicTask(
                            id = 56, 
                            name = '', 
                            crontab = iblai.models.crontab_schedule.CrontabSchedule(
                                minute = '', 
                                hour = '', 
                                day_of_week = '', 
                                day_of_month = '', 
                                month_of_year = '', ), 
                            one_off = True, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            enabled = True, ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        enabled = True, 
                        one_off = '', 
                        platform_key = '', 
                        pathway = '', 
                        callback_url = '', 
                        callback_secret = '', 
                        parent_session_id = '', 
                        parent_mentor_id = 56, 
                        previous_agent = 56, 
                        previous_agent_status = null, 
                        previous_agent_output = '', )
                    ]
            )
        else:
            return PaginatedPeriodicAgentList(
        )
        """

    def testPaginatedPeriodicAgentList(self):
        """Test PaginatedPeriodicAgentList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
