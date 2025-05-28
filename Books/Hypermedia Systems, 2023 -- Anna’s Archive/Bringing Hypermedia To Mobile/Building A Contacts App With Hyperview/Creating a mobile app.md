# Creating a mobile app

To get started with HXML, there’s one pesky requirement: the Hyperview client. When developing web applications, you only need to worry about the server because the client (web browser) is universally available. There’s no equivalent Hyperview client installed on every mobile device. Instead, we will create our own Hyperview client, customized to only talk to our server. This client can be packaged up into an Android or iOS mobile app, and distributed through the respective app stores.

Luckily, we don’t need to start from scratch to implement a Hyperview client. The Hyperview code repository comes with a demo backend and a demo client built using Expo. We will use this demo client but point it to our contacts app backend as a starting point.

    git clone git@github.com:Instawork/hyperview.git
    cd hyperview/demo
    yarn <1>
    yarn start <2>

1.  Install dependencies for the demo app
    
2.  Start the Expo server to run the mobile app in the iOS simulator.
    

After running `yarn start`, you will be presented with a prompt asking you to open the mobile app using an Android emulator or iOS simulator. Select an option based on which developer SDK you have installed. (The screenshots in this chapter will be taken from the iOS simulator.) With any luck, you will see the Expo mobile app installed in the simulator. The mobile app will automatically launch and show a screen saying “Network request failed.” That’s because by default, this app is configured to make a request to http://0.0.0.0:8085/index.xml, but our backend is listening on port 5000. To fix this, we can make a simple configuration change in the `demo/src/constants.js` file:

    //export const ENTRY_POINT_URL = 'http://0.0.0.0:8085/index.xml'; <1>
    export const ENTRY_POINT_URL = 'http://0.0.0.0:5000/'; <2>

1.  The default entry point URL in the demo app
    
2.  Setting the URL to point to our contacts app
    

We’re not up and running yet. With our Hyperview client now pointing to the right endpoint, we see a different error, a “ParseError.” That’s because the backend is responding to requests with HTML content, but the Hyperview client expects an XML response (specifically, HXML). So it’s time to turn our attention to our Flask backend. We will go through the Flask views, and replace the HTML templates with HXML templates. Specifically, let’s support the following features in our mobile app:

*   A searchable list of contacts- Viewing the details of a contact- Editing a contact- Deleting a contact- Adding a new contact
    

**Zero Client-Configuration in Hypermedia Applications**

For many mobile apps that use the Hyperview client, configuring this entry point URL is the only on-device code you need to write to deliver a full-featured app. Think of the entry point URL as the address you type into a web browser to open a web app. Except in Hyperview, there is no address bar, and the browser is hard-coded to only open one URL. This URL will load the first screen when a user launches the app. Every other action the user can take will be declared in the HXML of that first screen. This minimal configuration is one of the benefits of the Hypermedia-driven architecture.

Of course, you may want to write more on-device code to support more features in your mobile app. We will demonstrate how to do that later in this chapter, in the section called “Extending the Client.”