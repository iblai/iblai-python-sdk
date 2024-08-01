# SubTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**topic** | [**Topic**](Topic.md) |  | 
**name** | **str** |  | 

## Example

```python
from iblai.models.sub_topic import SubTopic

# TODO update the JSON string below
json = "{}"
# create an instance of SubTopic from a JSON string
sub_topic_instance = SubTopic.from_json(json)
# print the JSON string representation of the object
print(SubTopic.to_json())

# convert the object into a dict
sub_topic_dict = sub_topic_instance.to_dict()
# create an instance of SubTopic from a dict
sub_topic_from_dict = SubTopic.from_dict(sub_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


