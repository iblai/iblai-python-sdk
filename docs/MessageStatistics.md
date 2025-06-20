# MessageStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**avg_messages** | **int** |  | 
**total_sessions** | **int** |  | 

## Example

```python
from iblai.models.message_statistics import MessageStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStatistics from a JSON string
message_statistics_instance = MessageStatistics.from_json(json)
# print the JSON string representation of the object
print(MessageStatistics.to_json())

# convert the object into a dict
message_statistics_dict = message_statistics_instance.to_dict()
# create an instance of MessageStatistics from a dict
message_statistics_from_dict = MessageStatistics.from_dict(message_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


