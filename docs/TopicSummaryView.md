# TopicSummaryView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_topics** | **int** |  | 
**topics_summary** | [**List[TopicConversation]**](TopicConversation.md) |  | 

## Example

```python
from iblai.models.topic_summary_view import TopicSummaryView

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSummaryView from a JSON string
topic_summary_view_instance = TopicSummaryView.from_json(json)
# print the JSON string representation of the object
print(TopicSummaryView.to_json())

# convert the object into a dict
topic_summary_view_dict = topic_summary_view_instance.to_dict()
# create an instance of TopicSummaryView from a dict
topic_summary_view_from_dict = TopicSummaryView.from_dict(topic_summary_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


