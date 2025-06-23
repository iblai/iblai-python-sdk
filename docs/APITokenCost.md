# APITokenCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Week start date for token usage aggregation | 
**completion_tokens** | **int** | Total completion tokens used in this week | 
**prompt_tokens** | **int** | Total prompt tokens used in this week | 

## Example

```python
from iblai.models.api_token_cost import APITokenCost

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenCost from a JSON string
api_token_cost_instance = APITokenCost.from_json(json)
# print the JSON string representation of the object
print(APITokenCost.to_json())

# convert the object into a dict
api_token_cost_dict = api_token_cost_instance.to_dict()
# create an instance of APITokenCost from a dict
api_token_cost_from_dict = APITokenCost.from_dict(api_token_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


