# DesiredSkillCreateUpdateRequest

Serializer for desired skill creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**username** | **str** | Username | [optional] 
**skills** | **List[Dict[str, object]]** | List of skills (can be skill IDs or objects with name, platform_key, etc.) | 
**data** | **object** | Additional data | [optional] 

## Example

```python
from iblai.models.desired_skill_create_update_request import DesiredSkillCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredSkillCreateUpdateRequest from a JSON string
desired_skill_create_update_request_instance = DesiredSkillCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DesiredSkillCreateUpdateRequest.to_json())

# convert the object into a dict
desired_skill_create_update_request_dict = desired_skill_create_update_request_instance.to_dict()
# create an instance of DesiredSkillCreateUpdateRequest from a dict
desired_skill_create_update_request_from_dict = DesiredSkillCreateUpdateRequest.from_dict(desired_skill_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


