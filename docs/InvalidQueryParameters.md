# InvalidQueryParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] [default to 'Invalid query parameters.']

## Example

```python
from iblai.models.invalid_query_parameters import InvalidQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidQueryParameters from a JSON string
invalid_query_parameters_instance = InvalidQueryParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidQueryParameters.to_json())

# convert the object into a dict
invalid_query_parameters_dict = invalid_query_parameters_instance.to_dict()
# create an instance of InvalidQueryParameters from a dict
invalid_query_parameters_from_dict = InvalidQueryParameters.from_dict(invalid_query_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


