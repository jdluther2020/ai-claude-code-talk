# The Model Context Protocol - Video Transcript (Formatted)
**Medium Blog: [💠 Anthropic Talk — The Context of the Model Context Protocol (MCP)](https://medium.com/ai-ml-human-training-coaching/anthropic-talk-the-context-of-the-model-context-protocol-mcp-7a6ff7d160cb)**

---

**Video:** https://www.youtube.com/watch?v=CQywdSdi5iA

**Speakers:** Alex Albert, Theo Chu, David Soria Parra

**Duration:** 19 minutes

---

## Introduction
**[0:00]**

**David:** Around the time, in September, we had an internal hackathon, and everyone was free to build basically whatever we wanted to build. But it turns out everyone just built an MCP.

**Theo:** It was crazy! Everyone's ideas were, "Oh, but what if we made this an MCP server?"

**Alex:** Hey, I'm Alex. I lead Claude Relations here at Anthropic.

**Theo:** Hi, I'm Theo. I'm a product manager on MCP.

**David:** Hey, I'm David, member of technical staff at Anthropic and one of the co-creators of MCP.

**Alex:** Today we're gonna be talking about the Model Context Protocol and diving in deep into what it is and what's next.

---

## MCP and Core Components
**[0:35]**

**Alex:** Thank you both for coming on. Very excited to talk about MCP. But first, there's a lot of talk about MCP and not a lot of maybe real deep understanding of what it is. Can we dive into how you view MCP and what it really means to be using MCP or building on it?

**David:** MCP is just a way for putting my workflow into an AI application in a very simple way. I think that's how I really wanted it to be initially, or that's how we want it to be. But it's just a way to give context to an application that uses an LLM. And that's just as simple as that. And that can be tools, it can be just raw context, whatever you like it to be.

**Alex:** How is that different than you calling an API or something like that? It's passing this information from one place into the prompt, basically, of the model. What makes MCP special here?

**David:** I think the question is: what do models interact with? And they don't interact directly with APIs. They interact with prompts and tools and whatever you're giving the model to ingest. And so MCP standardizes how you take that data from, whether it's an API or some internal data source or whatever it is, how you take that data and then actually give it to the model.

**Alex:** So this is a protocol then. It's defining that sort of interaction pattern. What are the main aspects of this protocol that you have, that it has to follow?

**David:** The main part is that it's a protocol between the AI application that uses an LLM, and it exposes basically three main things. It's tools, it's a thing called resources, which is just raw data that you could ingest into a RAG pipeline or whatever you want it to do, and there's prompts. And that's the three main things that a server can expose for now.

**Alex:** So tools are like actions that the model can take out in the world. Resources could be files, texts...

**David:** Files, data, whatever kind of context you want to give the model.

**Alex:** And then prompts are?

**David:** Just like what a user wants to put into the context window by themselves, triggered by the user and just put into the context window, and then they can edit it as they want to. That's really what prompts are for - prompt templates at the end of the day.

**Alex:** Prompt templates, I see. So literally defining the prompt itself.

**Theo:** We typically see that being implemented as a slash command.

**Alex:** Oh okay, I see. So if you're in the AI application of your choice, you would do a slash command and it would pull in the prompt template.

**Theo:** Exactly.

**Alex:** Save you time from having to write that out, whatever it is. Okay, that's MCP at its most basic form. There's definitely a lot of nuance in there.

---

## How It Started
**[3:13]**

**Alex:** What was the origin of all this? How did this come about?

**David:** The origin, I think, the most basic thing is that I worked on internal developer stuff, and I got very quickly frustrated about having to copy things in and out of Claude Desktop and then copying things back and forth between my IDE. And that's just really what I was thinking about - how can I solve copy and pasting the things I care about the most between these two applications? And that's really the absolute origin of where MCP started, at least in my mind.

And then from there, I explained that to Justin, who's the other co-creator, and he really took it and ran with it. And then we together just built it out and built it into Claude Desktop. And I think there was a pivotal moment that you alluded to. Do you want to talk about the hack week?

**Theo:** I feel like you should take the story.

**David:** Okay, yeah. Hack week was fun. We weren't really sure - is this gonna work? But around the time, in September, we had an internal hackathon, and everyone was free to build basically whatever they wanted to build. But it turns out everyone just built an MCP.

**Theo:** It was crazy! Everyone's ideas were, "Oh, but what if we made this an MCP server?"

**David:** Yeah! And we had everything from people doing very standard things like Slack integration or things you would think of when you think MCP, up to people who steered their 3D printer with MCP. And I love this - when it got into the real world, when Claude got into the real world because of an MCP server.

**Alex:** What was it? Because I remember that too when we were doing all these hackathon projects. And there was no mandate to force people to use MCP. This was just an entirely organic thing. Why did people gravitate towards MCP for all their projects?

**Theo:** I think it really was that standardization layer just made it so much easier to add context to the application. Because the moment that Claude is now integrated against MCP, that means as the server builder, you can build 1, 10, 20, however many servers you want, and you know that it will automatically work with that application. And so I think that just gives you the ability to only think about one side and not have to think about the other side.

**David:** I think there's a bit of a magic moment when you teach Claude something new using an MCP server for the first time, and you see it take action about something you care about. And I feel that's a little bit of a moment of magic that I think MCP captures really well, which makes people so excited. Because within five minutes there's something going.

**Alex:** Right, right. Yeah, I've seen it myself, and I mean even experienced it, where it almost feels like you take Claude out of the box, so to speak. And all of a sudden, instead of just being this thing that is just right there outputting text, it's doing other things. It's calling other applications, fetching their data, or even operating a 3D printer, which is a really crazy thing. And that does feel really special. And I guess MCP allows that pretty seamlessly to some degree.

So this was back in end of summer, early fall...

---

## Launching MCP and Reception
**[6:22]**

**Alex:** ...as we were doing hack week and these other things. When did we launch MCP, and what did that look like?

**Theo:** We launched MCP around Thanksgiving.

**David:** Yeah, November 2024.

**Alex:** And how was that launch? What was the reception?

**Theo:** Slow at first. I think everyone's response is, as you can imagine - well, some people still have this response - what's MCP?

**Alex:** Right?

**Theo:** We... naming is hard. We definitely could have named it better.

**Alex:** It's arguable now, it's kind of caught its storm.

**Theo:** I know. That's fair. But you still get "MPC" instead of "MCP," and then it makes me think "NPC," and you know?

**Alex:** Yeah, acronyms are hard.

**Theo:** But yeah, acronyms are hard. But you had a lot of people asking "what is MCP?" - not just externally, but I also think internally, because it was such a bottoms-up movement. You know, initially people were like, "Oh, what is this thing? What does it mean to give the model context?"

And then as people started playing around with it and seeing it for themselves, I think that's where it actually slowly caught steam. And the turning point was when more and more clients started adopting. So I think the IDEs were the first to adopt. More recently we've seen a lot of adoption from model providers, and that's created a lot of waves in the market to incentivize a lot more server providers to actually build servers.

**David:** I think one part is you see so many times on social media: "What is MCP? Why would I ever want this?" And then a month later, a few days later, they're like, "This is the best thing ever!" We have so many of these stories, and it's so funny.

**Alex:** Yeah, so it's now become, I think it's fair to say, an industry standard integration protocol. I mean, there's nothing else in my mind that kind of rivals it.

---

## Making It Open Source
**[8:12]**

**Alex:** But I think going back to the launch, a key decision here was to actually make this open source. And that was pretty different in comparison to maybe previous efforts in this area that had been launched. Can you explain the reasoning behind that decision and why we open sourced it?

**Theo:** Yeah, if you have a closed ecosystem for integrations and for context to be provided to AI applications, then it isn't clear to the server builders or the integration builders - is that AI application gonna be around forever? Should they invest in that? Which ones should they invest in? And so by making it an open standard, you really kind of decrease the friction to even building those integrations.

And we believe that the value of building an AI application is not necessarily which integrations you have access to, but the model's intelligence and the workflow that you build on top of the model. So we wanted to focus the industry on those two things and not necessarily on building integrations.

**Alex:** That makes sense. And there also seems potentially with open source, there's this kind of cycle you can get into where somebody contributes to a server, and then somebody uses it and they notice bugs in it, and then they're like, "Oh, I can just go fix it myself." And that maybe speeds it all up.

**David:** There's another part to that - Justin and I just like open source.

**Alex:** Hey, sometimes it's the simplest thing!

**David:** Yeah!

**Alex:** So now we have lots of companies adopting MCP into their own products. We have lots of other developers and companies creating servers to be plugged into all these clients.

---

## Current State
**[9:55]**

**Alex:** What does this look like across the industry now? What's the current state of MCP?

**Theo:** The current state is that we have major players adopting it across their products. We have a really big ecosystem of MCP server builders - it's like 10,000-plus. And it's at this interesting intersection that initially was mostly focused on developers and a very local experience, where the servers would run local and the software they use would run local.

And I think we have this inflection point where we're starting to see these servers being hosted in the cloud, like as a web thing through what we call "remote MCP." And Claude AI integrations is really the first big entry to that, that allows you to connect just like a website that offers an MCP server into your day-to-day Claude AI workflow.

And I feel this is a pivotal moment where it can be a true standard for the web for how LLMs interact with that. I think we'll see how this works out. But yeah, I think that's where we're currently at. And we do of course have an increasingly bigger community being built around us. And this is big companies, but it's also sometimes just open source people who just like working on MCP, and that's just becoming bigger.

**David:** The craziest thing is someone fixed our docs this morning because we had an image that was out of date, and they just submitted the PR. We accepted it.

**Alex:** That's why you want to do it open source!

**David:** Yeah, that's... I love that!

**Theo:** I love that the community gets behind it and they also feel ownership and wanting to maintain it as well.

**Alex:** And it seems like, I mean, we were chatting about this before we started filming - there's a lot of things happening in the MCP world too, outside of just working on the protocol. What's going on in your world these days with MCP?

**David:** Yeah, it has a lot, right? There's conferences on MCP. There's just a lot of conversation. There's partnerships where we work with big companies on evolution of the specification and what their problems are. I learned a lot about enterprise deployments and the needs for identity and authorization in that space over the last few months, and had help from some of the best people in the world around this. And that's just a little bit of that world of MCP at the moment.

**Alex:** That's awesome. Yeah, I'm just blown away by the response. And I'm starting to see now online posts around, "Is this what it looks like to witness the birth of a new protocol? Is this what it was like to be around for HTTP or something like that?" How would you guys liken those comparisons? Is this a new protocol of that sense, or how can we expect to frame this in comparison to things we've seen in the past?

**Theo:** I mean, I would hope so. None of us can see the future. You know, knock on wood that we've landed on the right thing. But I think that's where the community can help guide us. The hope is that we have hit on the right problem of providing context to LLMs and that we have thought far enough ahead that all the right building blocks are there, and the community can help guide us as we're evolving it into the next few steps.

**David:** I think from my perspective, we just need to build something that people want to use and build this together with people who care about this. And I think you don't need to compare it to HTTP or anything else. It's just like, just make something that people want to use, and that's it at the end of the day.

---

## Tips for Getting Started
**[13:23]**

**Alex:** So if I'm a developer and I'm new to MCP, and I want to become involved, and I also want to learn a little bit about how to work with MCP, do you have any tips for this person?

**Theo:** I think the first thing that I would do is go look at an existing server that is online. Go play around with it, see how it works with Claude AI or Claude Desktop if you want to play around with local MCPs. But just get a feel for what that interaction pattern is first, and that will make it much easier for you to then build your own MCP.

And start with the classic, you know, "hello world." Just do one tool, just respond with "hello world." Do the same thing for prompts, resources. Just try the very basic thing for each before you go into anything more complex. And I think once people get a feel for that, they realize how easy it is.

**David:** Yeah, I would certainly just start local. Just whip out Claude Code and just write code, an MCP server, and just go from there. I think that works actually surprisingly well. With 10 minutes you can have something. And then yes, what Theo said - just look at great servers and what they do and make modifications from there.

**Alex:** Yeah, it's funny you say that. I was experimenting the other day with just getting the docs from Model Context Protocol dot IO, pasting it into Claude Code, and then like "make me a server." And I didn't even have to paste in the content or anything. Claude Code went, grabbed it, fetched it, brought it in, made the server. It was like a very easy example right there of just how quickly you can get started with some of these things, especially when you have Claude under the hood powering it.

---

## Favorite MCP Servers
**[14:57]**

**Alex:** Any favorite MCP servers that you guys have seen out in the world so far?

**David:** I really like those MCP servers that bridge the gap to the real world. Like I'm a person who likes music, and I have synthesizers at home, and there's an MCP server that someone created to control their synthesizer. And I just love that. It's just like, here's Claude interacting with a physical device that later makes music, and that's just so cool in my mind.

I love those, and I love the creative ones. I love the ones where people play around with Blender. I love the quirky ones. Like one of our team members has Claude control his door through an MCP server and role-play a doorman. And it's just like, I love that creativity.

**Alex:** I mean really with that, it's like the possibilities are endless. Anything that you could ping through an API or anything, you could wrap in an MCP server and then control it with Claude or another LLM. And the Blender one - explain that. So somebody was actually using Claude to control Blender just through MCP?

**David:** Yeah, basically the MCP server just writes Blender scripts into Blender. And you see in - you know, there's lots of videos, you should check it out - you just see Claude calling these tools, and on the side Blender just creates a scene out of nowhere. And it's actually just not the person, it's Claude creating it. And I love it.

**Alex:** That's awesome. I love that.

---

## Claude 4 Improvements
**[16:23]**

**Alex:** Let's switch gears a little bit. So we just recently released Claude 4 - Opus and the new Sonnet. What does this enable for MCP, and how does this connect into this broader theme we're seeing around agents and AIs that can kind of operate on longer time horizons?

**Theo:** As we get into models with more intelligence that can do longer running tasks, I think some of the primitives that we've actually built into MCP are going to become more used that right now may not have gotten as much adoption. So, you know, things related to statefulness, things related to actually doing sampling... but those are the primitives that we thought about in the beginning that actually help in an agent's world, but do require the models to have the amount of intelligence where they can start doing longer running tasks.

**Alex:** That's interesting. So some of these things that maybe haven't been utilized so much just yet will become more and more important because the models just get more capable and they're able to use them.

**David:** It also just makes it probably easier to put more MCP servers - attach them - and Claude is just gonna get better and better at distinguishing which one it needs to take action.

**Alex:** How many MCP servers can you throw at Claude at once? How does it know how to choose between them?

**David:** Depends.

**Alex:** Good question!

**David:** It depends because it depends on how the tools are written, are they overlapping? If you put three issue tracker MCP servers next to each other, of course the model can get confused. But if it's an issue tracker thing and I don't know, something completely different, then it becomes pretty easy. Then you can put a lot of them next to each other. It's just a matter of your workflow and how overlapping they are at the end of the day.

**Alex:** I see. And I'm assuming as models get more capable and intelligent, it becomes like you can throw more and more at them too.

**David:** Yeah.

**Alex:** So what's next for MCP?

---

## What's Next
**[18:18]**

**Theo:** The protocol is now live. There's good adoption, but we can do a better job of helping people understand what it is. So we're definitely going to invest in more examples, better documentation.

We're also investing in key security primitives. So the thing I think most people are gonna be excited about is agents and how we're thinking about agents.

So for agents, one really big ship that's coming is the **registry API**. That is going to allow models to actually go and search for additional servers that they can then bring into the LLM. That then allows kind of a little bit more of an agentic loop, since the client doesn't just get to decide "here are the 10 things that I am aware of and that I want the model to have context to." The model can now go and search for more things on demand.

The second is **long running tasks**. So actually making it easy for you to do longer running things with MCP.

And then the third one is **elicitation**. So how do you as a server actually go back and ask the user for more information if you need more information?

**Alex:** Exciting! Well, I'm very excited to see what the future holds for MCP. And thank you both for coming on.

**Theo & David:** Thank you!

---

**[End of Video - 19:30]**

---

**Formatted for easy reading while watching**
**Created:** 2026-02-02
**Source:** Official Anthropic MCP video
