# V2PersonalizedMentorsResponse

Response serializer for V2 Personalized Mentors Search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** | List of personalized mentor search results | 
**count** | **int** | Total number of results | 
**next** | **str** | URL for next page of results | 
**previous** | **str** | URL for previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from iblai.models.v2_personalized_mentors_response import V2PersonalizedMentorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2PersonalizedMentorsResponse from a JSON string
v2_personalized_mentors_response_instance = V2PersonalizedMentorsResponse.from_json(json)
# print the JSON string representation of the object
print(V2PersonalizedMentorsResponse.to_json())

# convert the object into a dict
v2_personalized_mentors_response_dict = v2_personalized_mentors_response_instance.to_dict()
# create an instance of V2PersonalizedMentorsResponse from a dict
v2_personalized_mentors_response_from_dict = V2PersonalizedMentorsResponse.from_dict(v2_personalized_mentors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


