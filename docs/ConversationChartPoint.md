# ConversationChartPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**value** | **int** |  | 

## Example

```python
from iblai.models.conversation_chart_point import ConversationChartPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationChartPoint from a JSON string
conversation_chart_point_instance = ConversationChartPoint.from_json(json)
# print the JSON string representation of the object
print(ConversationChartPoint.to_json())

# convert the object into a dict
conversation_chart_point_dict = conversation_chart_point_instance.to_dict()
# create an instance of ConversationChartPoint from a dict
conversation_chart_point_from_dict = ConversationChartPoint.from_dict(conversation_chart_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


