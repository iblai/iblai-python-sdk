# DisclaimerAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**disclaimer** | **int** |  | 
**agreed_at** | **datetime** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**user_id** | **str** |  | [readonly] 

## Example

```python
from iblai.models.disclaimer_agreement import DisclaimerAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of DisclaimerAgreement from a JSON string
disclaimer_agreement_instance = DisclaimerAgreement.from_json(json)
# print the JSON string representation of the object
print(DisclaimerAgreement.to_json())

# convert the object into a dict
disclaimer_agreement_dict = disclaimer_agreement_instance.to_dict()
# create an instance of DisclaimerAgreement from a dict
disclaimer_agreement_from_dict = DisclaimerAgreement.from_dict(disclaimer_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


