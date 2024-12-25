# Chapter 3: Interaction Design with HTTP

This chapter dives deep into designing the interaction between clients and servers in REST APIs using the HTTP (HyperText Transfer Protocol). It focuses on using HTTP methods, response status codes, and specific rules to create a consistent, user-friendly, and maintainable REST API.

## Key Concepts & Examples:

### HTTP Methods:

This section introduces HTTP methods and how to use them to define the action a client wants to perform on a resource in a REST API.

#### Common HTTP Methods:

- **GET**: Retrieve a resource.

  **Example**:  
  `GET /users` to fetch a list of users.

- **POST**: Create a new resource, execute a controller.

  **Example**:  
  `POST /users` to create a new user.  
  `POST /login` to initiate a login process.

- **PUT**: Update a resource.

  **Example**:  
  `PUT /users/123` to update the information for the user with ID 123.

- **DELETE**: Delete a resource.

  **Example**:  
  `DELETE /users/123` to delete the user with ID 123.

- **HEAD**: Get the headers of a resource.

  **Example**:  
  `HEAD /users/123` to get the headers of the user with ID 123 (often used to check if a resource exists).

- **OPTIONS**: Get information about allowed methods for a resource.

  **Example**:  
  `OPTIONS /users/123` to see which HTTP methods are allowed on the user resource with ID 123.

### Rules:

- Avoid using **GET** and **POST** to tunnel other HTTP methods (tunneling):

  **Example**:  
  Avoid using `GET` to perform a `DELETE` operation by encoding DELETE information in the URI query.

- Don't use **POST** for CRUD operations (Create, Read, Update, Delete):

  **Example**:  
  Use `PUT` to update a resource (`PUT /users/123`) instead of `POST /users/123/update`.

- Use the right HTTP method for each action: This ensures REST API consistency and clarity.

### Response Status Codes:

Response status codes are used by servers to inform clients about the result of a request.

#### Common Response Status Codes:

- **200 OK**: Request successful.
- **201 Created**: New resource creation successful.
- **202 Accepted**: Request accepted for asynchronous processing.
- **204 No Content**: Request successful, but no content in the response.
- **301 Moved Permanently**: Resource URI permanently changed.
- **302 Found**: Resource URI temporarily changed.
- **303 See Other**: Redirect the request to a different URI.
- **304 Not Modified**: Resource content has not changed.
- **400 Bad Request**: Invalid request.
- **401 Unauthorized**: Unauthorized access.
- **403 Forbidden**: Access forbidden.
- **404 Not Found**: Resource not found.
- **405 Method Not Allowed**: HTTP method not allowed.
- **406 Not Acceptable**: Unsupported media type.
- **409 Conflict**: Conflict occurred during the operation.
- **412 Precondition Failed**: Precondition failed.
- **415 Unsupported Media Type**: Unsupported media type.
- **500 Internal Server Error**: Server error.

#### Note:

Use appropriate status codes to provide clear feedback to clients.

#### Example:

- **GET /users**:

  **Response**:  
  `200 OK` with a list of users in JSON.

- **POST /users**:

  **Response**:  
  `201 Created` with the URI of the newly created user.

- **PUT /users/123**:

  **Response**:  
  `200 OK` if successful, or `400 Bad Request` if the request is invalid.

- **DELETE /users/123**:

  **Response**:  
  `204 No Content` if deletion was successful.
