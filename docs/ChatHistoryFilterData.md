# ChatHistoryFilterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | [**List[TopicModel]**](TopicModel.md) |  | 
**date_ranges** | [**List[DateRange]**](DateRange.md) |  | [optional] 
**sentiment** | **List[str]** |  | [optional] 

## Example

```python
from iblai.models.chat_history_filter_data import ChatHistoryFilterData

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistoryFilterData from a JSON string
chat_history_filter_data_instance = ChatHistoryFilterData.from_json(json)
# print the JSON string representation of the object
print(ChatHistoryFilterData.to_json())

# convert the object into a dict
chat_history_filter_data_dict = chat_history_filter_data_instance.to_dict()
# create an instance of ChatHistoryFilterData from a dict
chat_history_filter_data_from_dict = ChatHistoryFilterData.from_dict(chat_history_filter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


