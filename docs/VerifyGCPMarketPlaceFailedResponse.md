# VerifyGCPMarketPlaceFailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | [optional] [default to '']
**aud** | **str** |  | [optional] [default to '']
**iat** | **str** |  | [optional] [default to '']
**exp** | **str** |  | [optional] [default to '']
**google** | **Dict[str, object]** |  | [optional] 
**iss** | **str** |  | [optional] [default to '']
**redirect_to** | **str** |  | [readonly] 
**message** | **str** |  | [optional] [default to '']
**success** | **bool** |  | [optional] [default to False]

## Example

```python
from iblai.models.verify_gcp_market_place_failed_response import VerifyGCPMarketPlaceFailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyGCPMarketPlaceFailedResponse from a JSON string
verify_gcp_market_place_failed_response_instance = VerifyGCPMarketPlaceFailedResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyGCPMarketPlaceFailedResponse.to_json())

# convert the object into a dict
verify_gcp_market_place_failed_response_dict = verify_gcp_market_place_failed_response_instance.to_dict()
# create an instance of VerifyGCPMarketPlaceFailedResponse from a dict
verify_gcp_market_place_failed_response_from_dict = VerifyGCPMarketPlaceFailedResponse.from_dict(verify_gcp_market_place_failed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


