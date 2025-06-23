# TopicStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**conversations** | **int** |  | 
**messages** | **int** |  | 
**avg_sentiment** | **str** |  | 
**avg_user_rating** | **str** |  | 

## Example

```python
from iblai.models.topic_statistics import TopicStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of TopicStatistics from a JSON string
topic_statistics_instance = TopicStatistics.from_json(json)
# print the JSON string representation of the object
print(TopicStatistics.to_json())

# convert the object into a dict
topic_statistics_dict = topic_statistics_instance.to_dict()
# create an instance of TopicStatistics from a dict
topic_statistics_from_dict = TopicStatistics.from_dict(topic_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


