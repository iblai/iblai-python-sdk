# EdxSignalReceiverRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | **object** |  | 

## Example

```python
from iblai.models.edx_signal_receiver_request import EdxSignalReceiverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EdxSignalReceiverRequest from a JSON string
edx_signal_receiver_request_instance = EdxSignalReceiverRequest.from_json(json)
# print the JSON string representation of the object
print(EdxSignalReceiverRequest.to_json())

# convert the object into a dict
edx_signal_receiver_request_dict = edx_signal_receiver_request_instance.to_dict()
# create an instance of EdxSignalReceiverRequest from a dict
edx_signal_receiver_request_from_dict = EdxSignalReceiverRequest.from_dict(edx_signal_receiver_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


