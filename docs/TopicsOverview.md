# TopicsOverview

Dashboard KPI overview for topics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | [**TopicsOverviewMetric**](TopicsOverviewMetric.md) | Topic metrics including all-time, monthly counts and percentage change | 
**sessions** | [**TopicsOverviewMetric**](TopicsOverviewMetric.md) | Session metrics including all-time, monthly counts and percentage change | 
**conversations** | [**TopicsOverviewMetric**](TopicsOverviewMetric.md) | Conversation metrics including all-time, monthly counts and percentage change | 
**messages** | [**TopicsOverviewMetric**](TopicsOverviewMetric.md) | Message metrics including all-time, monthly counts and percentage change | 

## Example

```python
from iblai.models.topics_overview import TopicsOverview

# TODO update the JSON string below
json = "{}"
# create an instance of TopicsOverview from a JSON string
topics_overview_instance = TopicsOverview.from_json(json)
# print the JSON string representation of the object
print(TopicsOverview.to_json())

# convert the object into a dict
topics_overview_dict = topics_overview_instance.to_dict()
# create an instance of TopicsOverview from a dict
topics_overview_from_dict = TopicsOverview.from_dict(topics_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


