# MentorCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**unique_id** | **str** |  | [optional] 
**flow** | **object** | The langflow json for the mentor | [optional] 
**slug** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**allow_anonymous** | **bool** |  | [optional] 
**metadata** | **object** |  | [optional] 
**enable_moderation** | **bool** |  | [optional] 
**enable_multi_query_rag** | **bool** |  | [optional] 
**enable_post_processing_system** | **bool** |  | [optional] 
**enable_openai_assistant** | **bool** | (Deprecated) Set template mentor to openai-agent instead. | [optional] 
**enable_total_grounding** | **bool** | Whether to force mentor to only use information within the provided documents. | [optional] 
**enable_suggested_prompts** | **bool** | Whether to show suggested prompts for the mentor or not. Note: Suggested prompts are created by tenant admins. | [optional] 
**enable_guided_prompts** | **bool** | Whether to show suggested prompts for the mentor or not. Note: Guided prompts are created with an llm based on chat history. | [optional] 
**google_voice** | **int** |  | [optional] 
**openai_voice** | **int** |  | [optional] 
**guided_prompt_instructions** | **str** | Instructions to determine how prompt suggestions are generated. | [optional] 
**categories** | **List[int]** |  | [optional] 
**types** | **List[int]** |  | [optional] 
**subjects** | **List[int]** |  | [optional] 
**proactive_prompt** | **str** | Prompt template used to start a conversation with the user when greeting_type is proactive_prompt. This will be sent to the LLM so it can respond naturally | [optional] 
**disclaimer** | **str** | Disclaimer to be shown to the user when the mentor is used. | [optional] 
**enable_disclaimer** | **bool** |  | [optional] 
**show_attachment** | **bool** | Show attachments on mentor. | [optional] 
**show_voice_call** | **bool** | Show voice call button on mentor. | [optional] 
**show_voice_record** | **bool** | Show voice recording button on mentor. | [optional] 
**show_rag_images** | **bool** | Show RAG images in mentor response. | [optional] 
**embed_is_context_aware** | **bool** | Allow embedded mentor to read content on the embedded web page. | [optional] 
**embed_open_by_default** | **bool** | Open mentor embed iframe by default. | [optional] 
**embed_show_attachment** | **bool** | Show attachments on embedded mentor. | [optional] 
**embed_show_voice_call** | **bool** | Show voice call button on embedded mentor. | [optional] 
**embed_show_voice_record** | **bool** | Show voice recording button on embedded mentor. | [optional] 
**placeholder_prompt** | **str** | Placeholder to be shown in the input text area when the mentor is used. | [optional] 
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
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mentor_create import MentorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCreate from a JSON string
mentor_create_instance = MentorCreate.from_json(json)
# print the JSON string representation of the object
print(MentorCreate.to_json())

# convert the object into a dict
mentor_create_dict = mentor_create_instance.to_dict()
# create an instance of MentorCreate from a dict
mentor_create_from_dict = MentorCreate.from_dict(mentor_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


