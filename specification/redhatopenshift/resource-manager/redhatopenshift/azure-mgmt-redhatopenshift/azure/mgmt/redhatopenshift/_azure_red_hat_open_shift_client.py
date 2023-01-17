# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import AzureRedHatOpenShiftClientConfiguration
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class AzureRedHatOpenShiftClient(MultiApiClientMixin, _SDKClient):
    """Rest API for Azure Red Hat OpenShift 4.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2022-09-04'
    _PROFILE_TAG = "azure.mgmt.redhatopenshift.AzureRedHatOpenShiftClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version: Optional[str]=None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles=KnownProfiles.default,
        **kwargs: Any
    ):
        self._config = AzureRedHatOpenShiftClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(AzureRedHatOpenShiftClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2020-04-30: :mod:`v2020_04_30.models<azure.mgmt.redhatopenshift.v2020_04_30.models>`
           * 2021-09-01-preview: :mod:`v2021_09_01_preview.models<azure.mgmt.redhatopenshift.v2021_09_01_preview.models>`
           * 2022-04-01: :mod:`v2022_04_01.models<azure.mgmt.redhatopenshift.v2022_04_01.models>`
           * 2022-09-04: :mod:`v2022_09_04.models<azure.mgmt.redhatopenshift.v2022_09_04.models>`
        """
        if api_version == '2020-04-30':
            from .v2020_04_30 import models
            return models
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview import models
            return models
        elif api_version == '2022-04-01':
            from .v2022_04_01 import models
            return models
        elif api_version == '2022-09-04':
            from .v2022_09_04 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def machine_pools(self):
        """Instance depends on the API version:

           * 2022-09-04: :class:`MachinePoolsOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.MachinePoolsOperations>`
        """
        api_version = self._get_api_version('machine_pools')
        if api_version == '2022-09-04':
            from .v2022_09_04.operations import MachinePoolsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'machine_pools'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def open_shift_clusters(self):
        """Instance depends on the API version:

           * 2020-04-30: :class:`OpenShiftClustersOperations<azure.mgmt.redhatopenshift.v2020_04_30.operations.OpenShiftClustersOperations>`
           * 2021-09-01-preview: :class:`OpenShiftClustersOperations<azure.mgmt.redhatopenshift.v2021_09_01_preview.operations.OpenShiftClustersOperations>`
           * 2022-04-01: :class:`OpenShiftClustersOperations<azure.mgmt.redhatopenshift.v2022_04_01.operations.OpenShiftClustersOperations>`
           * 2022-09-04: :class:`OpenShiftClustersOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.OpenShiftClustersOperations>`
        """
        api_version = self._get_api_version('open_shift_clusters')
        if api_version == '2020-04-30':
            from .v2020_04_30.operations import OpenShiftClustersOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import OpenShiftClustersOperations as OperationClass
        elif api_version == '2022-04-01':
            from .v2022_04_01.operations import OpenShiftClustersOperations as OperationClass
        elif api_version == '2022-09-04':
            from .v2022_09_04.operations import OpenShiftClustersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'open_shift_clusters'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def open_shift_versions(self):
        """Instance depends on the API version:

           * 2022-09-04: :class:`OpenShiftVersionsOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.OpenShiftVersionsOperations>`
        """
        api_version = self._get_api_version('open_shift_versions')
        if api_version == '2022-09-04':
            from .v2022_09_04.operations import OpenShiftVersionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'open_shift_versions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2020-04-30: :class:`Operations<azure.mgmt.redhatopenshift.v2020_04_30.operations.Operations>`
           * 2021-09-01-preview: :class:`Operations<azure.mgmt.redhatopenshift.v2021_09_01_preview.operations.Operations>`
           * 2022-04-01: :class:`Operations<azure.mgmt.redhatopenshift.v2022_04_01.operations.Operations>`
           * 2022-09-04: :class:`Operations<azure.mgmt.redhatopenshift.v2022_09_04.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2020-04-30':
            from .v2020_04_30.operations import Operations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import Operations as OperationClass
        elif api_version == '2022-04-01':
            from .v2022_04_01.operations import Operations as OperationClass
        elif api_version == '2022-09-04':
            from .v2022_09_04.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def secrets(self):
        """Instance depends on the API version:

           * 2022-09-04: :class:`SecretsOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.SecretsOperations>`
        """
        api_version = self._get_api_version('secrets')
        if api_version == '2022-09-04':
            from .v2022_09_04.operations import SecretsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'secrets'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def sync_identity_providers(self):
        """Instance depends on the API version:

           * 2022-09-04: :class:`SyncIdentityProvidersOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.SyncIdentityProvidersOperations>`
        """
        api_version = self._get_api_version('sync_identity_providers')
        if api_version == '2022-09-04':
            from .v2022_09_04.operations import SyncIdentityProvidersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'sync_identity_providers'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def sync_sets(self):
        """Instance depends on the API version:

           * 2022-09-04: :class:`SyncSetsOperations<azure.mgmt.redhatopenshift.v2022_09_04.operations.SyncSetsOperations>`
        """
        api_version = self._get_api_version('sync_sets')
        if api_version == '2022-09-04':
            from .v2022_09_04.operations import SyncSetsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'sync_sets'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)