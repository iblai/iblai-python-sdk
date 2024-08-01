# TopicModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from iblai.models.topic_model import TopicModel

# TODO update the JSON string below
json = "{}"
# create an instance of TopicModel from a JSON string
topic_model_instance = TopicModel.from_json(json)
# print the JSON string representation of the object
print(TopicModel.to_json())

# convert the object into a dict
topic_model_dict = topic_model_instance.to_dict()
# create an instance of TopicModel from a dict
topic_model_from_dict = TopicModel.from_dict(topic_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


