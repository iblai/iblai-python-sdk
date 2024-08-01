# AudioToTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** |  | 

## Example

```python
from iblai.models.audio_to_text_request import AudioToTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AudioToTextRequest from a JSON string
audio_to_text_request_instance = AudioToTextRequest.from_json(json)
# print the JSON string representation of the object
print(AudioToTextRequest.to_json())

# convert the object into a dict
audio_to_text_request_dict = audio_to_text_request_instance.to_dict()
# create an instance of AudioToTextRequest from a dict
audio_to_text_request_from_dict = AudioToTextRequest.from_dict(audio_to_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


