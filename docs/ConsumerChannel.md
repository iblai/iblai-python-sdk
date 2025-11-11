# ConsumerChannel

Serializer for channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from iblai.models.consumer_channel import ConsumerChannel

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerChannel from a JSON string
consumer_channel_instance = ConsumerChannel.from_json(json)
# print the JSON string representation of the object
print(ConsumerChannel.to_json())

# convert the object into a dict
consumer_channel_dict = consumer_channel_instance.to_dict()
# create an instance of ConsumerChannel from a dict
consumer_channel_from_dict = ConsumerChannel.from_dict(consumer_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


