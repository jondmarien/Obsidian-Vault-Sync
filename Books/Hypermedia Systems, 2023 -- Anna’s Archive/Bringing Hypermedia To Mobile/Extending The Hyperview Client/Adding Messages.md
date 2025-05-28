# Adding Messages

The phone and email actions added in the previous section are examples of “system actions.” System actions trigger some UI or capability provided by the device’s OS. But custom actions are not limited to interacting with OS-level APIs. Remember, the callbacks that implement actions can run arbitrary code, including code that renders our own UI elements. This next custom action example will do just that: render a custom confirmation message UI element.

If you recall, our Contacts web app shows messages upon successful actions, such as deleting or creating a contact. These messages are generated in the Flask backend using the `flash()` function, called from the views. Then the base `layout.html` template renders the messages into the final web page.

    {% for message in get_flashed_messages() %}
      {{ message }}
    {% endfor %}
    

Snippet templates/layout.html

Our Flask app still includes the calls to `flash()`, but the Hyperview app is not accessing the flashed message to display to the user. Let’s add that support now.

We could just show the messages using a similar technique to the web app: loop through the messages and render some elements in `layout.xml`. This approach has a major downside: the rendered messages would be tied to a specific screen. If that screen was hidden by a navigation action, the message would be hidden too. What we really want is for our message UI to display “above” all of the screens in the navigation stack. That way, the message would remain visible (fading away after a few seconds), even if the stack of screens changes below. To display some UI outside of the elements, we’re going to need to extend the Hyperview client with a new custom action, `show-message`. This is another opportunity to use an open-source library, `react-native-root-toast`. Let’s add this library to our demo app.

    cd hyperview/demo
    yarn add react-native-root-toast <1>
    yarn start <2>

\]

1.  Add dependency on `react-native-root-toast`
    
2.  Re-start the mobile app

Now, we can write the code to implement the message UI as a custom action.

    import Toast from 'react-native-root-toast'; <1>
    
    const namespace = "https://hypermedia.systems/hyperview/message";
    
    export default {
      action: "show-message", <2>
      callback: (behaviorElement) => { <3>
        const text = behaviorElement.getAttributeNS(namespace, "text");
        if (text != null) {
          Toast.show(text, { <4>
            position: Toast.positions.TOP, duration: 2000
          });
        }
      },
    };

demo/src/message.js

1.  Import the `Toast` API.
    
2.  The name of the action.
    
3.  The callback that runs when the action triggers.
    
4.  Pass the message to the toast library.

This code looks very similar to the implementation of `open-phone`. Both callbacks follow a similar pattern: read namespaced attributes from the element, and pass those values to a 3rd party library. For simplicity, we’re hard-coding options to show the message at the top of the screen, fading out after 2 seconds. But `react-native-root-toast` exposes many options for positioning, timing of animations, colors, and more. We could specify these options using extra attributes on `behaviorElement` to make the action more configurable. For our purposes, we will just stick to a bare-bones implementation.

Now we need to register our custom action with the component, by passing it to the `behaviors` prop.

    import React, { PureComponent } from 'react';
    import Hyperview from 'hyperview';
    import OpenEmail from './email';
    import OpenPhone from './phone';
    import ShowMessage from './message'; <1>
    
    export default class HyperviewScreen extends PureComponent {
      // ... omitted for brevity
    
      behaviors = [OpenEmail, OpenPhone, ShowMessage]; <2>
    
      // ... omitted for brevity
    }

demo/src/HyperviewScreen.js

1.  Import the `show-message` action.
    
2.  Pass the action to the `Hyperview` component, as a prop called `behaviors`.

All that’s left to do is trigger the `show-message` action from our HXML. There are three user actions that result in showing a message:

1.  Creating a new contact
    
2.  Updating an existing contact
    
3.  Deleting a contact

The first two actions are implemented in our app using the same HXML template, `form_fields.xml`. Upon successfully creating or updating a contact, this template will reload the screen and trigger an event, using behaviors that trigger on “load”. The deletion action also uses behaviors that trigger on “load”, defined in the `deleted.xml` template. So both `form_fields.xml` and `deleted.xml` need to be modified to also show messages on load. Since the actual behaviors will be the same in both templates, let’s create a shared template to reuse the HXML.

    {% for message in get_flashed_messages() %}
      <behavior <1>
        xmlns:message="https://hypermedia.systems/hyperview/message"
        trigger="load" <2>
        action="show-message" <3>
        message:text="{{ message }}" <4>
      />
    {% endfor %}

hv/templates/messages.xml

1.  Define a behavior for each message to display.
    
2.  Trigger this behavior as soon as the element loads.
    
3.  Trigger the new “show-message” action.
    
4.  The “show-message” action will display the flashed message in its UI.

Like in `layout.html` of the web app, we loop through all of the flashed messages and render some markup for each message. However, in the web app, the message was directly rendered into the web page. In the Hyperview app, each message is displayed using a behavior that triggers our custom UI. Now we just need to include this template in `form_fields.xml`:

    <view xmlns="https://hyperview.org/hyperview" style="edit-group">
      {% if saved %}
        {% include "hv/messages.xml" %} <1>
        <behavior trigger="load" once="true" action="dispatch-event"
          event-name="contact-updated" />
        <behavior trigger="load" once="true" action="reload"
          href="/contacts/{{contact.id}}" />
      {% endif %}
      
    view>

Snippet of hv/templates/form\_fields.xml

1.  Show the messages as soon as the screen loads.

And we can do the same thing in `deleted.xml`:

    <view xmlns="https://hyperview.org/hyperview">
      {% include "hv/messages.xml" %} <1>
      <behavior trigger="load" action="dispatch-event"
        event-name="contact-updated" />
      <behavior trigger="load" action="back" />
    view>

hv/templates/deleted.xml

1.  Show the messages as soon as the screen loads.

In both `form_fields.xml` and `deleted.xml`, multiple behaviors get triggered on “load.” In `deleted.xml`, we immediately navigate back to the previous screen. In `form_fields.xml`, we immediately reload the current screen to show the Contact details. If we rendered our message UI elements directly in the screen, the user would barely see them before the screen disappeared or reloaded. By using a custom action, the message UI remains visible even while the screens change beneath them.

![](file16.png)

Message shown during back navigation