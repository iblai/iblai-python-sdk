# BulkCreateAssertion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipped** | **List[object]** |  | 
**issued** | **List[object]** |  | 

## Example

```python
from iblai.models.bulk_create_assertion import BulkCreateAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateAssertion from a JSON string
bulk_create_assertion_instance = BulkCreateAssertion.from_json(json)
# print the JSON string representation of the object
print(BulkCreateAssertion.to_json())

# convert the object into a dict
bulk_create_assertion_dict = bulk_create_assertion_instance.to_dict()
# create an instance of BulkCreateAssertion from a dict
bulk_create_assertion_from_dict = BulkCreateAssertion.from_dict(bulk_create_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


