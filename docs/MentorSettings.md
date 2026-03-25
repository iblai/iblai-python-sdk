# MentorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**display_name** | **str** |  | [optional] 
**profile_image** | **str** |  | [optional] 
**initial_message** | **str** |  | [optional] 
**suggested_message** | **str** |  | [optional] 
**theme** | [**ThemeEnum**](ThemeEnum.md) |  | [optional] 
**user_message_color** | **str** |  | [optional] 
**mentor_bubble_color** | **str** |  | [optional] 
**align_mentor_bubble** | [**AlignMentorBubbleEnum**](AlignMentorBubbleEnum.md) |  | [optional] 
**mentor** | **str** |  | [readonly] 
**mentor_slug** | **str** |  | [readonly] 
**mentor_unique_id** | **str** |  | [readonly] 
**mentor_id** | **int** |  | [readonly] 
**metadata** | **object** |  | [readonly] 
**mentor_visibility** | **str** |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**enable_memory_component** | **bool** |  | [readonly] 
**custom_css** | **str** |  | [optional] 
**custom_javascript** | **str** |  | [optional] 
**enable_custom_javascript** | **bool** |  | [readonly] 
**allow_anonymous** | **bool** |  | [readonly] 
**enable_offline_mode** | **bool** |  | [readonly] 
**mentor_description** | **str** |  | [readonly] 
**suggested_prompts** | **object** |  | [readonly] 
**proactive_response** | **str** |  | [readonly] 
**greeting_method** | **str** |  | [readonly] 
**mentor_tools** | **object** |  | [readonly] 
**can_use_tools** | **bool** |  | [readonly] 
**llm_name** | **str** |  | [readonly] 
**proactive_prompt** | **str** |  | [readonly] 
**study_mode_prompt** | **str** |  | [readonly] 
**disclaimer** | **str** |  | [readonly] 
**enable_disclaimer** | **bool** |  | [readonly] 
**show_attachment** | **bool** |  | [readonly] 
**show_voice_call** | **bool** |  | [readonly] 
**show_voice_record** | **bool** |  | [readonly] 
**show_rag_images** | **bool** |  | [readonly] 
**starter_prompts** | **str** |  | [readonly] 
**embed_is_context_aware** | **bool** |  | [readonly] 
**embed_open_by_default** | **bool** |  | [readonly] 
**embed_show_attachment** | **bool** |  | [readonly] 
**embed_show_voice_call** | **bool** |  | [readonly] 
**embed_show_voice_record** | **bool** |  | [readonly] 
**show_explore_mentors** | **bool** |  | [readonly] 
**embed_icon_selection_data** | **object** |  | [readonly] 
**embed_custom_image** | **str** |  | [optional] 
**placeholder_prompt** | **str** |  | [readonly] 
**enable_email_chat** | **bool** |  | [readonly] 
**enable_spaced_repetition** | **bool** |  | [readonly] 
**enable_instruction_mode** | **bool** |  | [readonly] 
**enable_socratic_mode** | **bool** |  | [readonly] 
**is_guided_mentor** | **bool** |  | [readonly] 
**is_featured** | **bool** |  | [readonly] 
**enable_guided_prompts** | **bool** |  | [readonly] 
**save_flagged_prompts** | **bool** |  | [readonly] 
**enable_moderation** | **bool** |  | [readonly] 
**enable_multi_query_rag** | **bool** |  | [readonly] 
**enable_prompt_caching** | **bool** |  | [readonly] 
**enable_post_processing_system** | **bool** |  | [readonly] 
**enable_safety_system** | **bool** |  | [readonly] 
**forkable** | **bool** |  | [readonly] 
**forkable_with_training_data** | **bool** |  | [readonly] 
**mentor_name** | **str** |  | [readonly] 
**categories** | [**List[MentorCategory]**](MentorCategory.md) |  | [readonly] 
**types** | [**List[MentorType]**](MentorType.md) |  | [readonly] 
**subjects** | [**List[Subject]**](Subject.md) |  | [readonly] 
**recently_accessed_at** | **datetime** |  | [readonly] 
**created_by** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**llm_config** | **object** |  | [readonly] 
**llm_provider** | **str** |  | [readonly] 
**system_prompt** | **str** |  | [readonly] 
**llm_temperature** | **float** |  | [readonly] 
**safety_system_prompt** | **str** |  | [readonly] 
**safety_response** | **str** |  | [readonly] 
**moderation_system_prompt** | **str** |  | [readonly] 
**post_processing_prompt** | **str** |  | [readonly] 
**moderation_response** | **str** |  | [readonly] 
**mcp_servers** | [**List[MCPServer]**](MCPServer.md) |  | [readonly] 
**department** | **str** |  | [readonly] 
**disable_chathistory** | **str** |  | [readonly] 
**call_configuration** | [**CallConfiguration**](CallConfiguration.md) |  | [readonly] 
**guided_prompt_instructions** | **str** |  | [readonly] 
**seo_tags** | **object** |  | [readonly] 
**marketing_conversations** | **object** |  | [readonly] 
**template_mentor** | **object** |  | [readonly] 
**google_voice** | **str** |  | [readonly] 
**openai_voice** | **str** |  | [readonly] 
**enable_openai_assistant** | **bool** |  | [readonly] 
**enable_total_grounding** | **bool** |  | [readonly] 
**enable_suggested_prompts** | **bool** |  | [readonly] 
**is_deleted** | **bool** |  | [readonly] 
**is_lti_accessible** | **bool** | Enables LTI access for this mentor. When True, LTI users can be granted access via RBAC policies. | [optional] 

## Example

```python
from iblai.models.mentor_settings import MentorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSettings from a JSON string
mentor_settings_instance = MentorSettings.from_json(json)
# print the JSON string representation of the object
print(MentorSettings.to_json())

# convert the object into a dict
mentor_settings_dict = mentor_settings_instance.to_dict()
# create an instance of MentorSettings from a dict
mentor_settings_from_dict = MentorSettings.from_dict(mentor_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


