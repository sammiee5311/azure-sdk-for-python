# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_linked_services_by_workspace_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/linkedservices')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_linked_service_request_initial(
    linked_service_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    if_match = kwargs.pop('if_match', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/linkedservices/{linkedServiceName}')
    path_format_arguments = {
        "linkedServiceName": _SERIALIZER.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_linked_service_request(
    linked_service_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    if_none_match = kwargs.pop('if_none_match', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/linkedservices/{linkedServiceName}')
    path_format_arguments = {
        "linkedServiceName": _SERIALIZER.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_none_match is not None:
        header_parameters['If-None-Match'] = _SERIALIZER.header("if_none_match", if_none_match, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_linked_service_request_initial(
    linked_service_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/linkedservices/{linkedServiceName}')
    path_format_arguments = {
        "linkedServiceName": _SERIALIZER.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_rename_linked_service_request_initial(
    linked_service_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/linkedservices/{linkedServiceName}/rename')
    path_format_arguments = {
        "linkedServiceName": _SERIALIZER.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class LinkedServiceOperations(object):
    """LinkedServiceOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_linked_services_by_workspace(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.LinkedServiceListResponse"]
        """Lists linked services.

        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LinkedServiceListResponse or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.LinkedServiceListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LinkedServiceListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_linked_services_by_workspace_request(
                    api_version=api_version,
                    template_url=self.get_linked_services_by_workspace.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_get_linked_services_by_workspace_request(
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("LinkedServiceListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    get_linked_services_by_workspace.metadata = {'url': '/linkedservices'}  # type: ignore

    def _create_or_update_linked_service_initial(
        self,
        linked_service_name,  # type: str
        properties,  # type: "_models.LinkedService"
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LinkedServiceResource"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LinkedServiceResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _linked_service = _models.LinkedServiceResource(properties=properties)
        _json = self._serialize.body(_linked_service, 'LinkedServiceResource')

        request = build_create_or_update_linked_service_request_initial(
            linked_service_name=linked_service_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self._create_or_update_linked_service_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_linked_service_initial.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore


    @distributed_trace
    def begin_create_or_update_linked_service(
        self,
        linked_service_name,  # type: str
        properties,  # type: "_models.LinkedService"
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LinkedServiceResource"]
        """Creates or updates a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param properties: Properties of linked service.
        :type properties: ~azure.synapse.artifacts.models.LinkedService
        :param if_match: ETag of the linkedService entity.  Should only be specified for update, for
         which it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either LinkedServiceResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.LinkedServiceResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LinkedServiceResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_linked_service_initial(
                linked_service_name=linked_service_name,
                properties=properties,
                if_match=if_match,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('LinkedServiceResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore

    @distributed_trace
    def get_linked_service(
        self,
        linked_service_name,  # type: str
        if_none_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LinkedServiceResource"]
        """Gets a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param if_none_match: ETag of the linked service entity. Should only be specified for get. If
         the ETag matches the existing entity tag, or if * was provided, then no content will be
         returned.
        :type if_none_match: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.LinkedServiceResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LinkedServiceResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_get_linked_service_request(
            linked_service_name=linked_service_name,
            api_version=api_version,
            if_none_match=if_none_match,
            template_url=self.get_linked_service.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore


    def _delete_linked_service_initial(
        self,
        linked_service_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_delete_linked_service_request_initial(
            linked_service_name=linked_service_name,
            api_version=api_version,
            template_url=self._delete_linked_service_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_linked_service_initial.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore


    @distributed_trace
    def begin_delete_linked_service(
        self,
        linked_service_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Deletes a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_linked_service_initial(
                linked_service_name=linked_service_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore

    def _rename_linked_service_initial(
        self,
        linked_service_name,  # type: str
        new_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _request = _models.ArtifactRenameRequest(new_name=new_name)
        _json = self._serialize.body(_request, 'ArtifactRenameRequest')

        request = build_rename_linked_service_request_initial(
            linked_service_name=linked_service_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._rename_linked_service_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _rename_linked_service_initial.metadata = {'url': '/linkedservices/{linkedServiceName}/rename'}  # type: ignore


    @distributed_trace
    def begin_rename_linked_service(
        self,
        linked_service_name,  # type: str
        new_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Renames a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param new_name: New name of the artifact.
        :type new_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._rename_linked_service_initial(
                linked_service_name=linked_service_name,
                new_name=new_name,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_rename_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}/rename'}  # type: ignore
