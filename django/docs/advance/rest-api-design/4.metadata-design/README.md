# Chapter 4: Metadata Design

Chapter 4 of "REST API Design Rulebook" focuses on metadata design in REST APIs, which involves utilizing HTTP headers, media types, and other elements to provide additional information for both clients and servers.

## Key Concepts & Examples:

### HTTP Headers:

HTTP headers are a crucial part of HTTP messages, conveying additional information beyond the main content of a request or response.

#### Rules:

- **Use Content-Type**: The `Content-Type` header specifies the data format of the content being transmitted in a request or response.

  **Example**:  
  `Content-Type: application/json` indicates that the content is JSON data.

- **Use Content-Length**: The `Content-Length` header indicates the size of the content being transmitted.

  **Example**:  
  `Content-Length: 1234` indicates the content is 1234 bytes.

- **Use Last-Modified**: The `Last-Modified` header indicates the last time a resource was modified.

  **Example**:  
  `Last-Modified: Thu, 01 Dec 1994 16:00:00 GMT` indicates the resource was last updated on December 1st, 1994 at 4:00 PM GMT.

- **Use ETag**: The `ETag` header is a unique identifier for a specific version of a resource.

  **Example**:  
  `ETag: "text/html:hello world"` identifies the version of the resource as "text/html:hello world".

- **Stores must support conditional PUT requests**: To prevent conflicts during updates to resources stored in a store, the server should support conditional `PUT` requests.

  **Example**:  
  Clients can send `PUT` requests with the `If-Unmodified-Since` header to specify the last modification time of a resource, or `If-Match` to specify the resource's version, ensuring the resource hasn't been modified before the update is attempted.

- **Use Location**: The `Location` header contains the URI of the newly created resource.

  **Example**:  
  After creating a new user, the server might return a `201 Created` response with `Location: http://api.example.com/users/123`, indicating the URI of the newly created user.

- **Use Cache-Control, Expires, and Date to encourage caching**: To optimize performance, you can encourage browsers to cache resources.

  **Example**:  
  `Cache-Control: max-age=60, must-revalidate` indicates that the resource can be cached for 60 seconds and must be revalidated after 60 seconds.

- **Use Cache-Control, Expires, and Pragma to discourage caching**: To prevent browsers from caching sensitive resources, use these headers.

  **Example**:  
  `Cache-Control: no-cache, no-store` prevents the resource from being cached.

- **Use expiration caching headers for successful responses (200 OK)**: Optimize performance by using expiration caching headers for `200 OK` responses.

- **Expiration caching headers can be used optionally for 3xx and 4xx responses**: This helps reduce server load by minimizing unnecessary resource requests.

- **Do not use custom HTTP headers to change the behavior of HTTP methods**: Avoid using custom headers to change the behavior of HTTP methods.

  **Example**:  
  Do not use a custom header to bypass authentication for a `POST` request.

### Media Types:

Media types are used to identify the data format being transmitted.

#### Rules:

- **Use specific media types for each data format**: Ensure both clients and servers understand the data format.

  **Example**:  
  Use `application/json` for JSON data, `application/xml` for XML data, `text/html` for HTML content, etc.

- **Create media types specific to your application**: This ensures consistency and independence for your API.

  **Example**:  
  Create a media type like `application/vnd.company.your-api+json` for your company's API.

- **Support media type negotiation**: Allow clients to specify their preferred media type using the `Accept` header.

- **Use media types to represent formats**:

  **Example**:  
  `application/vnd.company.your-api+json; format="http://api.formats.wrml.org/application/json"` indicates that the format is JSON.

- **Use media types to represent schemas**:

  **Example**:  
  `application/vnd.company.your-api+json; schema="http://api.schemas.wrml.org/your-api/user"` defines the schema for the "user" resource in the API.

### Advanced Rules:

- **Create separate resources to describe formats**: Create a resource to describe the format of a media type, helping clients understand how to use it.
- **Create separate resources to describe schemas**: Create a resource to describe the schema of a media type, helping clients understand the structure of the resource.

#### Example:

- **Response with JSON**:

  `Content-Type: application/json`

- **Response with XML**:

  `Content-Type: application/xml`

- **Response with HTML**:

  `Content-Type: text/html`
