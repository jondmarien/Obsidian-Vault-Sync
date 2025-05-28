# What Is Hypermedia?

> Hypertexts: new forms of writing, appearing on computer screens, that will branch or perform at the reader’s command. A hypertext is a non-sequential piece of writing; only the computer display makes it practical.
> 
> ℄ Ted Nelson, https://archive.org/details/SelectedPapers1977/page/n7/mode/2up

Let us begin at the beginning: what is hypermedia?

Hypermedia is a media, for example a text, that includes _non-linear branching_ from one location in the media to another, via, for example, hyperlinks embedded in the media. The prefix “hyper-” derives from the Greek prefix “ὑπερ-” which means “beyond” or “over”, indicating that hypermedia _goes beyond_ normal, passively consumed media like magazines and newspapers.

Hyperlinks are a canonical example of what is called a _hypermedia control_:

Hypermedia Control

A hypermedia control is an element in a hypermedia that describes (or controls) some sort of interaction, often with a remote server, by encoding information about that interaction directly and completely within itself.

Hypermedia controls are what differentiate hypermedia from other sorts of media.

You may be more familiar with the term _hypertext_, from whose Wikipedia page the above quote is taken. Hypertext is a sub-category of hypermedia and much of this book is going to discuss how to build modern applications using hypertexts such as HTML, the Hypertext Markup Language, or HXML, a hypertext used by the Hyperview mobile hypermedia system.

Hypertexts like HTML function alongside other technologies crucial for making an entire hypermedia system work: network protocols like HTTP, other media types such as images and videos, hypermedia servers (i.e., servers providing hypermedia APIs), sophisticated hypermedia clients (e.g., web browsers), and so on.

Because of this, we prefer the broader term _hypermedia systems_ when describing the underlying architecture of applications built using hypertext, to emphasize the system architecture over the particular hypermedia being used.

It is the entire hypermedia _system architecture_ that is underappreciated and ignored by many modern web developers.