# Hypermedia for Mobile Apps

We’ve seen that the hypermedia architecture can address the shortcomings of SPAs on the web. But can hypermedia work for mobile apps as well? The answer is yes!

Just like on the web, we can use hypermedia formats on mobile and let it serve as the engine of application state. All of the logic is controlled from the backend, rather than being spread between two codebases. Hypermedia architecture also solves the annoying problem of API churn on mobile apps. Since the backend serves a hypermedia response containing both data and actions, there’s no way for the data and UI to get out of sync. No more worries about backwards compatibility or maintaining multiple API versions.

So how can you use hypermedia for your mobile app? There are two approaches employing hypermedia to build & ship native mobile apps today:

*   Web views, which wraps the trusty web platform in a mobile app shell
    
*   Hyperview, a new hypermedia system we designed specifically for mobile apps
    

## Web Views

The simplest way to use hypermedia architecture on mobile is by leveraging web technologies. Both Android and iOS SDKs provide “web views”: chromeless web browsers that can be embedded in native apps. Tools like Apache Cordova make it easy to take the URL of a website, and spit out native iOS and Android apps based on web views. If you already have a responsive web app, you can get a “native” mobile HDA for free. Sounds too good to be true, right?

Of course, there is a fundamental limitation with this approach. The web platform and mobile platforms have different capabilities and UX conventions. HTML doesn’t natively support common UI patterns of mobile apps. One of the biggest differences is around how each platform handles navigation. On the web, navigation is page-based, with one page replacing another and the browser providing back/forward buttons to navigate the page history. On mobile, navigation is more complex, and tuned for the physicality of gesture-based interactions.

*   To drill down, screens slide on top of each other, forming stacks of screens.
    
*   Tab bars at the top or bottom of the app allow switching between various stacks of screens.
    
*   Modals slide up from the bottom of the app, covering the other stacks and tab bar.
    
*   Unlike with web pages, all of these screens are still present in memory, rendered and updating based on app state.
    

The navigation architecture is a major difference between how mobile and web apps function. But it’s not the only one. Many other UX patterns are present in mobile apps, but are not natively supported on the web:

*   pull-to-refresh to refresh content in a screen
    
*   horizontal swipe on UI elements to reveal actions
    
*   sectioned lists with sticky headers
    

While these interactions are not natively supported by web browsers, they can be simulated with JS libraries. Of course, these libraries will never have the same feel and performance as native gestures. And using them usually requires embracing a JS-heavy SPA architecture like React. This puts us back at square 1! To avoid using the typical thick-client architecture of native mobile apps, we turned to a web view. The web view allows us to use good-old hypermedia-based HTML. But to get the desired look & feel of a mobile app, we end up building a SPA in JS, losing the benefits of Hypermedia in the process.

To build a mobile HDA that acts and feels like a native app, HTML isn’t going to cut it. We need a format designed to represent the interactions and patterns of native mobile apps. That’s exactly what Hyperview does.

## Hyperview

Hyperview is an open-source hypermedia system that provides:

*   A hypermedia format for defining mobile apps called HXML
    
*   A hypermedia client for HXML that works on iOS and Android
    
*   Extension points in HXML and the client to customize the framework for a given app
    

### The format

HXML was designed to feel familiar to web developers, used to working with HTML. Thus the choice of XML for the base format. In addition to familiar ergonomics, XML is compatible with server-side rendering libraries. For example, Jinja2 is perfectly suited as a templating library to render HXML. The familiarity of XML and the ease of integration on the backend make it simple to adopt in both new and existing codebases. Take a look at a “Hello World” app written in HXML. The syntax should be familiar to anyone who’s worked with HTML:

    <doc xmlns="https://hyperview.org/hyperview">
      <screen>
        <styles />
        <body>
          <header>
            <text>My first apptext>
          header>
          <view>
            <text>Hello World!text>
          view>
        body>
      screen>
    doc>

Hello World

But HXML is not just a straight port of HTML with differently named tags. In previous chapters, we’ve seen how htmx enhances HTML with a handful of new attributes. These additions maintain the declarative nature of HTML, while giving developers the power to create rich web apps. In HXML, the concepts of htmx are built into the spec. Specifically, HXML is not limited to “click a link” and “submit a form” interactions like basic HTML. It supports a range of triggers and actions for modifying the content on a screen. These interactions are bundled together in a powerful concept of “behaviors.” Developers can even define new behavior actions to add new capabilities to their app, without the need for scripting. We will learn more about behaviors later in this chapter.

### The client

Hyperview provides an open-source HXML client library written in React Native. With a little bit of configuration and a few steps on the command line, this library compiles into native app binaries for iOS or Android. Users install the app on their device via an app store. On launch, the app makes an HTTP request to the configured URL, and renders the HXML response as the first screen.

It may seem a little strange that developing a HDA using Hyperview requires a single-purpose client binary. After all, we don’t ask users to first download and install a binary to view a web app. No, users just enter a URL in the address bar of a general-purpose web browser. A single HTML client renders apps from any HTML server.

                      ┌────────────┐
                      │            │
    ┌──────────┬─┐    │   SERVER   │
    ├──────────┴─┤    │            │
    │            │    └──▲─────────┘
    │            │       │
    │            │       │  
    │            ├───────┘  ┌────────────┐
    │            │          │            │
    │   CLIENT   ├──────────▶   SERVER   │
    │            │          │            │
    │            ├─────┐    └────────────┘
    │            │     │
    │            │   ┌────────────┐
    │            │   │            │
    └────────────┘   │   SERVER   │
                     │            │
                     └────────────┘
    

One HTML client, multiple HTML servers

It is theoretically possible to build an equivalent general-purpose “Hyperview browser.” This HXML client would render apps from any HXML server, and users would enter a URL to specify the app they want to use. But iOS and Android are built around the concept of single-purpose apps. Users expect to find and install apps from an app store, and launch them from the home screen of their device. Hyperview embraces this app-centric paradigm of today’s popular mobile platforms. That means that the HXML client (app binary) renders its UI from a single pre-configured HXML server:

    ┌────────────┐
    │            │       ┌────────────┐
    │            │       │┌──────────┐│
    │   SERVER   │       ││          ││
    │            │       ││┌───┐┌───┐││
    │            ◀─────────┤   ││   │││
    │            │       ││└───┘└───┘││
    │            │       ││ App  App ││
    │            │       ││          ││
    │            │       ││┌───┐┌───┐││
    │            │       │└┴───┴┴───┴┘│
    │            │       │   CLIENT   │
    │            │       └────────────┘
    └────────────┘
    

One HXML client, one HXML server

Luckily, developers do not need to write a HXML client from scratch; the open-source client library does 99% of the work. And as we will see in the next section, there are major benefits to controlling both the client and server in a HDA.

### Extensibility

To understand the benefits of Hyperview’s architecture, we need to first discuss the drawbacks of the web architecture. On the web, any web browser can render HTML from any web server. This level of compatibility can only happen with well-defined standards such as HTML5. But defining and evolving standards is a laborious process. For example, the W3C took over 7 years to go from first draft to recommendation on the HTML5 spec. It’s not surprising, given the level of thoughtfulness that needs to go into a change that impacts so many people. But it means that progress happens slowly. As a web developer, you may need to wait years for browsers to gain widespread support for the feature you need.

So what are the benefits of Hyperview’s architecture? In a Hyperview app, _your_ mobile app only renders HXML from _your_ server. You don’t need to worry about compatibility between your server and other mobile apps, or between your mobile app and other servers. There is no standards body to consult. If you want to add a blink feature to your mobile app, go ahead and implement a element in the client, and start returning elements in the HXML responses from your server. In fact, the Hyperview client library was built with this type of extensibility in mind. There are extension points for custom UI elements and custom behavior actions. We expect and encourage developers to use these extensions to make HXML more expressive and customized to their app’s functionality.

And by extending the HXML format and client itself, there’s no need for Hyperview to include a scripting layer in HXML. Features that require client-side logic get “built-in” to the client binary. HXML responses remain pure, with UI and interactions represented in declarative XML.

## Which Hypermedia Architecture Should You Use?

We’ve discussed two approaches for creating mobile apps using hypermedia systems:

*   create a backend that returns HTML, and serve it in a mobile app through a web view
    
*   create a backend that returns HXML, and serve it in a mobile app with the Hyperview client
    

I purposefully described the two approaches in a way to highlight their similarities. After all, they are both based on hypermedia systems, just with different formats and clients. Both approaches solve the fundamental issues with traditional, SPA-like mobile app development:

*   The backend controls the full state of the app.
    
*   Our app’s logic is all in one place.
    
*   The app always runs the latest version, there’s no API churn to worry about.
    

So which approach should you use for a mobile HDA? Based on our experience building both types of apps, we believe the Hyperview approach results in a better user experience. The web-view will always feel out-of-place on iOS and Android; there’s just no good way to replicate the patterns of navigation and interaction that mobile users expect. Hyperview was created specifically to address the limitations of thick-client and web view approaches. After the initial investment to learn Hyperview, you’ll get all of the benefits of the Hypermedia architecture, without the downsides of a degraded user experience.

Of course, if you already have a simple, mobile-friendly web app, then using a web-view approach is sensible. You will certainly save time from not having to serve your app as HXML in addition to HTML. But as we will show at the end of this chapter, it doesn’t take a lot of work to convert an existing Hypermedia-driven web app into a Hyperview mobile app. But before we get there, we need to introduce the concepts of elements and behaviors in Hyperview. Then, we’ll re-build our contacts app in Hyperview.

**When Shouldn’t You Use Hypermedia to Build a Mobile App?**

Hypermedia is not always the right choice to build a mobile app. Just like on the web, apps that require highly dynamic UIs (such as a spreadsheet application) are better implemented with client-side code. Additionally, some apps need to function while fully offline. Since HDAs require a server to render UI, offline-first mobile apps are not a good fit for this architecture. However, just like on the web, developers can use a hybrid approach to build their mobile app. The highly dynamic screens can be built with complex client-side logic, while the less dynamic screens can be built with web views or Hyperview. In this way, developers can spend their _complexity budget_ on the core of the application, and keep the simple screens simple.