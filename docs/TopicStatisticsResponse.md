# TopicStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_topics** | **int** |  | 
**total_topics_change_percentage** | **float** |  | 
**new_topics** | **int** |  | 
**new_topics_change_percentage** | **float** |  | 

## Example

```python
from iblai.models.topic_statistics_response import TopicStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicStatisticsResponse from a JSON string
topic_statistics_response_instance = TopicStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(TopicStatisticsResponse.to_json())

# convert the object into a dict
topic_statistics_response_dict = topic_statistics_response_instance.to_dict()
# create an instance of TopicStatisticsResponse from a dict
topic_statistics_response_from_dict = TopicStatisticsResponse.from_dict(topic_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


