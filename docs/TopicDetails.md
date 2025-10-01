# TopicDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TopicDetail]**](TopicDetail.md) |  | 
**pagination** | **Dict[str, object]** |  | 

## Example

```python
from iblai.models.topic_details import TopicDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TopicDetails from a JSON string
topic_details_instance = TopicDetails.from_json(json)
# print the JSON string representation of the object
print(TopicDetails.to_json())

# convert the object into a dict
topic_details_dict = topic_details_instance.to_dict()
# create an instance of TopicDetails from a dict
topic_details_from_dict = TopicDetails.from_dict(topic_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


