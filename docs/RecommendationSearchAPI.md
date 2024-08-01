# RecommendationSearchAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_api_url** | **str** |  | 

## Example

```python
from iblai.models.recommendation_search_api import RecommendationSearchAPI

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationSearchAPI from a JSON string
recommendation_search_api_instance = RecommendationSearchAPI.from_json(json)
# print the JSON string representation of the object
print(RecommendationSearchAPI.to_json())

# convert the object into a dict
recommendation_search_api_dict = recommendation_search_api_instance.to_dict()
# create an instance of RecommendationSearchAPI from a dict
recommendation_search_api_from_dict = RecommendationSearchAPI.from_dict(recommendation_search_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


