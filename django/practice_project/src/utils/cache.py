import hashlib


def default_cache_key_func(view_instance, view_method, request, args, kwargs) -> str:
    resources_and_ids = extract_resources_and_ids_from_path(request)
    query_params = extract_query_params_from_path(request)

    namespaces = build_namespace_from_resources(resources_and_ids, query_params)

    return namespaces


def default_list_cache_key_func(self, view_method, request, args, **kwargs) -> str:
    resources_and_ids = extract_resources_and_ids_from_path(request)
    query_params = extract_query_params_from_path(request)

    namespaces = build_namespace_from_resources(resources_and_ids, query_params)

    return namespaces


def default_object_cache_key_func(
    self, view_instance, view_method, request, args, kwargs
) -> str:
    resources_and_ids = extract_resources_and_ids_from_path(request)
    query_params = extract_query_params_from_path(request)

    namespaces = build_namespace_from_resources(resources_and_ids, query_params)

    return namespaces


def generate_hash(input_string):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the input string encoded to bytes
    hash_object.update(input_string.encode("utf-8"))

    # Get the hexadecimal representation of the hash
    hashed_value = hash_object.hexdigest()

    return hashed_value


def build_namespace_from_resources(resources_and_ids, query_params):
    """
    Builds a namespace string from a list of resource-ID dictionaries, appending query parameters
    in the format 'resource:id:params:key=value&key=value' if the resource ID is None.
    If no query parameters are provided, it will append an empty 'params:' segment.

    Args:
        resources_and_ids: List of dictionaries in the format [{'resource': id}, ...]
        query_params: Dictionary of query parameters (optional, used only when resource_id is None).

    Returns:
        string: A namespace string in the format 'resource:id' or 'resource' if ID is None,
                with query parameters appended as a 'params' segment.
    """
    namespaces = []

    # Build the base namespace from resources and IDs
    for resource_dict in resources_and_ids:
        for resource, resource_id in resource_dict.items():
            # If resource_id is None, return just the resource name and add params:
            if resource_id is None:
                query_str = "&".join(
                    [f"{key}={value}" for key, value in query_params.items()]
                )

                # Generate a hash for the query string
                hashed_query_string = generate_hash(query_str)
                namespaces.append(f"{resource}:params:{hashed_query_string}")
            else:
                # Generate a hash for the resource ID
                hashed_resource_id = generate_hash(resource_id)
                namespaces.append(f"{resource}:{hashed_resource_id}")

    # Convert to a single string (join with colon)
    return ":".join(namespaces)


def extract_resources_and_ids_from_path(request):
    """
    Extracts resources and their IDs from a request's URL path, excluding the 'api' segment if it's the first.
    If no ID is present for a resource, it returns None for that resource.

    Args:
        request: Django HTTP request object.

    Returns:
        list of dictionaries: [{'resource': id}, ...] where resource is the name and id is the associated value or None.
    """

    # Split the URL path into individual segments, removing any empty segments
    path_segments = [segment for segment in request.path.split("/") if segment]

    # If the path starts with 'api', remove it
    if path_segments and path_segments[0] == "api":
        path_segments.pop(0)

    # Initialize an empty list to store the resource-ID pairs
    resources_and_ids = []

    # Iterate through the path segments in steps of 2 (resource and ID)
    for i in range(0, len(path_segments), 2):
        # Resource is at the even index (0, 2, 4, ...)
        resource = path_segments[i]

        # Check if the next segment exists, if not, assign None for the ID
        resource_id = path_segments[i + 1] if i + 1 < len(path_segments) else None

        # Add the resource and its ID (or None) as a dictionary to the result list
        resources_and_ids.append({resource: resource_id})

    return resources_and_ids


def extract_query_params_from_path(request):
    """
    Extracts query parameters from a request's URL path.

    Args:
        request: Django HTTP request object.

    Returns:
        dict: Dictionary of query parameters.
    """

    # Convert the QueryDict to a dictionary
    query_params = request.query_params.dict()

    # Convert the QueryDict to a dictionary and sort it
    sorted_query_params = dict(sorted(query_params.items()))

    return sorted_query_params
