# PaginatedArtifactListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ArtifactList]**](ArtifactList.md) |  | 

## Example

```python
from iblai.models.paginated_artifact_list_list import PaginatedArtifactListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedArtifactListList from a JSON string
paginated_artifact_list_list_instance = PaginatedArtifactListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedArtifactListList.to_json())

# convert the object into a dict
paginated_artifact_list_list_dict = paginated_artifact_list_list_instance.to_dict()
# create an instance of PaginatedArtifactListList from a dict
paginated_artifact_list_list_from_dict = PaginatedArtifactListList.from_dict(paginated_artifact_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


