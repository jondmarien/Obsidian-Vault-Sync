# Adding Phone Calls and Email

Let’s start with the most obvious feature missing from our Contacts app: phone calls. Mobile devices can make phone calls. The contacts in our app have phone numbers. Shouldn’t our app support calling those phone numbers? And while we’re at it, our app should also support e-mailing the contacts.

On the web, calling phone numbers is supported with the `tel:` URI scheme, and e-mails are supported with the `mailto:` URI scheme:

    <a href="tel:555-555-5555">Calla> <1>
    <a href="mailto:joe@example.com">Emaila> <2>

`tel` and `mailto` schemes in HTML

1.  When clicked, prompt the user to call the given phone number
    
2.  When clicked, open an e-mail client with the given address populated in the `to:` field.

The Hyperview client doesn’t support the `tel:` and `mailto:` URI schemes. But we can add these capabilities to the client with custom behavior actions. Remember that behaviors are interactions defined in HXML. Behaviors have triggers (“press”, “refresh”) and actions (“update”, “share”). The values of “action” are not limited to the set that comes in the Hyperview library. So let’s define two new actions, “open-phone” and “open-email”.

    <view
      xmlns:comms="https://hypermedia.systems/hyperview/communications"> <1>
      <text>
        <behavior action="open-phone"
          comms:phone-number="555-555-5555" /> <2>
        Call
      text>
      <text>
        <behavior action="open-email"
          comms:email-address="joe@example.com" /> <3>
        Email
      text>
    view>

Phone and Email actions

1.  Define an alias for an XML namespace used by our new attributes.
    
2.  When pressed, prompt the user to call the given phone number.
    
3.  When pressed, open an e-mail client with the given address populated in the `to:` field.

Notice we defined the actual phone number and email address using separate attributes. In HTML, the scheme and data are crammed into the `href` attribute. HXML’s elements give more options for representing the data. We chose to use attributes, but we could have represented the phone number or email using child elements. We’re also using a namespace to avoid potential future conflicts with other client extensions.

So far so good, but how does the Hyperview client know how to interpret `open-phone` and `open-email`, and how to reference the `phone-number` and `email-address` attributes? This is where we finally need to write some JavaScript.

First, we’re going to add a 3rd-party library (`react-native-communications`) to our demo app. This library provides a simple API that interacts with OS-level functionality for calls and emails.

    cd hyperview/demo
    yarn add react-native-communications <1>
    yarn start <2>

1.  Add dependency on `react-native-communications`
    
2.  Re-start the mobile app

Next, we’ll create a new file, `phone.js`, that will implement the code associated with the `open-phone` action:

    import { phonecall } from 'react-native-communications'; <1>
    
    const namespace = "https://hypermedia.systems/hyperview/communications";
    
    export default {
      action: "open-phone", <2>
      callback: (behaviorElement) => { <3>
        const number = behaviorElement
          .getAttributeNS(namespace, "phone-number"); <4>
        if (number != null) {
          phonecall(number, false); <5>
        }
      },
    };

demo/src/phone.js

1.  Import the function we need from the 3rd party library.
    
2.  The name of the action.
    
3.  The callback that runs when the action triggers.
    
4.  Get the phone number from the element.
    
5.  Pass the phone number to the function from the 3rd party library.

Custom actions are defined as a JavaScript object with two keys: `action` and `callback`. This is how the Hyperview client associates a custom action in the HXML with our custom code. The callback value is a function that takes a single parameter, `behaviorElement`. This parameter is an XML DOM representation of the element that triggered the action. That means we can call methods on it like `getAttribute`, or access attributes like `childNodes`. In this case, we use `getAttributeNS` to read the phone number from the `phone-number` attribute on the element. If the phone number is defined on the element, we can call the `phonecall()` function provided by the `react-native-communications` library.

There’s one more thing to do before we can use our custom action: register the action with the Hyperview client. The Hyperview client is represented as a React Native component called `Hyperview`. This component takes a prop called `behaviors`, which is an array of custom action objects like our “open-phone” action. Let’s pass our “open-phone” implementation to the `Hyperview` component in our demo app.

    import React, { PureComponent } from 'react';
    import Hyperview from 'hyperview';
    import OpenPhone from './phone'; <1>
    
    export default class HyperviewScreen extends PureComponent {
      // ... omitted for brevity
    
      behaviors = [OpenPhone]; <2>
    
      render() {
        return (
          <Hyperview
            behaviors={this.behaviors} <3>
            entrypointUrl={this.entrypointUrl}
            // more props...
          />
        );
      }
    }

demo/src/HyperviewScreen.js

1.  Import the open-phone action.
    
2.  Create an array of custom actions.
    
3.  Pass the custom actions to the `Hyperview` component, as a prop called `behaviors`.

Under the hood, the `Hyperview` component is responsible for taking HXML and turning it into mobile UI elements. It also handles triggering behavior actions based on user interactions.

By passing the “open-phone” action to Hyperview, we can now use it as a value for the `action` attribute on elements. In fact, let’s do that now by updating the `show.xml` template in our Flask app:

    {% block content %}
    <view style="details">
      <text style="contact-name">
        {{ contact.first }} {{ contact.last }}
      text>
    
      <view style="contact-section">
        <behavior <1>
          xmlns:comms="https://hypermedia.systems/hyperview/communications"
          trigger="press"
          action="open-phone" <2>
          comms:phone-number="{{contact.phone}}" <3>
        />
        <text style="contact-section-label">Phonetext>
        <text style="contact-section-info">{{contact.phone}}text>
      view>
    
      <view style="contact-section">
        <behavior <4>
          xmlns:comms="https://hypermedia.systems/hyperview/communications"
          trigger="press"
          action="open-email"
          comms:email-address="{{contact.email}}"
        />
        <text style="contact-section-label">Emailtext>
        <text style="contact-section-info">{{contact.email}}text>
      view>
    view>
    {% endblock %}

Snippet of `hv/show.xml`

1.  Add a behavior to the phone number section that triggers on “press.”
    
2.  Trigger the new “open-phone” action.
    
3.  Set the attribute expected by the “open-phone” action.
    
4.  Same idea, with a different action (“open-email”).

We’ll skip over the implementation of the second custom action, “open-email.” As you can guess, this action will open a system-level email composer to let the user send an email to their contact. The implementation of “open-email” is almost identical to “open-phone.” The `react-native-communications` library exposes a function called `email()`, so we just wrap it and pass arguments to it in the same way.

We now have a complete example of extending the client with custom behavior actions. We chose a new name for our actions (“open-phone” and “open-email“), and mapped those names to functions. The functions take elements and can run any arbitrary React Native code. We wrapped an existing 3rd party library, and read attributes set on the element to pass data to the library. After re-starting our demo app, our client has new capabilities we can immediately utilize by referencing the actions from our HXML templates.