# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class WorkbookTemplateResource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(WorkbookTemplateResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class WorkbookTemplate(WorkbookTemplateResource):
    """An Application Insights workbook template definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param priority: Priority of the template. Determines which template to open when a workbook
     gallery is opened in viewer mode.
    :type priority: int
    :param author: Information about the author of the workbook template.
    :type author: str
    :param template_data: Valid JSON object containing workbook template payload.
    :type template_data: any
    :param galleries: Workbook galleries supported by the template.
    :type galleries:
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateGallery]
    :param localized: Key value pair of localized gallery. Each key is the locale code of languages
     supported by the Azure portal.
    :type localized: dict[str,
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateLocalizedGallery]]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'template_data': {'key': 'properties.templateData', 'type': 'object'},
        'galleries': {'key': 'properties.galleries', 'type': '[WorkbookTemplateGallery]'},
        'localized': {'key': 'properties.localized', 'type': '{[WorkbookTemplateLocalizedGallery]}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        priority: Optional[int] = None,
        author: Optional[str] = None,
        template_data: Optional[Any] = None,
        galleries: Optional[List["WorkbookTemplateGallery"]] = None,
        localized: Optional[Dict[str, List["WorkbookTemplateLocalizedGallery"]]] = None,
        **kwargs
    ):
        super(WorkbookTemplate, self).__init__(location=location, tags=tags, **kwargs)
        self.priority = priority
        self.author = author
        self.template_data = template_data
        self.galleries = galleries
        self.localized = localized


class WorkbookTemplateError(msrest.serialization.Model):
    """Error message that will indicate why the operation failed.

    :param error: Error message object that will indicate why the operation failed.
    :type error: ~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'WorkbookTemplateErrorBody'},
    }

    def __init__(
        self,
        *,
        error: Optional["WorkbookTemplateErrorBody"] = None,
        **kwargs
    ):
        super(WorkbookTemplateError, self).__init__(**kwargs)
        self.error = error


class WorkbookTemplateErrorBody(msrest.serialization.Model):
    """Error message body that will indicate why the operation failed.

    :param code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    :param details: The list of invalid fields send in request, in case of validation error.
    :type details:
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateErrorFieldContract]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[WorkbookTemplateErrorFieldContract]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        details: Optional[List["WorkbookTemplateErrorFieldContract"]] = None,
        **kwargs
    ):
        super(WorkbookTemplateErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details


class WorkbookTemplateErrorFieldContract(msrest.serialization.Model):
    """Error Field contract.

    :param code: Property level error code.
    :type code: str
    :param message: Human-readable representation of property-level error.
    :type message: str
    :param target: Property name.
    :type target: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(WorkbookTemplateErrorFieldContract, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class WorkbookTemplateGallery(msrest.serialization.Model):
    """Gallery information for a workbook template.

    :param name: Name of the workbook template in the gallery.
    :type name: str
    :param category: Category for the gallery.
    :type category: str
    :param type: Type of workbook supported by the workbook template.
    :type type: str
    :param order: Order of the template within the gallery.
    :type order: int
    :param resource_type: Azure resource type supported by the gallery.
    :type resource_type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        order: Optional[int] = None,
        resource_type: Optional[str] = None,
        **kwargs
    ):
        super(WorkbookTemplateGallery, self).__init__(**kwargs)
        self.name = name
        self.category = category
        self.type = type
        self.order = order
        self.resource_type = resource_type


class WorkbookTemplateLocalizedGallery(msrest.serialization.Model):
    """Localized template data and gallery information.

    :param template_data: Valid JSON object containing workbook template payload.
    :type template_data: any
    :param galleries: Workbook galleries supported by the template.
    :type galleries:
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateGallery]
    """

    _attribute_map = {
        'template_data': {'key': 'templateData', 'type': 'object'},
        'galleries': {'key': 'galleries', 'type': '[WorkbookTemplateGallery]'},
    }

    def __init__(
        self,
        *,
        template_data: Optional[Any] = None,
        galleries: Optional[List["WorkbookTemplateGallery"]] = None,
        **kwargs
    ):
        super(WorkbookTemplateLocalizedGallery, self).__init__(**kwargs)
        self.template_data = template_data
        self.galleries = galleries


class WorkbookTemplatesListResult(msrest.serialization.Model):
    """WorkbookTemplate list result.

    :param value: An array of workbook templates.
    :type value: list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplate]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[WorkbookTemplate]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["WorkbookTemplate"]] = None,
        **kwargs
    ):
        super(WorkbookTemplatesListResult, self).__init__(**kwargs)
        self.value = value


class WorkbookTemplateUpdateParameters(msrest.serialization.Model):
    """The parameters that can be provided when updating workbook template.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param priority: Priority of the template. Determines which template to open when a workbook
     gallery is opened in viewer mode.
    :type priority: int
    :param author: Information about the author of the workbook template.
    :type author: str
    :param template_data: Valid JSON object containing workbook template payload.
    :type template_data: any
    :param galleries: Workbook galleries supported by the template.
    :type galleries:
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateGallery]
    :param localized: Key value pair of localized gallery. Each key is the locale code of languages
     supported by the Azure portal.
    :type localized: dict[str,
     list[~azure.mgmt.applicationinsights.v2020_11_20.models.WorkbookTemplateLocalizedGallery]]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'template_data': {'key': 'properties.templateData', 'type': 'object'},
        'galleries': {'key': 'properties.galleries', 'type': '[WorkbookTemplateGallery]'},
        'localized': {'key': 'properties.localized', 'type': '{[WorkbookTemplateLocalizedGallery]}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        priority: Optional[int] = None,
        author: Optional[str] = None,
        template_data: Optional[Any] = None,
        galleries: Optional[List["WorkbookTemplateGallery"]] = None,
        localized: Optional[Dict[str, List["WorkbookTemplateLocalizedGallery"]]] = None,
        **kwargs
    ):
        super(WorkbookTemplateUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.priority = priority
        self.author = author
        self.template_data = template_data
        self.galleries = galleries
        self.localized = localized
