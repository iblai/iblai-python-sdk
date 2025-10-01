# PaginatedDisclaimerAgreementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DisclaimerAgreement]**](DisclaimerAgreement.md) |  | 

## Example

```python
from iblai.models.paginated_disclaimer_agreement_list import PaginatedDisclaimerAgreementList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDisclaimerAgreementList from a JSON string
paginated_disclaimer_agreement_list_instance = PaginatedDisclaimerAgreementList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDisclaimerAgreementList.to_json())

# convert the object into a dict
paginated_disclaimer_agreement_list_dict = paginated_disclaimer_agreement_list_instance.to_dict()
# create an instance of PaginatedDisclaimerAgreementList from a dict
paginated_disclaimer_agreement_list_from_dict = PaginatedDisclaimerAgreementList.from_dict(paginated_disclaimer_agreement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


