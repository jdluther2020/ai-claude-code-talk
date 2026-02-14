# The Future of Agentic Coding with Claude Code — Boris Cherny & Alex Albert

**Video:** https://www.youtube.com/watch?v=iF9iV4xponk

**Speakers:** Boris Cherny (Claude Code Creator, Anthropic) & Alex Albert (Claude Relations, Anthropic)
**Date:** September 2, 2025

---

## Video Info

### Description
Anthropic's Boris Cherny and Alex Albert discuss the current and future state of agentic coding, the evolution of coding models, and designing Claude Code's "hackability." Boris also shares some of his favorite tips for using Claude Code.

### Resources
- Learn more: http://clau.de/future-of-agentic-coding
- Claude Code docs: https://clau.de/claude-code-docs

### Timestamps
- 0:00 — Introductions
- 0:39 — The current state of agentic coding
- 5:20 — The evolution of coding models
- 7:39 — Coding model evaluation
- 8:56 — Claude Code user feedback loops
- 10:34 — The "hackability" of Claude Code (CLAUDE.md, MCP, slash commands)
- 13:11 — The future of agentic coding
- 14:49 — How to upskill for agentic coding
- 17:49 — Claude Code tips and tricks

---

## Introductions (0:00 - 0:37)

**Alex:** I think back to when I first started learning coding, I was the kid that sat in the back of math class in middle school, and I had my little TI-83 Plus calculator. I just programmed it with BASIC because at some point I realized that I can actually program the answers for the math test into the calculator.

Hey, I'm Alex. I lead Claude Relations here at Anthropic. Today we're gonna be talking about Claude Code and the future of software engineering.

**Boris:** I'm Boris. I'm a member of technical staff here at Anthropic and creator of Claude Code.

---

## The Current State of Agentic Coding (0:39 - 5:19)

**Alex:** A lot has happened in the past 12 months, and things are moving very, very fast, especially in the coding domain. Can you kind of catch us up here on what's happened, and where are we standing currently?

**Boris:** A year ago coding was totally different than what it is today. A year ago, if you want to write code, you have an IDE with some sort of autocomplete, and then there's some sort of chat app, and you might copy and paste code back and forth a little bit. That was the state of the art.

I think sometime around a year ago we started to see agents appear as a thing that people earnestly use in coding. It's like a part of the workflow now. It's not like a gimmick or a prototype. It's actually part of the inner loop when you're doing development.

What's changed the most is: when you code, you use an agent. You don't directly manipulate text in an IDE anymore. It's not just about autocomplete; it's about the model writing code for you.

**Alex:** So we've gone from it all being within a web app where you're copy and pasting the code out and making very targeted edits, to just being a lot more hands-off and telling an agent what you want it to do, and then trusting it to go make tons of edits and create whole apps sometimes even by itself.

**Boris:** Exactly. The reason we couldn't do it a year ago is because the models weren't really good enough, and the scaffolding—the thing on top of the model—wasn't good enough.

When we initially launched Claude Code, it was still using Sonnet 3.5. It sort of worked. I used it for maybe 10% of my code at first. But I remember when we launched it to the core team, I walked in one morning and saw engineers already using it after just giving it to them the day before. The model wasn't very good, the harness wasn't very good, but even in this early version, it was already a little bit useful.

Over the last year, the model has gotten way better at agentic coding with 3.7 and now 4.0 and Opus 4.1. And the harness—Claude Code—has also gotten a lot better.

---

## The Evolution of Coding Models (5:20 - 7:38)

**Alex:** When you say coevolve, is that because it's a deliberate thing in the training, or how is the model getting better at these sorts of things as we make the product features itself better?

**Boris:** It's pretty organic. At Anthropic, everyone uses Claude Code. That includes the researchers. Every day the people building the models are using the model in order to do their job.

As part of that, you kind of see natural limits that you hit with a model. For example, maybe the model's really bad at doing certain kinds of edits, and you see "failed to replace string" errors. This is a model capability, and we can improve this if we learn from it.

Or at a higher level, maybe if you let the model work for 30 minutes with 3.5, it could stay on track for a minute or so. But with newer models, this amount of time the model can operate autonomously gets longer and longer. This is really based on experience—you use the model, you see where you have to course correct and steer it, and then we incorporate that into the model and teach it to do this better itself.

---

## Coding Model Evaluation (7:39 - 8:55)

**Alex:** When you're evaluating a new model, do you kind of have a vibe check set of tests that you run? Or if it's like a new feature that we're rolling out, how do you personally evaluate if the performance is getting better?

**Boris:** I just do my work that day. My perfect day is I'm just coding all day. Whatever the model is, whatever is the new thing we're testing, I'll just code using that and see what the vibe is. There isn't a specific test I do.

In day-to-day work you do all sorts of stuff—writing new code, fixing bugs, reading Slack messages or GitHub issues to respond to feedback. I think more and more the model is able to do more and more of this. If you had maybe one thing that you always use the model for, you would miss out on some of these newer capabilities, like pulling in context through MCP, like reading your Slack messages, or automatically debugging stuff by pulling in Sentry logs.

**Alex:** So the best eval in some sense is the one that most looks like real life. And in that case, just using it gives you the best result.

**Boris:** We tried really hard to build product evals when building Claude Code, but honestly it's just so hard to build evals. By far the biggest signal is just the vibes. Does it feel smarter?

---

## Claude Code User Feedback Loops (8:56 - 10:33)

**Alex:** Claude Code has like the best dogfooding cycle I've seen of any type of product. Do you think there's something you did uniquely to set up that feedback loop internally?

**Boris:** Initially, I built it the way I do any other product: just listen to users and make it as easy as possible to listen to users.

When we built Claude Code, there was just a single feedback channel in Slack. Anytime anyone had feedback, I would direct them to that. People hesitated sometimes because when you give feedback, you expect that no one listens and it goes into this black hole.

One of the things that we did really right was: from the beginning, whenever someone gave feedback, I would try to fix it as fast as I can. Sometimes I would go into the office and spend like three hours or two hours, just go through as many bugs as I can and fix them as fast as I can, and then every time comment back and tell people it's fixed. This encourages them to keep giving feedback.

To this day the Claude Code feedback channel internally is just a fire hose, nonstop.

**Alex:** I remember dropping in there, posting something, and immediately you're reacting with emoji. Or you're asking for clarification, and you do feel like, okay, my feedback's being heard. You're able to be incentivized to go post more feedback in the future.

**Boris:** Yeah, because honestly, I don't know what I'm doing. No one really knows what they're doing with AI. We're discovering this thing as we build it. The best indicator is what the users want. So you gotta listen.

---

## The "Hackability" of Claude Code (10:34 - 13:10)

**Alex:** What is like the current state of Claude Code as a product? What are the latest features? What are you excited about?

**Boris:** Claude Code, from the start, was built to be the simplest thing it can and to be as hackable as possible. The hackability is something we've been developing a lot.

Originally, the way to hack Claude Code was adding to its CLAUDE.md. That was the original extension point. You can put it in the root directory, in child directories—different places.

Over time we've added a lot more extension points:
- **Settings and permissions system** — Very sophisticated now
- **Hooks** — Dixon built this, an extensive hook system. He saw all these different user asks for "I want to extend it this way, I want to hook into this"
- **MCP** — A really great extension point
- **Slash commands and subagents** — We've invested in this a lot. User-defined slash commands are just a workflow—a markdown file you put in your code that you can reuse

For example, I have a slash command for making commits. I have instructions: here's how you write a good git commit. I pre-allow the git commit Bash command so I don't have to accept it every time, and the model can just do it.

Slash commands are really interesting, and agents are kind of a different view of slash commands. It's like a slash command but with a forked context window. You can think of agents and slash commands as two sides of the same thing.

When I look at the future, I think a lot of it is: How do we extend Claude Code more? How do we make it easier for other people to build on top? How do we make the SDK more useful for people? The Claude Code SDK is useful if you want to build a coding agent, but also you can use it for other stuff—anything that you need an agent for.

All of this benefits from the work we're doing to make the model more autonomous, to make it work for longer periods of time, to make it better adhere to instructions, to make it remember things better. Everything along the way benefits.

---

## The Future of Agentic Coding (13:11 - 14:48)

**Alex:** So I'm using Claude Code, or whatever form of it, in six to 12 months; what does my work actually look like? Am I reviewing PRs all day, or what does it day to day break down to?

**Boris:** I think there's gonna be a mix of more hands-on coding. I don't think that's going away. Maybe it'll look different though. Maybe hands-on coding today is directly manipulating text, but in the future it might be using Claude to manipulate the text for you.

And then I think there's gonna be this other bucket of maybe less direct coding where Claude proactively does something, and maybe Claude even reviews it. And it's your job to decide if this is a change that you want or not.

I think maybe 12 or 24 months from now we're gonna start seeing Claude that's more about goals and more about higher level things that it needs to do, and less about the specific tasks that go into it. The same way that, as an engineer, I think about what is it that I want to do over the next month and I make small changes to work towards that. Maybe Claude will go through the same thing.

**Alex:** So sort of moving up and up the stack to these like abstraction levels—from getting Claude to make individual changes to files, to getting Claude to make changes to a whole PR, to getting Claude to think about a goal of building an app or whatever else it is.

**Boris:** Yeah, exactly.

---

## How to Upskill for Agentic Coding (14:49 - 17:48)

**Alex:** If I'm an engineer and I'm hearing that, it seems like there's gonna be a lot changing in a very short amount of time, especially with my role and what I should be doing. What's your advice for folks out there that are looking to prepare themselves and adapt to this world?

**Boris:** I think back to when I first started learning coding. I was the kid that sat in the back of math class in middle school with my little TI-83 Plus calculator. I programmed it with BASIC because I realized I could program the answers for the math test into it.

There's just something about this visceral feeling of being able to hack—having this idea and just going into my calculator and coding it, and then restarting and using it really quick. This feedback cycle was really amazing. It made it possible for me to build stuff that I never could have before. It was just so easy to get started.

The difference with agentic coding is that stacks got way, way too complicated before. If I wanted to make a JavaScript website, I had to learn about React and maybe Next.js, three different build systems and a deploy system. It was just so complicated.

One really cool thing about agents is that they're changing this. With coding agents it makes it really easy to get started. If you have an idea you can just build it. It's a lot more about the idea now than it is about the details, because with Claude Code, you can rewrite the code over and over.

Claude Code itself we rewrite all the time. The code itself is no longer precious. There's still an art to writing it, and you know, sometimes you write code by hand. One of the engineers on the team, Lena, still sometimes writes C++ by hand on the weekends just 'cause it's fun. As a coder, it can be a really joyous thing to do this.

But I think more and more it's gonna be about the thing you make and not about the process of making it as much.

My advice for people learning to code today: You still have to learn the craft. You still have to learn to code, learn languages, learn compilers, runtimes, how to build web apps, how to build programs, system design. You still have to know all the stuff. But also just start to get more creative.

If you have an idea for a startup or an idea for a product, you can just build it now in a way that you just couldn't before. We don't really understand what this means, but there's just so much potential that's about to be unlocked because of it.

**Alex:** I think that's great advice. Ideas suddenly become something you can action on in a span of a few minutes almost, whereas before it could be just in your backlog forever.

---

## Claude Code Tips and Tricks (17:49 - 20:15)

**Alex:** Before we wrap, I want to ask you, as the creator of Claude Code, what are your best practices for using Claude Code? And any tips or tricks.

**Boris:** I think the biggest thing that I recommend—okay, maybe two tricks.

**Trick #1: Start by Asking Questions, Not Writing Code**

If you're brand new to Claude Code and you haven't used it before, don't use it to write code yet. I know it sounds crazy, but you gotta stop yourself. Don't use it to write code yet.

The thing to start with is use it to ask questions about the code base. Ask "If I want to add a new logger, how do I do that?" and have Claude Code explore the codebase and figure it out for you. Or "Why is this function designed the way that it is?" Claude Code can go in and look through Git history and answer this stuff for you.

So ask Claude Code questions about the code base and just don't code yet. Once you feel comfortable with using Claude Code this way and you get comfortable with this idea of an agent that's doing this research for you, then start to use it to code.

**Trick #2: Right-Size Your Tasks**

When you are using Claude Code to write code, think about what kind of work you want to do and how big is the task. I have these three categories in my mind: easy, medium, and hard.

**Easy tasks** — Claude can write in one shot. One prompt, it'll get it pretty much right. Nowadays I'll just go to GitHub and tag @Claude on an issue and have Claude write the PR for me. This frees up my terminal.

**Medium tasks** — I'll start it in the terminal and go into plan mode. Just Shift+Tab into plan, and align on a plan with Claude first. Once I feel good about the plan, I'll go into auto-accept and have it implemented.

**Hard tasks** — I'm still the one driving, and Claude is more of a tool. I'm kind of pairing with it. But really I'm the one in the driver's seat, not Claude. I'll use Claude maybe to do some code-based research, prototype a few ideas, maybe vibe code a few options to understand the boundaries of the system. But I'll still mostly implement myself. Maybe Claude will write the unit tests, but it's still mostly me doing the coding.

So the second advice is: just think about what's the task that you're doing and what's the right way to use Claude Code to do it.

**Alex:** Those are great tips. Really appreciate the time, Boris.

**Boris:** Yeah, thanks, Alex.
