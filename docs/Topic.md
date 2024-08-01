# Topic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_topics** | **int** |  | 
**number_of_messages** | **int** |  | 
**topic_detail** | [**List[TopicDetail]**](TopicDetail.md) |  | 
**monthly_total_topics_diff** | **int** |  | 

## Example

```python
from iblai.models.topic import Topic

# TODO update the JSON string below
json = "{}"
# create an instance of Topic from a JSON string
topic_instance = Topic.from_json(json)
# print the JSON string representation of the object
print(Topic.to_json())

# convert the object into a dict
topic_dict = topic_instance.to_dict()
# create an instance of Topic from a dict
topic_from_dict = Topic.from_dict(topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


