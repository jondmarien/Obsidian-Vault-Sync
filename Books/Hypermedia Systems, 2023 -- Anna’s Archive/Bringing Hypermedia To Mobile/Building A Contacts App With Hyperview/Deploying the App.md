# Deploying the App

With the completion of the contact creation UI, we have a fully implemented mobile app. It supports searching a list of contacts, viewing the details of a contact, editing and deleting a contact, and adding a new contact. But so far, we’ve been developing the app using a simulator on our desktop computer. How can we see it running on a mobile device? And how can we get it into the hands of our users?

To see the app running on a physical device, let’s take advantage of the Expo platform’s app preview functionality.

1.  Download the Expo Go app on an Android or iOS device.
    
2.  Restart the Flask app, binding to an interface accessible on your network. This might look something like `flask run --host 192.168.7.229`, where the host is your computer’s IP address on the network.
    
3.  Update the Hyperview client code so that `ENTRY_POINT_URL` (in `demo/src/constants.js`) points to the IP and port that the Flask server is bound to.
    
4.  After running `yarn start` in the Hyperview demo app, you will see a QR code printed in the console, with instructions on how to scan it on Android and iOS.
    

Once you scan the QR code, the full app will run on the device. As you interact with the app, you will see HTTP requests made to the Flask server. You can even use the physical device during development. Any time you make a change in the HXML, just reload the screen to see the UI updates.

So we have the app running on a physical device, but it’s still not production ready. To get the app into the hands of our users, there’s a few things we need to do:

1.  Deploy our backend in production. We need to use a production-grade web server like Gunicorn instead of the Flask development server. And we should run our app on a machine reachable on the Internet, most likely using a cloud provider like AWS or Heroku.
    
2.  Create standalone binary apps. By following the instructions from the Expo project, we can create a `.ipa` or `.apk` file, for the iOS and Android platforms. Remember to update `ENTRY_POINT_URL` in the Hyperview client to point to the production backend.
    
3.  Submit our binaries to the iOS App Store or Google Play Store, and wait for app approval.
    

Once the app is approved, congratulations! Our mobile app can be downloaded by Android and iOS users. And here’s the best part: Because our app uses the hypermedia architecture, we can add features to our app by simply updating the backend. The UI and interactions are completely specified with the HXML generated from server-side templates. Want to add a new section to a screen? Just update an existing HXML template. Want to add a new type of screen to the app? Create a new route, view, and HXML template. Then, add a behavior to an existing screen that will open the new screen. To push these changes to your users, you just need to re-deploy the backend. Our app knows how to interpret HXML, and that’s enough for it to understand how to handle the new features.