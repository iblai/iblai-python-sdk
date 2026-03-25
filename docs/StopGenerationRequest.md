# StopGenerationRequest

Serializer for stop generation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation_id** | **str** | The unique identifier of the generation to stop | 

## Example

```python
from iblai.models.stop_generation_request import StopGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopGenerationRequest from a JSON string
stop_generation_request_instance = StopGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(StopGenerationRequest.to_json())

# convert the object into a dict
stop_generation_request_dict = stop_generation_request_instance.to_dict()
# create an instance of StopGenerationRequest from a dict
stop_generation_request_from_dict = StopGenerationRequest.from_dict(stop_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


