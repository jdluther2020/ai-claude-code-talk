# Designing Claude Code by Anthropic

YouTube Video Link: https://www.youtube.com/watch?v=vLIDHi-1PVU
```markdown
In this video, Anthropic’s Meaghan Choi (Claude Code) and Alex Albert (Claude Relations) discuss the design principles behind Claude Code, the evolution of the terminal in the age of large-language models (LLMs), and how product designers can prototype new features with agentic coding.

0:00 — Introductions

00:20 — Claude Code’s design principles

1:40 — The evolution of the terminal

3:22 — Mapping the developer workflow to Claude Code

5:10 — Prompting in the terminal

6:45 — How we design new features

8:10 — Meaghan’s favorite Claude Code design elements

9:10 — Tips and tricks for designers using Claude Code (brainstorming with Claude, scoping product development timelines, and making design tweaks after new product releases)

Learn more: https://claude.com/product/claude-code
```

## Introductions
Hi, I’m Alex. I lead Claude Relations here at Anthropic. Today we’re talking about design for Claude Code, and I’m joined by my colleague Meaghan.

Hi, my name is Meaghan, and I’m the design lead for Claude Code.

## Claude Code’s Design Principles
Meaghan, I want to start with the very unique form factor that Claude Code has. We built this coding product, and it lives within a terminal. Can you tell me how we even got to that?

Yeah, definitely. Well, if you’ve seen some of our previous videos, you know that Claude Code was a brainchild of a few folks here at Anthropic who are really passionate about Claude’s ability to solve coding problems and help developers. Part of the initial decision for a CLI (Command Line Interface) was really just the ease of the form factor — to be able to build really quickly and to iterate on features and functionality.

But from there, honestly, against my expectations and all our expectations, it took a life of its own because it’s just so versatile. A terminal is in every developer’s workflow. Whether or not you’re primarily in an IDE or even if you’re just a Vim user, you’re using a terminal as part of your workflow in one shape or another. It lets you integrate directly into developers’ workflow where they are today, without needing to adopt a new tool of any sort.

I think that’s a really good point. The terminal has been a foundational piece of software development since forever, basically. It’s almost natural to embed the next generation of a coding product within it. But Claude Code does some things that I didn’t even know were possible with a terminal. Walk me through the history of terminal products thus far, and how Claude Code is the next step.

## The Evolution of the Terminal
This is something I’m personally very passionate about. I think terminals are like the first user interface; they’re the first ways that people used to talk to computers. They were text-only. There were very specific commands you needed to know in order to interface with these devices. They are a super-powered tool.

From there, we evolved into these really rich web interfaces. We had beautiful web UI, Tailwind, CSS, and JavaScript. Everything became very animated and polished. But when LLMs came out, we actually went all the way back to just chatting with a computer again. You didn’t actually need all these buttons; you just needed to chat.

I think the terminal is actually the perfect form factor for an LLM because you’re giving text in and getting text out. It is so native to how you think about using a command line interface that it was a beautiful marriage of what the technology can do and what the product can do. It just happened to be that developers also spend their time there, so it’s great.

I see. So we’re almost going full circle to some degree because the model allows us to do it, removing the need for the UI abstractions that we’ve had to develop previously for different applications.

Exactly. I also think a big part of why Claude Code is successful is that no one likes copying and pasting things from a web UI to a local file. I definitely do this all the time when I’m using Claude.ai. And so being able to do natively in the environment where everything lives is just such a rich part of the experience. But it does come with some challenges. A CLI is not necessarily the most rich interaction surface.

## Mapping the Developer Workflow to Claude Code
Let’s talk more on that workflow piece because I remember very vividly when I was first using Claude for programming. I would be on the website, type in a prompt, and paste in a file. Then all of a sudden I’d get a code output, and I’d have to copy it, find my file on my local computer, paste it in, and make the edits myself manually.

Now, we’ve taken out that piece of the developer workflow and gone straight from the prompt to the direct edits on the file. Can you tell me a little bit more about how we’re thinking about future iterations of the evolution of this dev workflow and this dev loop within Claude Code?

I think the way I’ve been thinking about it — and a lot of folks on the team talk about it — is that the developer workflow initially started as writing lines of code. You’re at a word level or a function level, and that’s where you spend your time.

The first really big AI development for coding was “tab to autocomplete,” but that’s still at the line level. With this first generation of Claude Code, we’re up-leveling it to full file changes or full task changes — almost at a PR (Pull Request) level. And of course, there are some things that Claude Code can do better or worse, but we’re trying to kind of move in that direction.

As time goes on and our models get more intelligent and our capabilities get stronger, I think we’ll move from specific tasks to a project level. You’ll be orchestrating multiple Claudes from multiple places to accomplish something. Tasks will be longer-running, and Claude will be a lot more autonomous. We might eventually outgrow the CLI, but you’ll be operating at a higher order of workflow than ever before as a developer.

## Prompting in the Terminal
Related to the agent front, we recently put out subagents as a product. Can you talk more about that and how this paradigm of slash commands, subagent workflows, and other features tie together?

Part of the reason the terminal is so great is because it has a built-in architecture for how you control the interface. You have your flags that you put in as you launch Claude, and then you have your commands within the terminal. We introduced a very new paradigm, which is prompting in the terminal.

There was so much debate. I even have a doc with Boris, from November or December of last year, where we argued that we couldn’t put outlines in the terminal because resizing the window would break everything. Every experience I’ve ever had with designing for CLIs before made me avoid outlines like the plague.

What is an outline in this context? It’s like the outline around the input box that you see right now. You tend to avoid those in CLI design because when you resize, everything is just characters and spaces, so it doesn’t align properly. But Boris had a vision, and I was wrong. We found a great library and interface, and the team worked really hard to make it usable. The combination of separating your prompting (how you talk to the model) from your tools (slash commands) and your settings (settings.json and CLAUDE.md) creates an architecture that powers Claude Code. It also mirrors the regular architecture of software development, like a README file. It pairs beautifully.

## How We Design New Features
How do we actually design new things, like the outline box or the visual aesthetics? Do we have design principles we follow? Just walk me through that process.

Everyone is an inventor here at Anthropic and on the Claude Code team. For the most part, it’s a small team of one or two engineers coming up with ideas and prototyping them. Then we rigorously test them internally. Everyone at Anthropic uses Claude Code, and that’s where we get a lot of our feedback. We typically do a cycle of UX polish toward the end when we feel we have the right shape for the technology.

Subagents moved really fast from an idea to a landing. There was a little bit of design polish on how we show a subagent and differentiate it from Claude, and how you set it up. It was the same thing with MCP (Model Context Protocol).

The big principles I hold dearly are:

First, a CLI is a very limited interface, so we need to keep it as clean as possible. We don’t want to flood it with information; we want to keep it focused on the task.
Second, we really want the model to shine. Part of why the CLI is so nice is that it’s the thinnest wrapper possible around our models. You get access to the raw capability of Claude, and that’s what makes Claude Code so powerful.
## Favorite Design Elements
Do you have any favorite little design polishes or touches in Claude Code?

I definitely do. I really like the ASCII “reticulating” and “thinking” animations. I think those are such a great point of personality for Claude. I also really like the different modes — how we’ve outlined if you’re in thinking mode, planning mode, or auto-accept mode. It’s a very rich way to communicate complex information in a way that people can understand.

I agree. I love the personality touches as well. Programming can sometimes feel like a robotic process dealing with lines of code and characters, but using Claude Code elicits a different emotion than just typing line after line in an IDE.

I think there’s actually a lot of really rich things you can do in terminal, and sometimes it’s even about pulling us back. We don’t need to over-design this; we can just let the model take care of it, because it is really great at it.

## Tips and Tricks for Designers Using Claude Code

(brainstorming with Claude, scoping product development timelines, and making design tweaks after new product releases, collaborating on Scoping and Timelines)

I’m curious to hear some of your tips and best practices for using Claude Code, especially as a designer and not a traditional technical person. How do you best use Claude Code day-to-day?

I love this question. It’s something I’m personally very passionate about. I am a product designer, and I will be the first to admit that I should not be writing any code; any code I write is definitely “vibe coded” and should be reviewed. But Claude Code and these coding agents have unlocked a new “skill tree” for non-technical folks. Before, I might need to request time from a software engineer or let some things go if they weren’t a high priority. I now have a new set to reach into to do it myself. Now I can do it myself.

Designers talk about two big axes:

The first is that the cost of an idea is zero; you can prototype very quickly.
But the more exciting unlock for me is that I can actually push code to production. I can make the changes I want in the live codebase itself.
Common use cases I do daily include brainstorming with Claude Code when designing a new feature. I’ll ask, “What are the most common use cases here? What are the edge states I should think about? How would you design this, maybe?” I also ask Claude Code to help me scope designs. I’ll drag and drop an image of a design and ask, “How long do you think it’ll take to make this?” Claude will give me estimates so I can understand the timeline, and friendly debate with the engineers on how long it’ll actually take to build something, and we can reach a good compromise.

The last big one for me is about the “final 2%.” When you’re launching a new product, you often don’t really get to do that last bit of design polish you always want to do. That’s no longer true. Now, I can go in there once the engineers are done — either the day before launch or even a few days after — and clean up all those things that were labeled as “P2” (lower priority) that I really wanted to see in the product.

## The Rise of the Design Engineer
Wow, that’s amazing. It’s exciting to hear about this convergence of the designer and the engineer into a “design engineer,” in a sense, because of what Claude Code allows.

Absolutely. One surprising thing it has done for me is make my partnership with engineers a lot better. There are still many things I honestly can’t do on my own, but even making a first attempt and then chatting with the engineer makes our collaboration a lot stronger. It’s not just giving you a new skill set; it’s helping you collaborate better with your partners, which is a really important part of this whole cycle we’re building.

## Closing
I agree. That’s great. Well, Meaghan, this has been awesome. I really appreciate the conversation.


