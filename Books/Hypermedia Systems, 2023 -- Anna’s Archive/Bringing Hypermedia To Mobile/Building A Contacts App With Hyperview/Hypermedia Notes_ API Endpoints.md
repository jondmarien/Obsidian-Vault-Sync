# Hypermedia Notes: API Endpoints

Unlike a JSON API, the hypermedia API you produce for your hypermedia-driven application should feature endpoints specialized for your particular application’s UI needs.

Because hypermedia APIs are not designed to be consumed by general-purpose clients you can set aside the pressure to keep them generalized and produce the content specifically needed for your application. Your endpoints should be optimized to support your particular applications UI/UX needs, not for a general-purpose data-access model for your domain model.

A related tip is that, when you have a hypermedia-based API, you can aggressively refactor your API in a way that is heavily discouraged when writing JSON API-based SPAs or mobile clients. Because hypermedia-based applications use Hypermedia As The Engine Of Application State, you are able and, in fact, encouraged, to change the shape of them as your application developers and as use cases change.

A great strength of the hypermedia approach is that you can completely rework your API to adapt to new needs over time without needing to version the API or even document it. Take advantage of it!