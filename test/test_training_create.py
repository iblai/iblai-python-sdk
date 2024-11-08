# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.training_create import TrainingCreate

class TestTrainingCreate(unittest.TestCase):
    """TrainingCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrainingCreate:
        """Test TrainingCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrainingCreate`
        """
        model = TrainingCreate()
        if include_optional:
            return TrainingCreate(
                id = '',
                project_name = '',
                dataset = '',
                base_model_name = '',
                provider = 'openai',
                text_column = '',
                learning_rate = 1.337,
                batch_size = 56,
                num_epochs = 56,
                block_size = 56,
                warmup_ratio = 1.337,
                lora_r = 56,
                lora_alpha = 56,
                lora_dropout = 1.337,
                weight_decay = 1.337,
                gradient_accumulation = 56,
                use_peft = True,
                use_fp16 = True,
                use_int4 = True,
                push_to_hub = True,
                repo_id = '',
                preprocess_dataset = True,
                prompt_column = '',
                prompt_prefix = '',
                prompt_suffix = '',
                response_prefix = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return TrainingCreate(
                id = '',
                project_name = '',
                dataset = '',
                base_model_name = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testTrainingCreate(self):
        """Test TrainingCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
