# ArtifactVersion

Serializer for ArtifactVersion model.  Represents a single version of an artifact with its content and metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**artifact** | [**Artifact**](Artifact.md) |  | 
**title** | **str** | Get the title of the artifact version. | [readonly] 
**content** | **str** | The markdown-styled content of this artifact version | 
**session_id** | **str** | UUID of the session that generated this artifact version | [readonly] 
**content_length** | **int** | Length of the version content in characters | [readonly] 
**is_current** | **bool** | Whether this version is the current/active version | [readonly] 
**chat_message** | **int** |  | [readonly] 
**version_number** | **int** | Sequential version number for display purposes | [readonly] [default to 1]
**date_created** | **datetime** | When this version was created | [readonly] 
**created_by** | **str** | Identifier for who created this version (e.g., &#39;llm&#39;, &#39;user:username&#39;) | [optional] 
**change_summary** | **str** | Optional summary of what changed in this version | [optional] 
**interface** | [**InterfaceEnum**](InterfaceEnum.md) | How this version was created  * &#x60;chat&#x60; - Chat * &#x60;api&#x60; - Api | [readonly] 

## Example

```python
from iblai.models.artifact_version import ArtifactVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactVersion from a JSON string
artifact_version_instance = ArtifactVersion.from_json(json)
# print the JSON string representation of the object
print(ArtifactVersion.to_json())

# convert the object into a dict
artifact_version_dict = artifact_version_instance.to_dict()
# create an instance of ArtifactVersion from a dict
artifact_version_from_dict = ArtifactVersion.from_dict(artifact_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


