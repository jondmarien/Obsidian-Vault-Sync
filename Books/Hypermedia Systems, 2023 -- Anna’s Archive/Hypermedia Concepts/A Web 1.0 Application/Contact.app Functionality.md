# Contact.app Functionality

Now that we have some understanding of how to define routes, let’s get down to specifying and then implementing our web application.

What will Contact.app do?

Initially, it will allow users to:

*   View a list of contacts, including first name, last name, phone and email address- Search the contacts- Add a new contact- View the details of a contact- Edit the details of a contact- Delete a contact

So, as you can see, Contact.app is a CRUD application, the sort of application that is perfect for an old-school web 1.0 approach.

Note that the source code of Contact.app is available on [GitHub](https://github.com/bigskysoftware/contact-app).

## Showing A Searchable List Of Contacts

Let’s add our first real bit of functionality: the ability to show all the contacts in our app in a list (really, in a table).

This functionality is going to be found at the `/contacts` path, which is the path our previous route is redirecting to.

We will use Flask to route the `/contacts` path to a handler function, `contacts()`. This function will do one of two things:

*   If there is a search term found in the request, it will filter down to only contacts matching that term
    
*   If not, it will simply list all contacts

This is a common approach in web 1.0 style applications: the same URL that displays all instances of some resource also serves as the search results page for those resources. Taking this approach makes it easy to reuse the list display that is common to both types of request.

Here is what the code looks like for this handler:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q") <1>
        if search is not None:
            contacts_set = Contact.search(search) <2>
        else:
            contacts_set = Contact.all() <3>
        return render_template("index.html", contacts=contacts_set)

A handler for server-side search

1.  Look for the query parameter named `q`, which stands for “query.”
    
2.  If the parameter exists, call the `Contact.search()` function with it.
    
3.  If not, call the `Contact.all()` function.
    
4.  Pass the result to the `index.html` template to render to the client.

We see the same sort of routing code we saw in our first example, but we have a more elaborate handler function. First, we check to see if a search query parameter named `q` is part of the request.

Query Strings

A “query string” is part of the URL specification. Here is an example URL with a query string in it: `https://example.com/contacts?q=joe`. The query string is everything after the `?`, and has a name-value pair format. In this URL, the query parameter `q` is set to the string value `joe`. In plain HTML, a query string can be included in a request either by being hardcoded in an anchor tag or, more dynamically, by using a form tag with a `GET` request.

To return to our Flask route, if a query parameter named `q` is found, we call out to the `search()` method on a `Contact` model object to do the actual contact search and return all the matching contacts.

If the query parameter is _not_ found, we simply get all contacts by invoking the `all()` method on the `Contact` object.

Finally, we render a template, `index.html` that displays the given contacts, passing in the results of whichever of these two functions we end up calling.

**A Note On The Contact Class**

The `Contact` Python class we’re using is the “domain model” or just “model” class for our application, providing the “business logic” around the management of Contacts.

It could be working with a database (it isn’t) or a simple flat file (it is), but we’re going to skip over the internal details of the model. Think of it as a “normal” domain model class, with methods on it that act in a “normal” manner.

We will treat `Contact` as a _resource_, and focus on how to effectively provide hypermedia representations of that resource to clients.

### The list & search templates

Now that we have our handler logic written, we’ll create a template to render HTML in our response to the client. At a high level, our HTML response needs to have the following elements:

*   A list of any matching or all contacts.
    
*   A search box where a user may type and submit search terms.
    
*   A bit of surrounding “chrome”: a header and footer for the website that will be the same regardless of the page you are on.

We are using the Jinja2 templating language, which has the following features:

*   We can use double-curly braces, `{{ }}`, to embed expression values in the template.
    
*   we can use curly-percents, `{% %}`, for directives, like iteration or including other content.

Beyond this basic syntax, Jinja2 is very similar to other templating languages used to generate content, and should be easy to follow for most web developers.

Let’s look at the first few lines of code in the `index.html` template:

    {% extends 'layout.html' %} <1>
    
    {% block content %} <2>
    
      <form action="/contacts" method="get" class="tool-bar"> <3>
        <label for="search">Search Termlabel>
        <input id="search" type="search" name="q"
          value="{{ request.args.get('q') or '' }}" /> <4>
        <input type="submit" value="Search"/>
      form>

Start of index.html

1.  Set the layout template for this template.
    
2.  Delimit the content to be inserted into the layout.
    
3.  Create a search form that will issue an HTTP `GET` to `/contacts`.
    
4.  Create an input for a user to type search queries.

The first line of code references a base template, `layout.html`, with the `extends` directive. This layout template provides the layout for the page (again, sometimes called “the chrome”): it wraps the template content in an tag, imports any necessary CSS and JavaScript in a element, places a tag around the main content and so forth. All the common content wrapped around the “normal” content for the entire application is located in this file.

The next line of code declares the `content` section of this template. This content block is used by the `layout.html` template to inject the content of `index.html` within its HTML.

Next we have our first bit of actual HTML, rather than just Jinja directives. We have a simple HTML form that allows you to search contacts by issuing a `GET` request to the `/contacts` path. The form itself contains a label and an input with the name “q.” This input’s value will be submitted with the `GET` request to the `/contacts` path, as a query string (since this is a `GET` request.)

Note that the value of this input is set to the Jinja expression `{{ request.args.get('q') or '' }}`. This expression is evaluated by Jinja and will insert the request value of “q” as the input’s value, if it exists. This will “preserve” the search value when a user does a search, so that when the results of a search are rendered the text input contains the term that was searched for. This makes for a better user experience since the user can see exactly what the current results match, rather than having a blank text box at the top of the screen.

Finally, we have a submit-type input. This will render as a button and, when it is clicked, it will trigger the form to issue an HTTP request.

This search interface forms the top of our contact page. Following it is a table of contacts, either all contacts or the contacts that match the search, if a search was done.

Here is what the template code for the contact table looks like:

    <table>
      <thead>
      <tr>
        <th>First <th>Last <th>Phone <th>Email <th/> <1>
      tr>
      thead>
      <tbody>
      {% for contact in contacts %} <2>
        <tr>
          <td>{{ contact.first }}td>
          <td>{{ contact.last }}td>
          <td>{{ contact.phone }}td>
          <td>{{ contact.email }}td> <3>
          <td><a href="/contacts/{{ contact.id }}/edit">Edita>
            <a href="/contacts/{{ contact.id }}">Viewa>td> <4>
        tr>
      {% endfor %}
      tbody>
    table>

The contacts table

*   Output some headers for our table.
    
*   Iterate over the contacts that were passed in to the template.
    
*   Output the values of the current contact, first name, last name, etc.
    
*   An “operations” column, with links to edit or view the contact details.

This is the core of the page: we construct a table with appropriate headers matching the data we are going to show for each contact. We iterate over the contacts that were passed into the template by the handler method using the `for` loop directive in Jinja2. We then construct a series of rows, one for each contact, where we render the first and last name, phone and email of the contact as table cells in the row.

Additionally, we have a table cell that includes two links:

*   A link to the “Edit” page for the contact, located at `/contacts/{{ contact.id }}/edit` (e.g., For the contact with id 42, the edit link will point to `/contacts/42/edit`)
    
*   A link to the “View” page for the contact `/contacts/{{ contact.id }}` (using our previous contact example, the view page would be at `/contacts/42`)

Finally, we have a bit of end-matter: a link to add a new contact and a Jinja2 directive to end the `content` block:

    <p>
        <a href="/contacts/new">Add Contacta> <1>
      p>
    
    {% endblock %} <2>

The “add contact” link

1.  Link to the page that allows you to create a new contact.
    
2.  The closing element of the `content` block.

And that’s our complete template. Using this simple server-side template, in combination with our handler method, we can respond with an HTML _representation_ of all the contacts requested. So far, so hypermedia.

Here is what the template looks like, rendered with a bit of contact information:

![](file1.png)

Contact.app

Now, our application won’t win any design awards at this point, but notice that our template, when rendered, provides all the functionality necessary to see all the contacts and search them, and also provides links to edit them, view details of them or even create a new one.

And it does all this without the client (that is, the browser) knowing a thing about what contacts are or how to work with them. Everything is encoded _in_ the hypermedia. A web browser accessing this application just knows how to issue HTTP requests and then render HTML, nothing more about the specifics of our applications end points or underlying domain model.

As simple as our application is at this point, it is thoroughly RESTful.