# MentorCustomVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_provider** | **str** |  | 
**voice_name** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_custom_voice import MentorCustomVoice

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCustomVoice from a JSON string
mentor_custom_voice_instance = MentorCustomVoice.from_json(json)
# print the JSON string representation of the object
print(MentorCustomVoice.to_json())

# convert the object into a dict
mentor_custom_voice_dict = mentor_custom_voice_instance.to_dict()
# create an instance of MentorCustomVoice from a dict
mentor_custom_voice_from_dict = MentorCustomVoice.from_dict(mentor_custom_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


