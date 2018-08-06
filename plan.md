## K8s

* K8s-Class
	* create(api_verision, object_type, **kwargs)
		> API_GROUPS[api_verision][object_type]["create"](**kwargs)
	* delete()
	* list()
	* get()
	* read()
	* patch()
	* replace()
	* connect()
*
API_GROUPS = {
    "AdmissionregistrationApi": {
        "api_group": {
            "get": "get_api_group"
        },
    },
    "AdmissionregistrationV1alpha1Api": {
        "initializer_configuration": {
            "create": "create_initializer_configuration",
            "delete": "delete_initializer_configuration",
            "list": "list_initializer_configuration",
            "patch":"patch_initializer_configuration",
            "read":"read_initializer_configuration",
            "replace":"	replace_initializer_configuration",
        },
        "collection_initializer_configuration": {
            "delete":"delete_collection_initializer_configuration",
        },
        "api_resources"{
            "get":"get_api_resources",
        },

    },
    "ApiextensionsApi": {},
    "ApiextensionsV1beta1Api": {},
}
