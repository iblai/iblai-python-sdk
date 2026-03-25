# V2RecommendationResponse

Response serializer for V2 Course Recommendations.  Returns a list of recommended courses with AI-generated reasoning. Includes metadata about the recommendation method used (RAG vs LLM).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[CourseRecommendation]**](CourseRecommendation.md) | List of course recommendations with reasoning | 
**user_context** | **Dict[str, object]** | Summary of user context used for recommendations | [optional] 
**recommendation_id** | **str** | Unique ID for this recommendation set (for tracking) | [optional] 
**generated_at** | **datetime** | When these recommendations were generated | 
**platform_key** | **str** | Platform key for these recommendations | 
**method_used** | **str** | Method used to generate recommendations: &#39;rag_only&#39;, &#39;llm_only&#39;, or &#39;rag_plus_llm&#39; | [optional] 
**search_query_used** | **str** | The actual search query used for RAG similarity search (if applicable) | [optional] 
**candidates_retrieved** | **int** | Number of candidates retrieved via RAG before filtering (if applicable) | [optional] 
**includes_main_catalog** | **bool** | Whether the results include items from the &#39;main&#39; tenant catalog | [optional] [default to False]
**processing_time_seconds** | **float** | Time taken to generate recommendations (in seconds) | [optional] 
**success** | **bool** | Whether the request was successful | [optional] [default to True]
**count** | **int** | Total number of recommendations available | [optional] 
**next** | **str** | URL for the next page of results (if pagination is enabled) | [optional] 
**previous** | **str** | URL for the previous page of results (if pagination is enabled) | [optional] 

## Example

```python
from iblai.models.v2_recommendation_response import V2RecommendationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2RecommendationResponse from a JSON string
v2_recommendation_response_instance = V2RecommendationResponse.from_json(json)
# print the JSON string representation of the object
print(V2RecommendationResponse.to_json())

# convert the object into a dict
v2_recommendation_response_dict = v2_recommendation_response_instance.to_dict()
# create an instance of V2RecommendationResponse from a dict
v2_recommendation_response_from_dict = V2RecommendationResponse.from_dict(v2_recommendation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


