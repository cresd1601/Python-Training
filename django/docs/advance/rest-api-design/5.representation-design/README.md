# Chapter 5: Representation Design

Chapter 5 of "REST API Design Rulebook" focuses on designing and managing representations of resources in REST APIs.

## Key Concepts & Examples:

### Message Body Format:

This section deals with how data is transmitted in the body of HTTP requests or responses.

#### Rules:

- **Use JSON to represent resources**: JSON is a popular and flexible format for representing resources.

  **Example**:  
  `{"firstName": "John", "lastName": "Doe", "age": 30}` represents a user resource in JSON.

- **Use XML and other formats optionally**: XML and other formats can be used to represent resources, but JSON is generally preferred.

  **Example**:  
  `<user><firstName>John</firstName><lastName>Doe</lastName><age>30</age></user>` represents a user resource in XML.

- **Don't add additional wrapping**: Transmit the resource representation directly, avoiding unnecessary wrapping.

### Hypermedia Representation:

Hypermedia involves connecting resources to each other through links. Using hypermedia makes it easier for clients to navigate and interact with resources in REST APIs.

#### Rules:

- **Use a consistent format to represent links**: Use a consistent format to represent links for clarity and ease of processing for both clients and servers.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/Link"` to represent links.

- **Use a consistent format to represent link relations**: Use a consistent format to represent link relations, for clarity and ease of processing.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/LinkRelation"` to represent link relations.

- **Use a consistent format to advertise links**: Use a consistent format to advertise links, making it easier for clients to discover and use them.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/Link"` and a links structure to list links in the representation.

- **Include the "self" link in resource representations**: The "self" link points to the current resource, making it easy for clients to access the resource again.

- **Minimize the number of advertised "entry point" URIs**: Limit the number of "entry point" URIs (URLs that act as starting points for navigation) in your API to make navigation easier.

- **Use links to advertise available actions for resources in a state-sensitive manner**: Use links to advertise the actions a client can perform on a resource based on its current state.

### Media Type Representation:

Media types identify the data format being transmitted in a REST API.

#### Rules:

- **Use a consistent format to represent media types**: Use a consistent format to represent media types, ensuring clarity and ease of processing for both clients and servers.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/Format"` to represent media types.

- **Use a consistent format to represent schemas**: Use a consistent format to represent schemas, for clarity and ease of processing.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/Schema"` to represent schemas.

### Error Representation:

Errors occur when a client request is not successful.

#### Rules:

- **Use a consistent format to represent errors**: Use a consistent format to represent errors for clarity and ease of processing.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/Error"` to represent errors.

- **Use a consistent format to represent error responses**: Use a consistent format to represent error responses for clarity and ease of processing.

  **Example**:  
  Use `application/vnd.company.your-api+json` with a schema `schema="http://api.schemas.wrml.org/common/ErrorContainer"` to represent error responses.

### Examples:

#### User Resource Representation in JSON:

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 30,
  "links": [
    {
      "href": "http://api.example.com/users/123",
      "rel": "self"
    },
    {
      "href": "http://api.example.com/users/123/posts",
      "rel": "posts"
    }
  ]
}
```

#### Link Representation:

```json
{
  "href": "http://api.example.com/users/123",
  "rel": "self"
}
```

#### Link Relation Representation:

```json
{
  "name": "self",
  "description": "This link points to the current resource."
}
```

#### Error Representation:

```json
{
  "id": "404",
  "description": "Resource not found."
}
```

#### Error Response Representation:

```json
{
  "errors": [
    {
      "id": "404",
      "description": "Resource not found."
    }
  ]
}
```
