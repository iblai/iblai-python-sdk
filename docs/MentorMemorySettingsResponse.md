# MentorMemorySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | [readonly] 
**item_identifier** | **str** |  | [readonly] 
**learner_advance_correct_rate** | **float** |  | [optional] 
**learner_advance_question_count** | **int** |  | [optional] 

## Example

```python
from iblai.models.mentor_memory_settings_response import MentorMemorySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentorMemorySettingsResponse from a JSON string
mentor_memory_settings_response_instance = MentorMemorySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(MentorMemorySettingsResponse.to_json())

# convert the object into a dict
mentor_memory_settings_response_dict = mentor_memory_settings_response_instance.to_dict()
# create an instance of MentorMemorySettingsResponse from a dict
mentor_memory_settings_response_from_dict = MentorMemorySettingsResponse.from_dict(mentor_memory_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


