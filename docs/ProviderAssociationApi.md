# iblai.ProviderAssociationApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_association_stripe_callback_retrieve**](ProviderAssociationApi.md#provider_association_stripe_callback_retrieve) | **GET** /api/provider-association/stripe/callback/{launch_id}/ | 


# **provider_association_stripe_callback_retrieve**
> AiAccountOrgsUseDefaultLlmKeyCreate200Response provider_association_stripe_callback_retrieve(launch_id)



Handle callbacks from Stripe after successful checkout.  Updates: - Platform launch state - Association configuration status

### Example


```python
import iblai
from iblai.models.ai_account_orgs_use_default_llm_key_create200_response import AiAccountOrgsUseDefaultLlmKeyCreate200Response
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProviderAssociationApi(api_client)
launch_id = 'launch_id_example' # str | 

try:
    api_response = api_instance.provider_association_stripe_callback_retrieve(launch_id)
    print("The response of ProviderAssociationApi->provider_association_stripe_callback_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProviderAssociationApi->provider_association_stripe_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **str**|  | 

### Return type

[**AiAccountOrgsUseDefaultLlmKeyCreate200Response**](AiAccountOrgsUseDefaultLlmKeyCreate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

