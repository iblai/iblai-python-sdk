# PathwayCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** |  | 
**completion_percentage** | **float** |  | [optional] 

## Example

```python
from iblai.models.pathway_completion import PathwayCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayCompletion from a JSON string
pathway_completion_instance = PathwayCompletion.from_json(json)
# print the JSON string representation of the object
print(PathwayCompletion.to_json())

# convert the object into a dict
pathway_completion_dict = pathway_completion_instance.to_dict()
# create an instance of PathwayCompletion from a dict
pathway_completion_from_dict = PathwayCompletion.from_dict(pathway_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


