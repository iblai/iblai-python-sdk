# MainCreds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_main_credentials** | **bool** |  | 

## Example

```python
from iblai.models.main_creds import MainCreds

# TODO update the JSON string below
json = "{}"
# create an instance of MainCreds from a JSON string
main_creds_instance = MainCreds.from_json(json)
# print the JSON string representation of the object
print(MainCreds.to_json())

# convert the object into a dict
main_creds_dict = main_creds_instance.to_dict()
# create an instance of MainCreds from a dict
main_creds_from_dict = MainCreds.from_dict(main_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


