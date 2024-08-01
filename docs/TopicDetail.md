# TopicDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**total_topics** | **int** |  | 
**number_of_messages** | **int** |  | 
**number_of_conversations** | **int** |  | 
**user_sentiment** | **str** |  | 
**user_ratings** | **str** |  | 
**name** | **str** |  | 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**platform** | **int** |  | [optional] 

## Example

```python
from iblai.models.topic_detail import TopicDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TopicDetail from a JSON string
topic_detail_instance = TopicDetail.from_json(json)
# print the JSON string representation of the object
print(TopicDetail.to_json())

# convert the object into a dict
topic_detail_dict = topic_detail_instance.to_dict()
# create an instance of TopicDetail from a dict
topic_detail_from_dict = TopicDetail.from_dict(topic_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


