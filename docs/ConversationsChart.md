# ConversationsChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**points** | [**List[ConversationChartPoint]**](ConversationChartPoint.md) |  | 

## Example

```python
from iblai.models.conversations_chart import ConversationsChart

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsChart from a JSON string
conversations_chart_instance = ConversationsChart.from_json(json)
# print the JSON string representation of the object
print(ConversationsChart.to_json())

# convert the object into a dict
conversations_chart_dict = conversations_chart_instance.to_dict()
# create an instance of ConversationsChart from a dict
conversations_chart_from_dict = ConversationsChart.from_dict(conversations_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


