# PaginatedTopicStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | 
**previous** | **str** |  | 
**results** | [**List[TopicStatistics]**](TopicStatistics.md) |  | 

## Example

```python
from iblai.models.paginated_topic_statistics_response import PaginatedTopicStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTopicStatisticsResponse from a JSON string
paginated_topic_statistics_response_instance = PaginatedTopicStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedTopicStatisticsResponse.to_json())

# convert the object into a dict
paginated_topic_statistics_response_dict = paginated_topic_statistics_response_instance.to_dict()
# create an instance of PaginatedTopicStatisticsResponse from a dict
paginated_topic_statistics_response_from_dict = PaginatedTopicStatisticsResponse.from_dict(paginated_topic_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


