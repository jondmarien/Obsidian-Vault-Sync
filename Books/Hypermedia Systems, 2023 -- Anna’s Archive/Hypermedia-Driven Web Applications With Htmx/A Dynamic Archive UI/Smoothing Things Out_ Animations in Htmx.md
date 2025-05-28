# Smoothing Things Out: Animations in Htmx

As nice as this UI is, there is one minor annoyance: as the progress bar updates it “jumps” from one position to the next. This feels a bit like a full page refresh in web 1.0 style applications. Is there a way we can fix this? (Obviously there is, this why we went with a `div` rather than a `progress` element!)

Let’s walk through the cause of this visual problem and how we might fix it. (If you’re in a hurry to get to an answer, feel free to jump ahead to “our solution.”)

It turns out that there is a native HTML technology for smoothing out changes on an element from one state to another: the CSS Transitions API, the same one that we discussed in Chapter 4. Using CSS Transitions, you can smoothly animate an element between different styling by using the `transition` property.

If you look back at our CSS definition of the `.progress-bar` class, you will see the following transition definition: `transition: width .6s ease;`. This means that when the width of the progress bar is changed from, say 20% to 30%, the browser will animate over a period of .6 seconds using the “ease” function (which has a nice accelerate/decelerate effect).

So why isn’t that transition being applied in our current UI? The reason is that, in our example, htmx is _replacing_ the progress bar with a new one every time it polls. It isn’t updating the width of an _existing_ element. CSS transitions, unfortunately, only apply when the properties of an existing element change inline, not when the element is replaced.

This is a reason why pure HTML-based applications can feel jerky and unpolished when compared with their SPA counterparts: it is hard to use CSS transitions without some JavaScript.

But there is some good news: htmx has a way to utilize CSS transitions even when it replaces content in the DOM.

## The “Settling” Step in Htmx

When we discussed the htmx swap model in Chapter 4, we focused on the classes that htmx adds and removes, but we skipped over the process of “settling.” In htmx, settling involves several steps: when htmx is about to replace a chunk of content, it looks through the new content and finds all elements with an `id` on it. It then looks in the _existing_ content for elements with the same `id`.

If there is one, it does the following somewhat elaborate shuffle:

*   The _new_ content gets the attributes of the _old_ content temporarily.
    
*   The new content is inserted.
    
*   After a small delay, the new content has its attributes reverted to their actual values.
    

So, what is this strange little dance supposed to achieve?

Well, if an element has a stable id between swaps, you can now write CSS transitions between various states. Since the _new_ content briefly has the _old_ attributes, the normal CSS transition mechanism will kick in when the actual values are restored.

## Our Smoothing Solution

So, we arrive at our fix.

All we need to do is add a stable ID to our `progress-bar` element.

    <div class="progress" >
        <div id="archive-progress" class="progress-bar" role="progressbar"
             aria-valuenow="{{ archiver.progress() * 100 }}"
             style="width:{{ archiver.progress() * 100 }}%">div> <1>
    div>

Smoothing things out

1.  The progress bar div now has a stable id across requests.
    

Despite the complicated mechanics going on behind the scenes in htmx, the solution is as simple as adding a stable `id` attribute to the element we want to animate.

Now, rather than jumping on every update, the progress bar should smoothly move across the screen as it is updating, using the CSS transition defined in our style sheet. The htmx swapping model allows us to achieve this even though we are replacing the content with new HTML.

And voila: we have a nice, smoothly animated progress bar for our contact archiving feature. The result has the look and feel of a JavaScript-based solution, but we did it with the simplicity of an HTML-based approach.

Now that, dear reader, does spark joy.