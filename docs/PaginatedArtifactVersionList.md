# PaginatedArtifactVersionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ArtifactVersion]**](ArtifactVersion.md) |  | 

## Example

```python
from iblai.models.paginated_artifact_version_list import PaginatedArtifactVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedArtifactVersionList from a JSON string
paginated_artifact_version_list_instance = PaginatedArtifactVersionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedArtifactVersionList.to_json())

# convert the object into a dict
paginated_artifact_version_list_dict = paginated_artifact_version_list_instance.to_dict()
# create an instance of PaginatedArtifactVersionList from a dict
paginated_artifact_version_list_from_dict = PaginatedArtifactVersionList.from_dict(paginated_artifact_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


