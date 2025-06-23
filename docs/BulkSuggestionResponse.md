# BulkSuggestionResponse

Response serializer for bulk suggestion operation results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **int** | Number of successfully created suggestions | 
**error_codes** | **List[str]** | List of error codes for failed suggestions | 

## Example

```python
from iblai.models.bulk_suggestion_response import BulkSuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSuggestionResponse from a JSON string
bulk_suggestion_response_instance = BulkSuggestionResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSuggestionResponse.to_json())

# convert the object into a dict
bulk_suggestion_response_dict = bulk_suggestion_response_instance.to_dict()
# create an instance of BulkSuggestionResponse from a dict
bulk_suggestion_response_from_dict = BulkSuggestionResponse.from_dict(bulk_suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


