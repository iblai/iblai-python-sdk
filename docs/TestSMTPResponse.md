# TestSMTPResponse

Serializer for SMTP test response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from iblai.models.test_smtp_response import TestSMTPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestSMTPResponse from a JSON string
test_smtp_response_instance = TestSMTPResponse.from_json(json)
# print the JSON string representation of the object
print(TestSMTPResponse.to_json())

# convert the object into a dict
test_smtp_response_dict = test_smtp_response_instance.to_dict()
# create an instance of TestSMTPResponse from a dict
test_smtp_response_from_dict = TestSMTPResponse.from_dict(test_smtp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


