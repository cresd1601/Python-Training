from rest_framework.pagination import PageNumberPagination


class QueryParamsPagination(PageNumberPagination):
    # Default page size when 'page_size' is not provided
    page_size = 10
    
    # Allow the client to override page size by passing ?page_size= in the query
    page_size_query_param = 'page_size'

    # Maximum limit for page size to prevent abuse
    max_page_size = 100