# PatchedMentorCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**flow** | **object** | The langflow json for the mentor | [optional] 
**slug** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**allow_anonymous** | **bool** |  | [optional] 
**metadata** | **object** |  | [optional] 
**enable_moderation** | **bool** |  | [optional] 
**enable_post_processing_system** | **bool** |  | [optional] 
**enable_openai_assistant** | **bool** | (Deprecated) Set template mentor to openai-agent instead. | [optional] 
**enable_total_grounding** | **bool** | Whether to force mentor to only use information within the provided documents. | [optional] 
**enable_suggested_prompts** | **bool** | Whether to show suggested prompts for the mentor or not. Note: Suggested prompts are created by tenant admins. | [optional] 
**enable_guided_prompts** | **bool** | Whether to show suggested prompts for the mentor or not. Note: Guided prompts are created with an llm based on chat history. | [optional] 
**google_voice** | **int** |  | [optional] 
**openai_voice** | **int** |  | [optional] 
**guided_prompt_instructions** | **str** | Instructions to determine how prompt suggestions are generated. | [optional] 
**categories** | **List[int]** |  | [optional] 
**proactive_prompt** | **str** | Prompt template used to start a conversation with the user when greeting_type is proactive_prompt. This will be sent to the LLM so it can respond naturally | [optional] 
**moderation_system_prompt** | **str** | The prompt for the moderation system. This prompt must clearly distinguish between &#39;Approapriate&#39; and &#39;Not Appropriate&#39; queries. | [optional] 
**post_processing_prompt** | **str** | Prompt to be used to alter or modify final llm response into any desired form. | [optional] 
**moderation_response** | **str** | Desired feedback to return to the user when their prompt is deemed inappropriate. | [optional] 
**safety_system_prompt** | **str** | Prompt to check whether the models response is appropriate or not. | [optional] 
**safety_response** | **str** | Feedback given to the user when a model generates an inappropriate response | [optional] 
**disable_chathistory** | **bool** |  | [optional] 
**enable_safety_system** | **bool** |  | [optional] 
**proactive_response** | **str** | Response to start a conversation with a user. | [optional] 
**mcp_servers** | **List[int]** |  | [optional] 
**greeting_method** | [**GreetingMethodEnum**](GreetingMethodEnum.md) | How the mentor should greet the user. proactive_prompt: Allow the LLM to respond to proactive_prompt msg. proactive_response: use proactive_response template without performing an LLM call.  * &#x60;proactive_prompt&#x60; - Proactive Prompt * &#x60;proactive_response&#x60; - Proactive Response | [optional] 
**last_accessed_by** | **int** | edX user ID | [optional] 
**recently_accessed_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mentor_create import PatchedMentorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentorCreate from a JSON string
patched_mentor_create_instance = PatchedMentorCreate.from_json(json)
# print the JSON string representation of the object
print(PatchedMentorCreate.to_json())

# convert the object into a dict
patched_mentor_create_dict = patched_mentor_create_instance.to_dict()
# create an instance of PatchedMentorCreate from a dict
patched_mentor_create_from_dict = PatchedMentorCreate.from_dict(patched_mentor_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


