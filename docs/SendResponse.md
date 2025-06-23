# SendResponse

Response serializer for send notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**notifications_sent** | **int** |  | 
**build_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from iblai.models.send_response import SendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendResponse from a JSON string
send_response_instance = SendResponse.from_json(json)
# print the JSON string representation of the object
print(SendResponse.to_json())

# convert the object into a dict
send_response_dict = send_response_instance.to_dict()
# create an instance of SendResponse from a dict
send_response_from_dict = SendResponse.from_dict(send_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


