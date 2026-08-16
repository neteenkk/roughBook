"""
Two ideas define the pattern:

1. Step-by-step construction: Instead of passing everything to a constructor at once, 
you set each field through individual method calls. 
You only call the methods for the fields you need.

2.Fluent interface: Each setter method returns the builder itself, 
allowing you to chain calls into a single readable expression that ends with build().

- The Director is optional, and in many codebases you will not need one
Approach - Client uses Builder directly	
When to Use - One-off configurations, simple cases, or when each call site has unique requirements

Approach -  Director
When to Use - Multiple call sites need the same configuration, you want named presets, or construction logic is complex enough to warrant encapsulation

"""

class HttpRequest:
    def __init__(self, builder):
        self.url = builder._url
        self.method = builder._method
        self.headers = dict(builder._headers)  # defensive copy
        self.query_params = dict(builder._query_params)
        self.body = builder._body
        self.timeout = builder._timeout

    """
    __str__ is a special Python method that controls what gets
    displayed when you convert an object to a string, usually with print() or str().
    """
    def __str__(self):
        return (f"HttpRequest(url='{self.url}', method='{self.method}', "
                f"headers={self.headers}, query_params={self.query_params}, "
                f"body='{self.body}', timeout={self.timeout})")

    class Builder:
        def __init__(self, url):
            self._url = url  # required
            self._method = "GET"
            self._headers = {}
            self._query_params = {}
            self._body = None
            self._timeout = 30000

        def method(self, method):
            self._method = method
            return self

        def add_header(self, key, value):
            self._headers[key] = value
            return self

        def add_query_param(self, key, value):
            self._query_params[key] = value
            return self

        def body(self, body):
            self._body = body
            return self

        def timeout(self, timeout):
            self._timeout = timeout
            return self

        def build(self):
            return HttpRequest(self)


if __name__ == "__main__":
    get = HttpRequest.Builder("https://api/example.com/users").build()
    post = HttpRequest.Builder("https://api.example.com.users") \
                      .method("POST") \
                      .add_header("Content-Type", "application/json") \
                      .body('{"name": "Alice", "email":"alice@example.com"}') \
                      .timeout(5000) \
                      .build()

    print(get)
    print(post)