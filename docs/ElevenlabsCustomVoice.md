# ElevenlabsCustomVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**files** | **List[str]** |  | 

## Example

```python
from iblai.models.elevenlabs_custom_voice import ElevenlabsCustomVoice

# TODO update the JSON string below
json = "{}"
# create an instance of ElevenlabsCustomVoice from a JSON string
elevenlabs_custom_voice_instance = ElevenlabsCustomVoice.from_json(json)
# print the JSON string representation of the object
print(ElevenlabsCustomVoice.to_json())

# convert the object into a dict
elevenlabs_custom_voice_dict = elevenlabs_custom_voice_instance.to_dict()
# create an instance of ElevenlabsCustomVoice from a dict
elevenlabs_custom_voice_from_dict = ElevenlabsCustomVoice.from_dict(elevenlabs_custom_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


