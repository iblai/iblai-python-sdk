# AssumedKnowledge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels** | [**List[AssumedKnowledgeLevel]**](AssumedKnowledgeLevel.md) |  | 

## Example

```python
from iblai.models.assumed_knowledge import AssumedKnowledge

# TODO update the JSON string below
json = "{}"
# create an instance of AssumedKnowledge from a JSON string
assumed_knowledge_instance = AssumedKnowledge.from_json(json)
# print the JSON string representation of the object
print(AssumedKnowledge.to_json())

# convert the object into a dict
assumed_knowledge_dict = assumed_knowledge_instance.to_dict()
# create an instance of AssumedKnowledge from a dict
assumed_knowledge_from_dict = AssumedKnowledge.from_dict(assumed_knowledge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


