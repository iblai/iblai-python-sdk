# ArtifactVersionList

Lightweight serializer for listing artifact versions. Excludes the potentially large content field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**artifact** | **int** | The artifact this version belongs to | [readonly] 
**is_current** | **bool** | Whether this version is the current/active version | [readonly] 
**version_number** | **int** | Sequential version number for display purposes | [readonly] [default to 1]
**date_created** | **datetime** | When this version was created | [readonly] 
**created_by** | **str** | Identifier for who created this version (e.g., &#39;llm&#39;, &#39;user:username&#39;) | [readonly] 
**change_summary** | **str** | Optional summary of what changed in this version | [readonly] 
**content_length** | **int** | Length of the version content in characters | [readonly] 

## Example

```python
from iblai.models.artifact_version_list import ArtifactVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactVersionList from a JSON string
artifact_version_list_instance = ArtifactVersionList.from_json(json)
# print the JSON string representation of the object
print(ArtifactVersionList.to_json())

# convert the object into a dict
artifact_version_list_dict = artifact_version_list_instance.to_dict()
# create an instance of ArtifactVersionList from a dict
artifact_version_list_from_dict = ArtifactVersionList.from_dict(artifact_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


