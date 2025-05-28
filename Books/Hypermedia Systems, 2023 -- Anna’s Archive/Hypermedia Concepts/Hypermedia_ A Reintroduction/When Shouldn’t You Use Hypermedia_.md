# When Shouldn’t You Use Hypermedia?

So, what about that _not always_? When isn’t hypermedia going to work well for an application?

One example that springs immediately to mind is an online spreadsheet application. In the case of a spreadsheet, updating one cell could have a large number of cascading changes that need to be made across the entire sheet. Worse, this might need to happen _on every keystroke_.

In this case we have a highly dynamic user interface without clear boundaries as to what might need to be updated given a particular change. Introducing a hypermedia-style server round-trip on every cell change would hurt performance tremendously.

This is simply not a situation amenable to the “large-grain hypermedia data transfer” approach of the web. For an application like this we would certainly recommend looking into using a sophisticated client-side JavaScript approach.

_However_ even in the case of an online spreadsheet there are likely areas where the hypermedia approach might help.

The spreadsheet application likely also has a settings page. And perhaps that settings page _is_ amenable to the hypermedia approach. If it is simply a set of relatively straight-forward forms that need to be persisted to the server, the chances are good that hypermedia would, in fact, work great for this part of the app.

And, by adopting hypermedia for that part of your application, you might be able to simplify that part of the application quite a bit. You could then save more of your application’s _complexity budget_ for the core, complicated spreadsheet logic, keeping the simple stuff simple.

Why waste all the complexity associated with a heavy JavaScript framework on something as simple as a settings page?

**A Complexity Budget**

Any software project has a complexity budget, explicit or not: there is only so much complexity a given development team can tolerate and every new feature and implementation choice adds at least a bit more to the overall complexity of the system.

What is particularly nasty about complexity is that it tends to grow exponentially: one day you can keep the entire system in your head and understand the ramifications of a particular change, and a week later the whole system seems intractable. Even worse, efforts to help control complexity, such as introducing abstractions or infrastructure to manage the complexity, often end up making things even more complex. Truly, the job of the good software engineer is to keep complexity under control.

The sure-fire way to keep complexity down is also the hardest: say no. Pushing back on feature requests is an art and, if you can learn to do it well, making people feel like _they_ said no, you will go far.

Sadly this is not always possible: some features will need to be built. At this point the question becomes: “what is the simplest thing that could possibly work?” Understanding the possibilities available in the hypermedia approach will give you another tool in your “simplest thing” tool chest.