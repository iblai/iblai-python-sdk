# ArtifactList

Lightweight serializer for listing artifacts.  This serializer is optimized for list views, excluding the potentially large content field and including useful computed fields.  Fields:     - id: Unique identifier for the artifact     - title: Title or identifier for the artifact     - file_extension: The extension of the file     - llm_name: Name of the LLM that generated the artifact     - llm_provider: Provider of the LLM     - date_created: Timestamp when the artifact was created     - date_updated: Timestamp when the artifact was last updated     - username: Username of the student who owns the artifact     - session_id: UUID of the session that generated the artifact     - content_length: Length of the content in characters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | Title or identifier for the artifact | [readonly] 
**file_extension** | **str** | The extension of the file for the artifact. eg. &#x60;py&#x60;, &#x60;md&#x60;, &#x60;html&#x60;, &#x60;json&#x60;, &#x60;csv&#x60;, etc | [readonly] 
**llm_name** | **str** |  | [readonly] 
**llm_provider** | **str** |  | [readonly] 
**date_created** | **datetime** |  | [readonly] 
**date_updated** | **datetime** |  | [readonly] 
**username** | **str** | Username of the student who owns this artifact | [readonly] 
**session_id** | **str** | UUID of the session that generated this artifact | [readonly] 
**content_length** | **int** | Length of the artifact content in characters | [readonly] 

## Example

```python
from iblai.models.artifact_list import ArtifactList

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactList from a JSON string
artifact_list_instance = ArtifactList.from_json(json)
# print the JSON string representation of the object
print(ArtifactList.to_json())

# convert the object into a dict
artifact_list_dict = artifact_list_instance.to_dict()
# create an instance of ArtifactList from a dict
artifact_list_from_dict = ArtifactList.from_dict(artifact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


