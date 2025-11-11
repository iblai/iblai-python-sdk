# PlatformPrompt

Serializer for platform recommendation prompt management.  Used by instructors/admins to configure tenant-specific prompts for different SPAs. A platform can have multiple prompts (one per SPA/frontend).  Note: spa_url will be automatically normalized (protocol stripped, lowercase) during validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key this prompt belongs to | [optional] 
**prompt_text** | **str** | The custom recommendation strategy prompt | [optional] 
**recommendation_type** | [**RecommendationTypeEnum**](RecommendationTypeEnum.md) | Prompt category. Use &#39;catalog&#39; for courses/programs/resources/pathways; use &#39;mentors&#39; for mentor prompts.  * &#x60;mentors&#x60; - Mentor Recommendations * &#x60;catalog&#x60; - Catalog Recommendations | [optional] 
**spa_url** | **str** | Frontend/SPA identifier (e.g., &#39;catalog.example.com&#39;, &#39;mentor-ai.ibl.com&#39;, &#39;https://mentor-ai.ibl.com&#39;). Protocol and case will be normalized automatically. Leave blank for platform-wide prompts. | [optional] 
**active** | **bool** | Whether this prompt is currently active | [optional] [default to True]

## Example

```python
from iblai.models.platform_prompt import PlatformPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformPrompt from a JSON string
platform_prompt_instance = PlatformPrompt.from_json(json)
# print the JSON string representation of the object
print(PlatformPrompt.to_json())

# convert the object into a dict
platform_prompt_dict = platform_prompt_instance.to_dict()
# create an instance of PlatformPrompt from a dict
platform_prompt_from_dict = PlatformPrompt.from_dict(platform_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


