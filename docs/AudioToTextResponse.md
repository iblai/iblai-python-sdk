# AudioToTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from iblai.models.audio_to_text_response import AudioToTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AudioToTextResponse from a JSON string
audio_to_text_response_instance = AudioToTextResponse.from_json(json)
# print the JSON string representation of the object
print(AudioToTextResponse.to_json())

# convert the object into a dict
audio_to_text_response_dict = audio_to_text_response_instance.to_dict()
# create an instance of AudioToTextResponse from a dict
audio_to_text_response_from_dict = AudioToTextResponse.from_dict(audio_to_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


