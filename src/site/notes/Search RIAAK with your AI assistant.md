---
{"dg-publish":true,"permalink":"/search-riaak-with-your-ai-assistant/","tags":["AI"],"created":"2026-09-30T23:48:03.283+01:00","updated":"2026-09-30T23:51:37.602+01:00","dg-note-properties":{"Note Type":"RIAAK Admin","tags":["AI"]}}
---

You can get your own AI assistant such as Claude or ChatGPT to search RIAAK for you. Ask it a research question in plain English, and it will search RIAAK, answer using only what RIAAK contains, and give you a link to every source so you can read the originals.

It works through an **agent skill**: a short set of instructions your assistant follows. The skill is free, and it's published in Vegan Hacktivists' [collection of AI skills for the animal protection movement](https://github.com/veganhacktivists/animal-protection-ai-skills), where every skill is vetted by a person. I made this skill myself, so you know you can trust it!

# What you can ask
- "What does the research say about how consumers feel about cultivated meat?"
- "Find me studies on farmed fish welfare at slaughter."
- "Is there evidence that animal cruelty messages work better than health messages?"

A good answer is a few sentences, a link to the RIAAK page after each claim, and a list of the sources it used. If RIAAK doesn't cover your question, your assistant should say so rather than guess.

# How to add the skill
The skill is called `search-riaak`. The easiest way to add it is to ask your assistant: "Install the search-riaak skill from github.com/veganhacktivists/animal-protection-ai-skills". Alternatively:

**Claude (claude.ai and the desktop app)**
Download the `search-riaak` zip from the [releases page](https://github.com/veganhacktivists/animal-protection-ai-skills/releases), then upload it in Settings, under Capabilities, then Skills. Claude's code tool needs to be allowed to reach the internet for the search to work. If it fails, check that setting.

**OpenAI Codex**
Copy the [search-riaak folder](https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/search-riaak) into `~/.agents/skills/`.

**Gemini CLI**
```
gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/search-riaak
```

**GitHub Copilot**
```
gh skill install veganhacktivists/animal-protection-ai-skills search-riaak
```

**Any other assistant**
See the [install instructions for the whole collection](https://github.com/veganhacktivists/animal-protection-ai-skills#installing-a-skill).

# Good to know
- It only searches what's published on RIAAK, so a gap in RIAAK is a gap in the answers.
- Many of the study summaries in RIAAK were written with help from AI (the [[RIAAK Home page\|homepage]] explains how). Check the original source before you rely on a number.
- Your assistant needs to be able to make web requests. Assistants that can only browse web pages usually can't run it. If yours can't, use the search box on this site instead.
- It's free, and you don't need an account.
