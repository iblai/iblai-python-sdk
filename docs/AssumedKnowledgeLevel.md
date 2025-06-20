# AssumedKnowledgeLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**level** | **str** |  | 

## Example

```python
from iblai.models.assumed_knowledge_level import AssumedKnowledgeLevel

# TODO update the JSON string below
json = "{}"
# create an instance of AssumedKnowledgeLevel from a JSON string
assumed_knowledge_level_instance = AssumedKnowledgeLevel.from_json(json)
# print the JSON string representation of the object
print(AssumedKnowledgeLevel.to_json())

# convert the object into a dict
assumed_knowledge_level_dict = assumed_knowledge_level_instance.to_dict()
# create an instance of AssumedKnowledgeLevel from a dict
assumed_knowledge_level_from_dict = AssumedKnowledgeLevel.from_dict(assumed_knowledge_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


