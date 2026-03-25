# ReportedSkillCreateUpdateRequest

Serializer for reported skill creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**username** | **str** | Username | [optional] 
**skills** | **List[Dict[str, object]]** | List of skills (can be skill IDs or objects with name, platform_key, etc.) | 
**data** | **object** | Additional data | [optional] 

## Example

```python
from iblai.models.reported_skill_create_update_request import ReportedSkillCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportedSkillCreateUpdateRequest from a JSON string
reported_skill_create_update_request_instance = ReportedSkillCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportedSkillCreateUpdateRequest.to_json())

# convert the object into a dict
reported_skill_create_update_request_dict = reported_skill_create_update_request_instance.to_dict()
# create an instance of ReportedSkillCreateUpdateRequest from a dict
reported_skill_create_update_request_from_dict = ReportedSkillCreateUpdateRequest.from_dict(reported_skill_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


