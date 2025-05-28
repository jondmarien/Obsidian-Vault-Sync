# Swipe Gesture on Contacts

To add communication capabilities and the message UI, we extended the client with custom behavior actions. But the Hyperview client can also be extended with custom UI components that render on the screen. Custom components are implemented as React Native components. That means anything that’s possible in React Native can be done in Hyperview as well! Custom components open up endless possibilities to build rich mobile apps with the Hypermedia architecture.

To illustrate the possibilities, we will extend the Hyperview client in our mobile app to add a “swipeable row” component. How does it work? The “swipeable row” component supports a horizontal swiping gesture. As the user swipes this component from right to left, the component will slide over, revealing a series of action buttons. Each action button will be able to trigger standard Hyperview behaviors when pressed. We will use this custom component in our Contacts List screen. Each contact item will be a “swipeable row”, and the actions will give quick access to edit and delete actions for the contact.

![](file17.png)

Swipeable contact item

## Designing The Component

Rather than implementing the swipe gesture from scratch, we will once again use an open-source third-party library: `react-native-swipeable`.

    cd hyperview/demo
    yarn add react-native-swipeable <1>
    yarn start <2>

\]

1.  Add dependency on `react-native-swipeable`.
    
2.  Re-start the mobile app.

This library provides a React Native component called `Swipeable`. It can render any React Native components as its main content (the part that can be swiped). It also takes an array of React Native components as a prop to render as the action buttons.

When designing a custom component, we like to define the HXML of the component before writing the code. This way, we can make sure the markup is expressive but succinct, and will work with the underlying library.

For the swipeable row, we need a way to represent the entire component, the main content, and one of many buttons.

    <swipe:row
      xmlns:swipe="https://hypermedia.systems/hyperview/swipeable"> <1>
      <swipe:main> <2>
        
      swipe:main>
    
      <swipe:button> <3>
        
      swipe:button>
    
      <swipe:button> <4>
        
      swipe:button>
    swipe:row>

\]

1.  Parent element encapsulating the entire swipeable row, with custom namespace.
    
2.  The main content of the swipeable row, can hold any HXML.
    
3.  The first button that appears when swiping, can hold any HXML.
    
4.  The second button that appears when swiping, can hold any HXML.

This structure clearly separates the main content from the buttons. It also supports one, two, or more buttons. Buttons appear in the order of definition, making it easy to swap the order.

This design covers everything we need to implement a swipeable row for our contacts list. But it’s also generic enough to be reusable. The previous markup contains nothing specific to the contact name, editing the contact, or deleting the contact. If later we add another list screen to our app, we can use this component to make the items in that list swipeable.

## Implementing The Component

Now that we know the HXML structure of our custom component, we can write the code to implement it. What does that code look like? Hyperview components are written as React Native components. These React Native components are mapped to a unique XML namespace and tag name. When the Hyperview client encounters that namespace and tag name in the HXML, it delegates rendering of the HXML element to the matching React Native component. As part of delegation, the Hyperview Client passes several props to the React Native component:

*   `element`: The XML DOM element that maps to the React Native component.
    
*   `stylesheets`: The styles defined in the .
    
*   `onUpdate`: The function to call when the component triggers a behavior.
    
*   `option`: Miscellaneous settings used by the Hyperview client.

Our swipeable row component is a container with slots to render arbitrary main content and buttons. That means it needs to delegate back to the Hyperview client to render those parts of the UI. This is done with a public function exposed by the Hyperview client, `Hyperview.renderChildren()`.

Now that we know how custom Hyperview components are implemented, let’s write the code for our swipeable row.

    import React, { PureComponent } from 'react';
    import Hyperview from 'hyperview';
    import Swipeable from 'react-native-swipeable';
    
    const NAMESPACE_URI = 'https://hypermedia.systems/hyperview/swipeable';
    
    export default class SwipeableRow extends PureComponent { <1>
      static namespaceURI = NAMESPACE_URI; <2>
      static localName = "row"; <3>
    
      getElements = (tagName) => {
        return Array.from(this.props.element
          .getElementsByTagNameNS(NAMESPACE_URI, tagName));
      };
    
      getButtons = () => { <4>
        return this.getElements("button").map((buttonElement) => {
          return Hyperview.renderChildren(buttonElement,
            this.props.stylesheets,
            this.props.onUpdate,
            this.props.options); <5>
        });
      };
    
      render() {
        const [main] = this.getElements("main");
        if (!main) {
          return null;
        }
    
        return (
          <Swipeable rightButtons={this.getButtons()}> <6>
            {Hyperview.renderChildren(main,
              this.props.stylesheets,
              this.props.onUpdate,
              this.props.options)} <7>
          Swipeable>
        );
      }
    }

demo/src/swipeable.js

1.  Class-based React Native component.
    
2.  Map this component to the given HXML namespace.
    
3.  Map this component to the given HXML tag name.
    
4.  Function that returns an array of React Native components for each element.
    
5.  Delegate to the Hyperview client to render each button.
    
6.  Pass the buttons and main content to the third-party library.
    
7.  Delegate to the Hyperview client to render the main content.

The `SwipeableRow` class implements a React Native component. At the top of the class, we set a static `namespaceURI` property and `localName` property. These properties map the React Native component to a unique namespace and tag name pair in the HXML. This is how the Hyperview client knows to delegate to `SwipeableRow` when encountering custom elements in the HXML. At the bottom of the class, you’ll see a `render()` method. `render()` gets called by React Native to return the rendered component. Since React Native is built on the principle of composition, `render()` typically returns a composition of other React Native components. In this case, we return the `Swipeable` component (provided by the `react-native-swipeable` library), composed with React Native components for the buttons and main content. The React Native components for the buttons and main content are created using a similar process:

*   Find the specific child elements ( or
    
    ).- Turn those elements into React Native components using `Hyperview.renderChildren()`.- Set the components as children or props of `Swipeable`.

        HyperView Client               SwipeableRow
    ┌──────────────────────┐     ┌──────────────────────┐
    │───────────┼─────▶           │
    │                      │     │          │
    │    Hello◀─────┼────Hello│
    │                      │     │         │
    │                      │     │        │
    │    Edit◀┼─────┼────Edit │
    │                      │     │       │
    │          │     │          │
    └──────────────────────┘     └──────────────────────┘

Rendering delegation between the client and the custom components

This code may be hard to follow if you’ve never worked with React or React Native. That’s OK. The important takeaway is: we can write code to translate arbitrary HXML into React Native components. The structure of the HXML (both attributes and elements) can be used to represent multiple facets of the UI (in this case, the buttons and main content). Finally, the code can delegate rendering of child components back to the Hyperview client.

The result: this swipeable row component is completely generic. The actual structure and styling and interactions of the main content and buttons can be defined in the HXML. Creating a generic component means we can reuse it across multiple screens for different purposes. If we add more custom components or new behavior actions in the future, they will work with our swipeable row implementation.

The last thing to do is register this new component with the Hyperview client. The process is similar to registering custom actions. Custom components are passed as a separate `components` prop to the `Hyperview` component.

    import React, { PureComponent } from 'react';
    import Hyperview from 'hyperview';
    import OpenEmail from './email';
    import OpenPhone from './phone';
    import ShowMessage from './message';
    import SwipeableRow from './swipeable'; <1>
    
    export default class HyperviewScreen extends PureComponent {
      // ... omitted for brevity
    
      behaviors = [OpenEmail, OpenPhone, ShowMessage];
      components = [SwipeableRow]; <2>
    
      render() {
        return (
          <Hyperview
            behaviors={this.behaviors}
            components={this.components} <3>
            entrypointUrl={this.entrypointUrl}
            // more props...
          />
        );
      }
    }

demo/src/HyperviewScreen.js

1.  Import the `SwipeableRow` component.
    
2.  Create an array of custom components.
    
3.  Pass the custom component to the `Hyperview` component, as a prop called `components`.

We’re now ready to update our HXML templates to make use of the new swipeable row component.

### Using the component

Currently, the HXML for a contact item in the list consists of a and element:

    <item key="{{ contact.id }}" style="contact-item">
      <behavior trigger="press" action="push"
        href="/contacts/{{ contact.id }}" />
      <text style="contact-item-label">
        
      text>
    item>

Snippet of `hv/rows.xml`

With our swipeable row component, this markup will become the “main” UI. So let’s start by adding and

as ancestor elements.

    <item key="{{ contact.id }}">
      <swipe:row <1>
        xmlns:swipe="https://hypermedia.systems/hyperview/swipeable">
        <swipe:main> <2>
          <view style="contact-item"> <3>
            <behavior trigger="press" action="push"
              href="/contacts/{{ contact.id }}" />
            <text style="contact-item-label">
              
            text>
          view>
        swipe:main>
      swipe:row>
    item>

Adding swipeable row `hv/rows.xml`

1.  Added ancestor element, with namespace alias for `swipe`.
    
2.  Added element to define the main content.
    
3.  Wrapped the existing and elements in a .

Previously, the `contact-item` style was set on the element. That made sense when the element was the container for the main content of the list item. Now that the main content is a child of , we need to introduce a new where we apply the styles.

If we reload our backend and mobile app, you won’t experience any changes on the Contacts List screen yet. Without any action buttons defined, there’s nothing to reveal when swiping a row. Let’s add two buttons to the swipeable row.

    <item key="{{ contact.id }}">
      <swipe:row
        xmlns:swipe="https://hypermedia.systems/hyperview/swipeable">
        <swipe:main>
          
        swipe:main>
    
        <swipe:button> <1>
          <view style="swipe-button">
            <text style="button-label">Edittext>
          view>
        swipe:button>
    
        <swipe:button> <2>
          <view style="swipe-button">
            <text style="button-label-delete">Deletetext>
          view>
        swipe:button>
      swipe:row>
    item>

Adding swipeable row `hv/rows.xml`

1.  Added for edit action.
    
2.  Added for delete action.

Now if we use our mobile app, we can see the swipeable row in action! As you swipe the contact item, the “Edit” and “Delete” buttons reveal themselves. But they don’t do anything yet. We need to add some behaviors to these buttons. The “Edit” button is straight-forward: pressing it should open the contact details screen in edit mode.

    <swipe:button>
      <view style="swipe-button">
        <behavior trigger="press" action="push"
          href="/contacts/{{ contact.id }}/edit" /> <1>
        <text style="button-label">Edittext>
      view>
    swipe:button>

Snippet of `hv/rows.xml`

1.  When pressed, push a new screen with the Edit Contact UI.

The “Delete” button is a bit more complicated. There’s no screen to open for deletion, so what should happen when the user presses this button? Perhaps we use the same interaction as the “Delete” button on the Edit Contact screen. That interaction brings up a system dialog, asking the user to confirm the deletion. If the user confirms, the Hyperview client makes a `POST` request to `/contacts//delete`, and appends the response to the screen. The response triggers a few behaviors immediately to reload the contacts list and show a message. This interaction will work for our action button as well:

    <swipe:button>
      <view style="swipe-button">
        <behavior <1>
          xmlns:alert="https://hyperview.org/hyperview-alert"
          trigger="press"
          action="alert"
          alert:title="Confirm delete"
          alert:message="Are you sure you want to delete
            {{ contact.first }}?"
        >
          <alert:option alert:label="Confirm">
            <behavior <2>
              trigger="press"
              action="append"
              target="item-{{ contact.id }}"
              href="/contacts/{{ contact.id }}/delete"
              verb="post"
            />
          alert:option>
          <alert:option alert:label="Cancel" />
        behavior>
        <text style="button-label-delete">Deletetext>
      view>
    swipe:button>

Snippet of `hv/rows.xml`

1.  When pressed, open a system dialog box asking the user to confirm the action.
    
2.  If confirmed, make a POST request to the deletion endpoint, and append the response to the enclosing .

Now when we press “Delete,” we get the confirmation dialog as expected. After pressing confirm, the backend response triggers behaviors that show a confirmation message and reload the list of contacts. The item for the deleted contact disappears from the list.

![](file18.png)

Delete from swipe button

Notice that the action buttons are able to support any type of behavior action, from `push` to `alert`. If we wanted to, we could have the action buttons trigger our custom actions, like `open-phone` and `open-email`. Custom components and actions can be mixed freely with the standard components and actions that come standard with the Hyperview framework. This makes the extensions to the Hyperview client feel like first-class features.

In fact, we’ll let you in on a secret. Within the Hyperview client, standard components and actions are implemented the same way as custom components and actions! The rendering code does not treat differently from . The behavior code does not treat `alert` differently from `open-phone`. They are both implemented using the same techniques described in this section. Standard components and actions are just the ones that are universally needed by all mobile apps. But they are just the starting point.

Most mobile apps will require some extensions to the Hyperview client to deliver a great user experience. Extensions evolve the client from being a generic “Hyperview client,” to being a purpose-built client for your app. And importantly, this evolution preserves the Hypermedia, server-driven architecture and all of its benefits.