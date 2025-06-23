# MentorMemorySettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | [optional] 
**item_identifier** | **str** |  | [optional] 
**learner_advance_correct_rate** | **float** |  | [optional] 
**learner_advance_question_count** | **int** |  | [optional] 

## Example

```python
from iblai.models.mentor_memory_settings_request import MentorMemorySettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorMemorySettingsRequest from a JSON string
mentor_memory_settings_request_instance = MentorMemorySettingsRequest.from_json(json)
# print the JSON string representation of the object
print(MentorMemorySettingsRequest.to_json())

# convert the object into a dict
mentor_memory_settings_request_dict = mentor_memory_settings_request_instance.to_dict()
# create an instance of MentorMemorySettingsRequest from a dict
mentor_memory_settings_request_from_dict = MentorMemorySettingsRequest.from_dict(mentor_memory_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


