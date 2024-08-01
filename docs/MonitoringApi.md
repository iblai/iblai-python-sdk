# iblai.MonitoringApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitoring_connectors_retrieve**](MonitoringApi.md#monitoring_connectors_retrieve) | **GET** /monitoring/connectors/ | 


# **monitoring_connectors_retrieve**
> monitoring_connectors_retrieve()



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.MonitoringApi(api_client)

try:
    api_instance.monitoring_connectors_retrieve()
except Exception as e:
    print("Exception when calling MonitoringApi->monitoring_connectors_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

