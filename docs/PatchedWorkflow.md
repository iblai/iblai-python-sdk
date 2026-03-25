# PatchedWorkflow

Serializer for Workflow CRUD operations.  Provides basic ReactFlow JSON validation (Phase 1) to ensure definitions are renderable, while allowing draft workflows that may not be executable.  Comprehensive execution validation (Phase 2) is available via the validate action endpoint.  Fields: - All model fields are exposed - Platform and creator are set automatically from URL context - Read-only fields: id, unique_id, created_at, updated_at - Chat settings (chat_name, chat_greeting, etc.) update the entry_mentor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**unique_id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**definition** | **object** | Workflow definition in ReactFlow format | [optional] 
**is_active** | **bool** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**parent_workflow** | **int** | Parent workflow if this is a template variant | [optional] 
**platform** | **int** |  | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**platform_name** | **str** |  | [optional] [readonly] 
**created_by** | **int** | edX user ID | [optional] [readonly] 
**created_by_username** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**node_count** | **int** | Get the number of nodes in the workflow definition. | [optional] [readonly] 
**edge_count** | **int** | Get the number of edges in the workflow definition. | [optional] [readonly] 
**entry_mentor_id** | **str** |  | [optional] [readonly] 
**chat_name** | **str** | Display name for chat (updates entry_mentor.name) | [optional] 
**chat_proactive_response** | **str** | Proactive greeting message for chat (updates entry_mentor.proactive_response) | [optional] 

## Example

```python
from iblai.models.patched_workflow import PatchedWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWorkflow from a JSON string
patched_workflow_instance = PatchedWorkflow.from_json(json)
# print the JSON string representation of the object
print(PatchedWorkflow.to_json())

# convert the object into a dict
patched_workflow_dict = patched_workflow_instance.to_dict()
# create an instance of PatchedWorkflow from a dict
patched_workflow_from_dict = PatchedWorkflow.from_dict(patched_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


