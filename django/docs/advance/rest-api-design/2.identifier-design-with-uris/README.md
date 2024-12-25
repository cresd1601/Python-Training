# Chapter 2: Identifier Design with URIs

This chapter dives deep into crafting clear and meaningful URIs (Uniform Resource Identifiers) for REST APIs. It emphasizes the importance of well-structured URIs that effectively communicate the API's resource model to both humans and machines, leading to improved API consistency, readability, and maintainability.

## Key Concepts & Examples:

### URI Format:

The chapter outlines rules for formatting URIs to ensure consistency and readability:

#### Hierarchical Structure:

The forward slash (/) is used to create a hierarchical structure, similar to file directories.

**Example**:  
Consider a REST API for managing an online store. The URI `http://api.store.com/products/123/reviews` would indicate the reviews for a product with ID 123, clearly outlining the relationship between the product and its reviews.

#### Trailing Slashes:

Trailing slashes (/) are generally discouraged as they don't add semantic meaning.

**Example**:  
`http://api.store.com/products/123` is preferred over `http://api.store.com/products/123/`.

#### Readability and Hyphens:

Hyphens (-) are used for readability in long path segments.

**Example**:  
`http://api.store.com/products/new-product` is more readable than `http://api.store.com/products/newproduct`.

#### Case Sensitivity:

Lowercase letters are recommended for path segments.

**Example**:  
`http://api.store.com/products` is generally better than `http://api.store.com/PRODUCTS`.

#### File Extensions:

File extensions should be avoided in URIs; rely on media types instead to indicate the format of a resource.

**Example**:  
`http://api.store.com/products/123` is preferred over `http://api.store.com/products/123.json`.

### URI Authority Design:

This section covers how to use subdomain names effectively:

- **Consistent Subdomain Names**: Subdomains should be used consistently to identify the API's service owner (e.g., `api.store.com`) and developer portal (e.g., `developer.store.com`).

### Resource Modeling:

The importance of creating a clear resource model for the API is highlighted:

#### Resource Archetypes:

Four fundamental resource archetypes are introduced:

1. **Document**: Represents a single instance or entity (e.g., a user profile with `/users/123`).
2. **Collection**: Represents a list of documents (e.g., all users with `/users`).
3. **Store**: Represents a client-managed repository (e.g., a user's cart with `/users/123/cart`).
4. **Controller**: Represents an executable function or process (e.g., a login process with `/login`).

### URI Path Design:

This section provides rules for creating meaningful and consistent URI paths based on the resource model:

- **Singular vs. Plural Nouns**: Singular nouns are used for documents (e.g., `/user/123`), and plural nouns for collections (e.g., `/users`).
- **Verbs for Controllers**: Verbs should be used to name controllers (e.g., `/login`, `/logout`).
- **Variable Path Segments**: Variable segments (e.g., `/users/{id}`) allow for flexibility and dynamic URIs (e.g., `/users/{id}/orders`).
- **CRUD Functions**: CRUD functions should not be explicitly represented in URIs (e.g., `DELETE /users/123` is preferred over `DELETE /users/123/delete`).

### URI Query Design:

This section focuses on designing effective URI queries for filtering, paging, and searching resources:

- **Filtering**: Query parameters (e.g., `?role=admin`) can filter collections (e.g., `/users?role=admin`).
- **Pagination**: Parameters like `pageSize` and `pageStartIndex` can paginate resources (e.g., `/users?pageSize=10&pageStartIndex=20`).
- **Searching**: Query parameters (e.g., `?q=javascript`) can be used for searching (e.g., `/products?q=shoes`).
