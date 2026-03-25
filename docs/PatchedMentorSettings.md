# PatchedMentorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] 
**profile_image** | **str** |  | [optional] 
**initial_message** | **str** |  | [optional] 
**suggested_message** | **str** |  | [optional] 
**theme** | [**ThemeEnum**](ThemeEnum.md) |  | [optional] 
**user_message_color** | **str** |  | [optional] 
**mentor_bubble_color** | **str** |  | [optional] 
**align_mentor_bubble** | [**AlignMentorBubbleEnum**](AlignMentorBubbleEnum.md) |  | [optional] 
**mentor** | **str** |  | [optional] [readonly] 
**mentor_slug** | **str** |  | [optional] [readonly] 
**mentor_unique_id** | **str** |  | [optional] [readonly] 
**mentor_id** | **int** |  | [optional] [readonly] 
**metadata** | **object** |  | [optional] [readonly] 
**mentor_visibility** | **str** |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**enable_memory_component** | **bool** |  | [optional] [readonly] 
**custom_css** | **str** |  | [optional] 
**custom_javascript** | **str** |  | [optional] 
**enable_custom_javascript** | **bool** |  | [optional] [readonly] 
**allow_anonymous** | **bool** |  | [optional] [readonly] 
**enable_offline_mode** | **bool** |  | [optional] [readonly] 
**mentor_description** | **str** |  | [optional] [readonly] 
**suggested_prompts** | **object** |  | [optional] [readonly] 
**proactive_response** | **str** |  | [optional] [readonly] 
**greeting_method** | **str** |  | [optional] [readonly] 
**mentor_tools** | **object** |  | [optional] [readonly] 
**can_use_tools** | **bool** |  | [optional] [readonly] 
**llm_name** | **str** |  | [optional] [readonly] 
**proactive_prompt** | **str** |  | [optional] [readonly] 
**study_mode_prompt** | **str** |  | [optional] [readonly] 
**disclaimer** | **str** |  | [optional] [readonly] 
**enable_disclaimer** | **bool** |  | [optional] [readonly] 
**show_attachment** | **bool** |  | [optional] [readonly] 
**show_voice_call** | **bool** |  | [optional] [readonly] 
**show_voice_record** | **bool** |  | [optional] [readonly] 
**show_rag_images** | **bool** |  | [optional] [readonly] 
**starter_prompts** | **str** |  | [optional] [readonly] 
**embed_is_context_aware** | **bool** |  | [optional] [readonly] 
**embed_open_by_default** | **bool** |  | [optional] [readonly] 
**embed_show_attachment** | **bool** |  | [optional] [readonly] 
**embed_show_voice_call** | **bool** |  | [optional] [readonly] 
**embed_show_voice_record** | **bool** |  | [optional] [readonly] 
**show_explore_mentors** | **bool** |  | [optional] [readonly] 
**embed_icon_selection_data** | **object** |  | [optional] [readonly] 
**embed_custom_image** | **str** |  | [optional] 
**placeholder_prompt** | **str** |  | [optional] [readonly] 
**enable_email_chat** | **bool** |  | [optional] [readonly] 
**enable_spaced_repetition** | **bool** |  | [optional] [readonly] 
**enable_instruction_mode** | **bool** |  | [optional] [readonly] 
**enable_socratic_mode** | **bool** |  | [optional] [readonly] 
**is_guided_mentor** | **bool** |  | [optional] [readonly] 
**is_featured** | **bool** |  | [optional] [readonly] 
**enable_guided_prompts** | **bool** |  | [optional] [readonly] 
**save_flagged_prompts** | **bool** |  | [optional] [readonly] 
**enable_moderation** | **bool** |  | [optional] [readonly] 
**enable_multi_query_rag** | **bool** |  | [optional] [readonly] 
**enable_prompt_caching** | **bool** |  | [optional] [readonly] 
**enable_post_processing_system** | **bool** |  | [optional] [readonly] 
**enable_safety_system** | **bool** |  | [optional] [readonly] 
**forkable** | **bool** |  | [optional] [readonly] 
**forkable_with_training_data** | **bool** |  | [optional] [readonly] 
**mentor_name** | **str** |  | [optional] [readonly] 
**categories** | [**List[MentorCategory]**](MentorCategory.md) |  | [optional] [readonly] 
**types** | [**List[MentorType]**](MentorType.md) |  | [optional] [readonly] 
**subjects** | [**List[Subject]**](Subject.md) |  | [optional] [readonly] 
**recently_accessed_at** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**llm_config** | **object** |  | [optional] [readonly] 
**llm_provider** | **str** |  | [optional] [readonly] 
**system_prompt** | **str** |  | [optional] [readonly] 
**llm_temperature** | **float** |  | [optional] [readonly] 
**safety_system_prompt** | **str** |  | [optional] [readonly] 
**safety_response** | **str** |  | [optional] [readonly] 
**moderation_system_prompt** | **str** |  | [optional] [readonly] 
**post_processing_prompt** | **str** |  | [optional] [readonly] 
**moderation_response** | **str** |  | [optional] [readonly] 
**mcp_servers** | [**List[MCPServer]**](MCPServer.md) |  | [optional] [readonly] 
**department** | **str** |  | [optional] [readonly] 
**disable_chathistory** | **str** |  | [optional] [readonly] 
**call_configuration** | [**CallConfiguration**](CallConfiguration.md) |  | [optional] [readonly] 
**guided_prompt_instructions** | **str** |  | [optional] [readonly] 
**seo_tags** | **object** |  | [optional] [readonly] 
**marketing_conversations** | **object** |  | [optional] [readonly] 
**template_mentor** | **object** |  | [optional] [readonly] 
**google_voice** | **str** |  | [optional] [readonly] 
**openai_voice** | **str** |  | [optional] [readonly] 
**enable_openai_assistant** | **bool** |  | [optional] [readonly] 
**enable_total_grounding** | **bool** |  | [optional] [readonly] 
**enable_suggested_prompts** | **bool** |  | [optional] [readonly] 
**is_deleted** | **bool** |  | [optional] [readonly] 
**is_lti_accessible** | **bool** | Enables LTI access for this mentor. When True, LTI users can be granted access via RBAC policies. | [optional] 

## Example

```python
from iblai.models.patched_mentor_settings import PatchedMentorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentorSettings from a JSON string
patched_mentor_settings_instance = PatchedMentorSettings.from_json(json)
# print the JSON string representation of the object
print(PatchedMentorSettings.to_json())

# convert the object into a dict
patched_mentor_settings_dict = patched_mentor_settings_instance.to_dict()
# create an instance of PatchedMentorSettings from a dict
patched_mentor_settings_from_dict = PatchedMentorSettings.from_dict(patched_mentor_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


