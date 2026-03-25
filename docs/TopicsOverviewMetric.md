# TopicsOverviewMetric

Serializer for individual topic overview metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_time_total** | **int** | Total count since the beginning of time | 
**this_month** | **int** | Count for current month | 
**last_month** | **int** | Count for previous month | 
**percentage_change** | **float** | Percentage change from last month to this month | 

## Example

```python
from iblai.models.topics_overview_metric import TopicsOverviewMetric

# TODO update the JSON string below
json = "{}"
# create an instance of TopicsOverviewMetric from a JSON string
topics_overview_metric_instance = TopicsOverviewMetric.from_json(json)
# print the JSON string representation of the object
print(TopicsOverviewMetric.to_json())

# convert the object into a dict
topics_overview_metric_dict = topics_overview_metric_instance.to_dict()
# create an instance of TopicsOverviewMetric from a dict
topics_overview_metric_from_dict = TopicsOverviewMetric.from_dict(topics_overview_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


