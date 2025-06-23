# ValidateSourceResponse

Response serializer for source validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**valid_count** | **int** |  | 
**invalid_entries** | **List[str]** |  | 
**sample_recipients** | [**List[Recipient]**](Recipient.md) |  | 

## Example

```python
from iblai.models.validate_source_response import ValidateSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSourceResponse from a JSON string
validate_source_response_instance = ValidateSourceResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateSourceResponse.to_json())

# convert the object into a dict
validate_source_response_dict = validate_source_response_instance.to_dict()
# create an instance of ValidateSourceResponse from a dict
validate_source_response_from_dict = ValidateSourceResponse.from_dict(validate_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


