""" let's get started uh so here is what we'll be covering in this course first we will talk about what is slang chain why we
use it what problem does it actually solve and then we will set up our python environment so that we can actually
start using Lang chain and start interacting with these apis right so once we have that setup we are then
going to start diving deep into the core components of Lang chain first off we're going to start working with chat models
meaning uh we'll basically just interact with open AI chat models CL chat models all of that in the first section the
second core component of flank chain is going to be prompt templates basically make our prompts to the AI as templates
and add placeholders in it so that it can take Dynamic values all right the next component it gets really
interesting from this point onwards the third component of L chain is going to be chains okay so chains and L chain are
like an assembly line each step handles a specific task and passes it to the next next here's a real world example
okay so imagine chains like making a coffee right first you have to grind it then Brew it then steam it and then serf
it right so that's exactly what we're doing here as well so if there is a complex workflow we'll be dividing it
into smaller tasks and once the first task is done the result of that is passed to the second task so that is why
it's even called Lang chain and even the logo of L chain has a picture of chains because it links various processes like
models chat models prompts databases calls into a unified workflow and we have plenty of real world examples for
that as well in this course and then we have Rags this is a pretty huge section in this course and it's one of those
important technologies that are helping businesses to increase productivity so if you've ever heard of custom chatbots
trained on a company's private data the data could be in the form of PDFs or it could be from the database or and users
can sort of chat with the data then this is what's going on Rags or retrieval augmented generation and finally we are
going to wrap up this course with another critical component of L chain which is called agents and tools
basically think of AI agents like a human agent who can see a problem and use various tools to solve that
particular problem it can sort of interact with apis send emails automatically scrape data from a website
run a python script or even query a database I'll give you an example imagine an AI agent gets a task to book
a meeting just like a human it can check your calendar it can send an email invite it can update the CRM as well all
automatically right so that is the power of longchain Agents they can use the right tool for each and every single
step here is a quick tip if you want to get a complete overview first try watching the whole course at 2x speed
then you can go back and focus on the parts that you actually need most that's how I learn it because it lets me see
the big picture first and see how everything sort of fits together in the next section let's talk about what is
Lang chain why we even need it I'm pretty excited and I'll see you there all right so to understand what
Lang chain is let's start with a very simple problem so imagine you want to plan a vacation and you want to seek the
help of CH so I'm going to say something like I want to plan a trip to Paris the Saturday can you book my flight also
book a hotel the same day and suggest some good restaurants okay so let's actually see what happens behind the
scenes I'm not pressing enter just yet so when I press enter this query is sent to an llm model so this chity
application might use a lot of models it might use CHD 3.5 Char 40 40 mini a lot of other models right so these are the
large language models that you see on the right side the chib application itself is just an interface for the user
like you and me right so when I press enter let's see what happens right so you can see that it says I cannot make bookings directly but
I can help you with planning right so this is one of the biggest limitations of large language models they are smart
and can talk about travel but they cannot actually interact with the real world right so on its own the llms are
just the brains right they can be trained on certain data and it will reason with it right but it cannot do
anything outside of it let's say you want to build an application that needs to have the brains basically the
reasoning ability of an llm but at the same time it also should have the ability to communicate with the real
world right communicate with real world apis databases right send emails if you want to do that we need to have some
sort of a framework right in the middle right and that is where Lang chain comes into the picture Okay so Lang chain acts
as a bridge between the llms and the real world so to put it simply Lan chain is by far the most popular framework
that helps build applications using llms right so in the future if you want to switch out GPT 40 with let's say a free
hugging face llm if you're shot on cash let's say you can easily do so without even touching the code that you wrote
with L chain right so with L chain the AI that we working with can do so much more in real world I'll give you a few
examples so it can access a lot of apis for example it can access flight and restaurant booking API from let's say
booking.com or open.com it can access private company databases to answer customer queries it can send emails it
can browse Google Wikipedia it can scrape websites and a lot lot more right so Lang chain doesn't just make the AI
smarter it gives it the ability to act in the real world this is just a very small example so as we go through the
course we will explore a lot more use cases so I hope you're excited let's get started all right so let us talk about the
prerequisits first to be able to follow along with this course you will need python version 3.8 or higher installed
and the second thing is make sure that you have a code editor installed as well I will be using vs code in this course
and last but not least you will also have to create an open AI account because we will be using open AI apis in
this course if you don't have python installed I have attached Python 3 installation tutorial links in the
description for both windows as well as Mac so once you're done installing you can come back to this video and for vs
code you can go to this particular link right here and then you can download visual studio code for whichever
operating system that you working with the installation is also pretty straightforward for this and finally
let's go ahead and create an open AI account if you don't have it already the reason why we need that is because we
need the API key in order to be able to hit that API Endo to access open llms right so to do that let's go to platform.
open.com okay so I'm going to log in because I already have an account uh if you don't you can just go ahead and sign
up right here so once you're in you can click on this dashboard tab right here on your left side you can see a tab for
API keys so we can click on it so if you've never created a key before you might see an empty list right here so
let's actually go ahead and create a new one by clicking on this button I'm going to name it Lang chain
tutorial I'm going to leave the permissions as all and let's go ahead and create it all right so we have it
right here also please make sure to save it somewhere in your computer because if you lose it you will have to create
another one again okay and that's it so far we have installed Python 3 we've installed Visual Studio code as well as
we've created an openi account and created an API key as well so in the next section let us actually go ahead
and set up our development environment using python so that we can actually start working with L chain so I'll see """