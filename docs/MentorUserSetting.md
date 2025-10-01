# MentorUserSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_saved_memories** | **bool** |  | [optional] 

## Example

```python
from iblai.models.mentor_user_setting import MentorUserSetting

# TODO update the JSON string below
json = "{}"
# create an instance of MentorUserSetting from a JSON string
mentor_user_setting_instance = MentorUserSetting.from_json(json)
# print the JSON string representation of the object
print(MentorUserSetting.to_json())

# convert the object into a dict
mentor_user_setting_dict = mentor_user_setting_instance.to_dict()
# create an instance of MentorUserSetting from a dict
mentor_user_setting_from_dict = MentorUserSetting.from_dict(mentor_user_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


