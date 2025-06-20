# TopicRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_name** | **str** |  | 
**conversation_count** | **int** |  | 

## Example

```python
from iblai.models.topic_record import TopicRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TopicRecord from a JSON string
topic_record_instance = TopicRecord.from_json(json)
# print the JSON string representation of the object
print(TopicRecord.to_json())

# convert the object into a dict
topic_record_dict = topic_record_instance.to_dict()
# create an instance of TopicRecord from a dict
topic_record_from_dict = TopicRecord.from_dict(topic_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


