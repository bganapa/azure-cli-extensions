# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "devcenter admin pool update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a machine pool

    :example: Update
        az devcenter admin pool update --devbox-definition-name "WebDevBox2" --pool-name "{poolName}" --project-name "{projectName}" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2022-11-11-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/projects/{}/pools/{}", "2022-11-11-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.pool_name = AAZStrArg(
            options=["-n", "--name", "--pool-name"],
            help="Name of the pool.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project", "--project-name"],
            help="The name of the project. Use az configure -d project=<project_name> to configure a default.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.dev_box_definition_name = AAZStrArg(
            options=["-d", "--dev-box-definition-name"],
            arg_group="Properties",
            help="Name of a Dev Box definition in parent Project of this Pool",
        )
        _args_schema.local_administrator = AAZStrArg(
            options=["--local-administrator"],
            arg_group="Properties",
            help="Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.network_connection_name = AAZStrArg(
            options=["-c", "--network-connection-name"],
            arg_group="Properties",
            help="Name of a Network Connection in parent Project of this Pool",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PoolsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.PoolsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PoolsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/pools/{poolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-11-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_pool_read(cls._schema_on_200)

            return cls._schema_on_200

    class PoolsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/projects/{projectName}/pools/{poolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-11-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_pool_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("devBoxDefinitionName", AAZStrType, ".dev_box_definition_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("localAdministrator", AAZStrType, ".local_administrator", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("networkConnectionName", AAZStrType, ".network_connection_name", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_pool_read = None

    @classmethod
    def _build_schema_pool_read(cls, _schema):
        if cls._schema_pool_read is not None:
            _schema.id = cls._schema_pool_read.id
            _schema.location = cls._schema_pool_read.location
            _schema.name = cls._schema_pool_read.name
            _schema.properties = cls._schema_pool_read.properties
            _schema.system_data = cls._schema_pool_read.system_data
            _schema.tags = cls._schema_pool_read.tags
            _schema.type = cls._schema_pool_read.type
            return

        cls._schema_pool_read = _schema_pool_read = AAZObjectType()

        pool_read = _schema_pool_read
        pool_read.id = AAZStrType(
            flags={"read_only": True},
        )
        pool_read.location = AAZStrType(
            flags={"required": True},
        )
        pool_read.name = AAZStrType(
            flags={"read_only": True},
        )
        pool_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        pool_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        pool_read.tags = AAZDictType()
        pool_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_pool_read.properties
        properties.dev_box_definition_name = AAZStrType(
            serialized_name="devBoxDefinitionName",
            flags={"required": True},
        )
        properties.license_type = AAZStrType(
            serialized_name="licenseType",
            flags={"required": True},
        )
        properties.local_administrator = AAZStrType(
            serialized_name="localAdministrator",
            flags={"required": True},
        )
        properties.network_connection_name = AAZStrType(
            serialized_name="networkConnectionName",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        system_data = _schema_pool_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_pool_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_pool_read.id
        _schema.location = cls._schema_pool_read.location
        _schema.name = cls._schema_pool_read.name
        _schema.properties = cls._schema_pool_read.properties
        _schema.system_data = cls._schema_pool_read.system_data
        _schema.tags = cls._schema_pool_read.tags
        _schema.type = cls._schema_pool_read.type


__all__ = ["Update"]
