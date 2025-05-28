# Using Off-the-Shelf Components

That concludes our look at three different options for _your_ scripting infrastructure, that is, the code that _you_ write to enhance your Hypermedia-Driven Application. However, there is another major area to consider when discussing client side scripting: “off the shelf” components. That is, JavaScript libraries that other people have created that offer some sort of functionality, such as showing modal dialogs.

Components have become very popular in the web development world, with libraries like [DataTables](https://datatables.net/) providing rich user experiences with very little JavaScript code on the part of a user. Unfortunately, if these libraries aren’t integrated well into a website, they can begin to make an application feel “patched together.” Furthermore, some libraries go beyond simple DOM manipulation, and require that you integrate with a server endpoint, almost invariably with a JSON data API. This means you are no longer building a Hypermedia-Driven Application, simply because a particular widget demands something different. A shame!

**Web Components**

Web Components is the collective name of a few standards; Custom Elements and Shadow DOM, and