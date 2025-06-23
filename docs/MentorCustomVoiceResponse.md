# MentorCustomVoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_provider** | **str** |  | [readonly] 
**voice_name** | **str** |  | [readonly] 

## Example

```python
from iblai.models.mentor_custom_voice_response import MentorCustomVoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCustomVoiceResponse from a JSON string
mentor_custom_voice_response_instance = MentorCustomVoiceResponse.from_json(json)
# print the JSON string representation of the object
print(MentorCustomVoiceResponse.to_json())

# convert the object into a dict
mentor_custom_voice_response_dict = mentor_custom_voice_response_instance.to_dict()
# create an instance of MentorCustomVoiceResponse from a dict
mentor_custom_voice_response_from_dict = MentorCustomVoiceResponse.from_dict(mentor_custom_voice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


