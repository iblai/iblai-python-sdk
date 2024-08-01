# iblai.AiMathApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_math_math_math_students_create**](AiMathApi.md#ai_math_math_math_students_create) | **POST** /api/ai-math/math/{org}/math-students/ | 
[**ai_math_math_math_students_destroy**](AiMathApi.md#ai_math_math_math_students_destroy) | **DELETE** /api/ai-math/math/{org}/math-students/{id}/ | 
[**ai_math_math_math_students_list**](AiMathApi.md#ai_math_math_math_students_list) | **GET** /api/ai-math/math/{org}/math-students/ | 
[**ai_math_math_math_students_partial_update**](AiMathApi.md#ai_math_math_math_students_partial_update) | **PATCH** /api/ai-math/math/{org}/math-students/{id}/ | 
[**ai_math_math_math_students_retrieve**](AiMathApi.md#ai_math_math_math_students_retrieve) | **GET** /api/ai-math/math/{org}/math-students/{id}/ | 
[**ai_math_math_math_students_update**](AiMathApi.md#ai_math_math_math_students_update) | **PUT** /api/ai-math/math/{org}/math-students/{id}/ | 
[**ai_math_math_questions_destroy**](AiMathApi.md#ai_math_math_questions_destroy) | **DELETE** /api/ai-math/math/{org}/questions/{id}/ | 
[**ai_math_math_questions_list**](AiMathApi.md#ai_math_math_questions_list) | **GET** /api/ai-math/math/{org}/questions/ | 
[**ai_math_math_questions_partial_update**](AiMathApi.md#ai_math_math_questions_partial_update) | **PATCH** /api/ai-math/math/{org}/questions/{id}/ | 
[**ai_math_math_questions_retrieve**](AiMathApi.md#ai_math_math_questions_retrieve) | **GET** /api/ai-math/math/{org}/questions/{id}/ | 
[**ai_math_math_sample_questions_create**](AiMathApi.md#ai_math_math_sample_questions_create) | **POST** /api/ai-math/math/{org}/sample-questions/ | 
[**ai_math_math_sample_questions_destroy**](AiMathApi.md#ai_math_math_sample_questions_destroy) | **DELETE** /api/ai-math/math/{org}/sample-questions/{id}/ | 
[**ai_math_math_sample_questions_list**](AiMathApi.md#ai_math_math_sample_questions_list) | **GET** /api/ai-math/math/{org}/sample-questions/ | 
[**ai_math_math_sample_questions_retrieve**](AiMathApi.md#ai_math_math_sample_questions_retrieve) | **GET** /api/ai-math/math/{org}/sample-questions/{id}/ | 
[**ai_math_math_skills_create**](AiMathApi.md#ai_math_math_skills_create) | **POST** /api/ai-math/math/{org}/skills/ | 
[**ai_math_math_skills_destroy**](AiMathApi.md#ai_math_math_skills_destroy) | **DELETE** /api/ai-math/math/{org}/skills/{id}/ | 
[**ai_math_math_skills_list**](AiMathApi.md#ai_math_math_skills_list) | **GET** /api/ai-math/math/{org}/skills/ | 
[**ai_math_math_skills_partial_update**](AiMathApi.md#ai_math_math_skills_partial_update) | **PATCH** /api/ai-math/math/{org}/skills/{id}/ | 
[**ai_math_math_skills_retrieve**](AiMathApi.md#ai_math_math_skills_retrieve) | **GET** /api/ai-math/math/{org}/skills/{id}/ | 
[**ai_math_math_skills_update**](AiMathApi.md#ai_math_math_skills_update) | **PUT** /api/ai-math/math/{org}/skills/{id}/ | 
[**ai_math_math_student_answers_create**](AiMathApi.md#ai_math_math_student_answers_create) | **POST** /api/ai-math/math/{org}/student-answers/ | 
[**ai_math_math_student_answers_destroy**](AiMathApi.md#ai_math_math_student_answers_destroy) | **DELETE** /api/ai-math/math/{org}/student-answers/{id}/ | 
[**ai_math_math_student_answers_list**](AiMathApi.md#ai_math_math_student_answers_list) | **GET** /api/ai-math/math/{org}/student-answers/ | 
[**ai_math_math_student_answers_partial_update**](AiMathApi.md#ai_math_math_student_answers_partial_update) | **PATCH** /api/ai-math/math/{org}/student-answers/{id}/ | 
[**ai_math_math_student_answers_retrieve**](AiMathApi.md#ai_math_math_student_answers_retrieve) | **GET** /api/ai-math/math/{org}/student-answers/{id}/ | 
[**ai_math_math_student_answers_update**](AiMathApi.md#ai_math_math_student_answers_update) | **PUT** /api/ai-math/math/{org}/student-answers/{id}/ | 


# **ai_math_math_math_students_create**
> MathStudent ai_math_math_math_students_create(org, math_student=math_student)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_student import MathStudent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 
math_student = iblai.MathStudent() # MathStudent |  (optional)

try:
    api_response = api_instance.ai_math_math_math_students_create(org, math_student=math_student)
    print("The response of AiMathApi->ai_math_math_math_students_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **math_student** | [**MathStudent**](MathStudent.md)|  | [optional] 

### Return type

[**MathStudent**](MathStudent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_math_students_destroy**
> ai_math_math_math_students_destroy(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math student.
org = 'org_example' # str | 

try:
    api_instance.ai_math_math_math_students_destroy(id, org)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math student. | 
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_math_students_list**
> List[MathStudent] ai_math_math_math_students_list(org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_student import MathStudent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_math_students_list(org)
    print("The response of AiMathApi->ai_math_math_math_students_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[MathStudent]**](MathStudent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_math_students_partial_update**
> MathStudent ai_math_math_math_students_partial_update(id, org, patched_math_student=patched_math_student)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_student import MathStudent
from iblai.models.patched_math_student import PatchedMathStudent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math student.
org = 'org_example' # str | 
patched_math_student = iblai.PatchedMathStudent() # PatchedMathStudent |  (optional)

try:
    api_response = api_instance.ai_math_math_math_students_partial_update(id, org, patched_math_student=patched_math_student)
    print("The response of AiMathApi->ai_math_math_math_students_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math student. | 
 **org** | **str**|  | 
 **patched_math_student** | [**PatchedMathStudent**](PatchedMathStudent.md)|  | [optional] 

### Return type

[**MathStudent**](MathStudent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_math_students_retrieve**
> MathStudent ai_math_math_math_students_retrieve(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_student import MathStudent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math student.
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_math_students_retrieve(id, org)
    print("The response of AiMathApi->ai_math_math_math_students_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math student. | 
 **org** | **str**|  | 

### Return type

[**MathStudent**](MathStudent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_math_students_update**
> MathStudent ai_math_math_math_students_update(id, org, math_student=math_student)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_student import MathStudent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math student.
org = 'org_example' # str | 
math_student = iblai.MathStudent() # MathStudent |  (optional)

try:
    api_response = api_instance.ai_math_math_math_students_update(id, org, math_student=math_student)
    print("The response of AiMathApi->ai_math_math_math_students_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_math_students_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math student. | 
 **org** | **str**|  | 
 **math_student** | [**MathStudent**](MathStudent.md)|  | [optional] 

### Return type

[**MathStudent**](MathStudent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_questions_destroy**
> ai_math_math_questions_destroy(id, org)



Retrieve, update and delete math questions.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math question.
org = 'org_example' # str | 

try:
    api_instance.ai_math_math_questions_destroy(id, org)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_questions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math question. | 
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_questions_list**
> List[MathQuestion] ai_math_math_questions_list(org)



Retrieve, update and delete math questions.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_question import MathQuestion
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_questions_list(org)
    print("The response of AiMathApi->ai_math_math_questions_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_questions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[MathQuestion]**](MathQuestion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_questions_partial_update**
> MathQuestion ai_math_math_questions_partial_update(id, org, patched_math_question=patched_math_question)



Retrieve, update and delete math questions.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_question import MathQuestion
from iblai.models.patched_math_question import PatchedMathQuestion
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math question.
org = 'org_example' # str | 
patched_math_question = iblai.PatchedMathQuestion() # PatchedMathQuestion |  (optional)

try:
    api_response = api_instance.ai_math_math_questions_partial_update(id, org, patched_math_question=patched_math_question)
    print("The response of AiMathApi->ai_math_math_questions_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_questions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math question. | 
 **org** | **str**|  | 
 **patched_math_question** | [**PatchedMathQuestion**](PatchedMathQuestion.md)|  | [optional] 

### Return type

[**MathQuestion**](MathQuestion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_questions_retrieve**
> MathQuestion ai_math_math_questions_retrieve(id, org)



Retrieve, update and delete math questions.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.math_question import MathQuestion
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this math question.
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_questions_retrieve(id, org)
    print("The response of AiMathApi->ai_math_math_questions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_questions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this math question. | 
 **org** | **str**|  | 

### Return type

[**MathQuestion**](MathQuestion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_sample_questions_create**
> SampleQuestionsDocument ai_math_math_sample_questions_create(org, sample_questions_document)



Upload documents to provide sample questions of reference to generate more math questions from.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sample_questions_document import SampleQuestionsDocument
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 
sample_questions_document = iblai.SampleQuestionsDocument() # SampleQuestionsDocument | 

try:
    api_response = api_instance.ai_math_math_sample_questions_create(org, sample_questions_document)
    print("The response of AiMathApi->ai_math_math_sample_questions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_sample_questions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **sample_questions_document** | [**SampleQuestionsDocument**](SampleQuestionsDocument.md)|  | 

### Return type

[**SampleQuestionsDocument**](SampleQuestionsDocument.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_sample_questions_destroy**
> ai_math_math_sample_questions_destroy(id, org)



Upload documents to provide sample questions of reference to generate more math questions from.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this sample questions document.
org = 'org_example' # str | 

try:
    api_instance.ai_math_math_sample_questions_destroy(id, org)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_sample_questions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sample questions document. | 
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_sample_questions_list**
> List[SampleQuestionsDocument] ai_math_math_sample_questions_list(org)



Upload documents to provide sample questions of reference to generate more math questions from.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sample_questions_document import SampleQuestionsDocument
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_sample_questions_list(org)
    print("The response of AiMathApi->ai_math_math_sample_questions_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_sample_questions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[SampleQuestionsDocument]**](SampleQuestionsDocument.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_sample_questions_retrieve**
> SampleQuestionsDocument ai_math_math_sample_questions_retrieve(id, org)



Upload documents to provide sample questions of reference to generate more math questions from.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sample_questions_document import SampleQuestionsDocument
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this sample questions document.
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_sample_questions_retrieve(id, org)
    print("The response of AiMathApi->ai_math_math_sample_questions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_sample_questions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sample questions document. | 
 **org** | **str**|  | 

### Return type

[**SampleQuestionsDocument**](SampleQuestionsDocument.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_create**
> Skill ai_math_math_skills_create(org, skill)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill import Skill
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 
skill = iblai.Skill() # Skill | 

try:
    api_response = api_instance.ai_math_math_skills_create(org, skill)
    print("The response of AiMathApi->ai_math_math_skills_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **skill** | [**Skill**](Skill.md)|  | 

### Return type

[**Skill**](Skill.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_destroy**
> ai_math_math_skills_destroy(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this skill.
org = 'org_example' # str | 

try:
    api_instance.ai_math_math_skills_destroy(id, org)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this skill. | 
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_list**
> List[Skill] ai_math_math_skills_list(org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill import Skill
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_skills_list(org)
    print("The response of AiMathApi->ai_math_math_skills_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[Skill]**](Skill.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_partial_update**
> Skill ai_math_math_skills_partial_update(id, org, patched_skill=patched_skill)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_skill import PatchedSkill
from iblai.models.skill import Skill
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this skill.
org = 'org_example' # str | 
patched_skill = iblai.PatchedSkill() # PatchedSkill |  (optional)

try:
    api_response = api_instance.ai_math_math_skills_partial_update(id, org, patched_skill=patched_skill)
    print("The response of AiMathApi->ai_math_math_skills_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this skill. | 
 **org** | **str**|  | 
 **patched_skill** | [**PatchedSkill**](PatchedSkill.md)|  | [optional] 

### Return type

[**Skill**](Skill.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_retrieve**
> Skill ai_math_math_skills_retrieve(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill import Skill
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this skill.
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_skills_retrieve(id, org)
    print("The response of AiMathApi->ai_math_math_skills_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this skill. | 
 **org** | **str**|  | 

### Return type

[**Skill**](Skill.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_skills_update**
> Skill ai_math_math_skills_update(id, org, skill)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill import Skill
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this skill.
org = 'org_example' # str | 
skill = iblai.Skill() # Skill | 

try:
    api_response = api_instance.ai_math_math_skills_update(id, org, skill)
    print("The response of AiMathApi->ai_math_math_skills_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_skills_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this skill. | 
 **org** | **str**|  | 
 **skill** | [**Skill**](Skill.md)|  | 

### Return type

[**Skill**](Skill.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_create**
> StudentAnswer ai_math_math_student_answers_create(org, student_answer)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.student_answer import StudentAnswer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 
student_answer = iblai.StudentAnswer() # StudentAnswer | 

try:
    api_response = api_instance.ai_math_math_student_answers_create(org, student_answer)
    print("The response of AiMathApi->ai_math_math_student_answers_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **student_answer** | [**StudentAnswer**](StudentAnswer.md)|  | 

### Return type

[**StudentAnswer**](StudentAnswer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_destroy**
> ai_math_math_student_answers_destroy(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this student answer.
org = 'org_example' # str | 

try:
    api_instance.ai_math_math_student_answers_destroy(id, org)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this student answer. | 
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_list**
> List[StudentAnswer] ai_math_math_student_answers_list(org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.student_answer import StudentAnswer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_student_answers_list(org)
    print("The response of AiMathApi->ai_math_math_student_answers_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[StudentAnswer]**](StudentAnswer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_partial_update**
> StudentAnswer ai_math_math_student_answers_partial_update(id, org, patched_student_answer=patched_student_answer)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_student_answer import PatchedStudentAnswer
from iblai.models.student_answer import StudentAnswer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this student answer.
org = 'org_example' # str | 
patched_student_answer = iblai.PatchedStudentAnswer() # PatchedStudentAnswer |  (optional)

try:
    api_response = api_instance.ai_math_math_student_answers_partial_update(id, org, patched_student_answer=patched_student_answer)
    print("The response of AiMathApi->ai_math_math_student_answers_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this student answer. | 
 **org** | **str**|  | 
 **patched_student_answer** | [**PatchedStudentAnswer**](PatchedStudentAnswer.md)|  | [optional] 

### Return type

[**StudentAnswer**](StudentAnswer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_retrieve**
> StudentAnswer ai_math_math_student_answers_retrieve(id, org)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.student_answer import StudentAnswer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this student answer.
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_math_math_student_answers_retrieve(id, org)
    print("The response of AiMathApi->ai_math_math_student_answers_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this student answer. | 
 **org** | **str**|  | 

### Return type

[**StudentAnswer**](StudentAnswer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_math_math_student_answers_update**
> StudentAnswer ai_math_math_student_answers_update(id, org, student_answer)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.student_answer import StudentAnswer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMathApi(api_client)
id = 56 # int | A unique integer value identifying this student answer.
org = 'org_example' # str | 
student_answer = iblai.StudentAnswer() # StudentAnswer | 

try:
    api_response = api_instance.ai_math_math_student_answers_update(id, org, student_answer)
    print("The response of AiMathApi->ai_math_math_student_answers_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMathApi->ai_math_math_student_answers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this student answer. | 
 **org** | **str**|  | 
 **student_answer** | [**StudentAnswer**](StudentAnswer.md)|  | 

### Return type

[**StudentAnswer**](StudentAnswer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

