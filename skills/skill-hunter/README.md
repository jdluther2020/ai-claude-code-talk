# Skill Hunter — Discover the Skills Ecosystem

A comprehensive tool for discovering, extracting, and analyzing Claude SKILL.md files across GitHub.

## Install

```bash
npx skills add jdluther2020/ai-claude-code-talk skill-hunter
```

## What It Does

**Skill Hunter** automates finding and analyzing skill documentation across GitHub:

- **Discover** — Find 270+ SKILL.md files across 193+ repositories
- **Extract** — Get complete, analyzed skill documentation
- **Analyze** — Understand ecosystem patterns and best practices
- **Learn** — See how professional skills are structured
- **Build** — Get insights for creating your own skills

## Use Cases

### 1. Find Examples
Find well-documented skills in your domain to learn from:
> "Show me code review skills and how they're structured"

### 2. Understand Best Practices
Learn what makes high-quality skill documentation:
> "What patterns do top-tier Anthropic skills follow?"

### 3. Analyze Trends
See how the skill ecosystem is evolving:
> "What's trending in skill design right now?"

### 4. Get Started Building
Get a learning path for creating your own skills:
> "I want to build a skill. What should I know?"

### 5. Reference Official Standards
Compare community skills against official implementations:
> "How do official Anthropic skills compare to community ones?"

## What You'll Learn

After using Skill Hunter, you'll understand:

- **Naming conventions** — What naming style is trending (SKILL.md vs skill.md)
- **Quality standards** — What makes excellent skill documentation
- **File size sweet spot** — How long great skills typically are (5-15 KB)
- **Structure patterns** — What sections successful skills include
- **Ecosystem health** — Growth trends and maturity level

## Key Statistics

From analyzing 270+ discovered skills:

- 45% use uppercase `SKILL.md`
- 35% use lowercase `skill.md`
- 28% reach excellent quality (80+/100)
- 63% include code examples
- 193+ unique repositories hosting skills
- Growing ecosystem with emerging standards

## Data Included

This skill comes with:

- **100+ extracted SKILL.md files** — Real examples from the ecosystem
- **270 discovered skills metadata** — Searchable, analyzable index
- **Quality rankings** — Assessment of documentation excellence
- **Pattern analysis** — What works and why
- **Implementation code** — Python script for running your own discovery

## How to Use

### Step 1: Ask Skill Hunter for Guidance
```
"I want to build a skill for X. Show me relevant examples and patterns."
```

Skill Hunter will:
1. Search the ecosystem for similar skills
2. Extract and analyze examples
3. Explain what makes them effective
4. Provide learning progression

### Step 2: Study the Examples
Review the extracted SKILL.md files to understand:
- How frontmatter is structured
- What sections are included
- How examples are formatted
- What makes documentation clear

### Step 3: Learn the Patterns
Understand:
- Common naming conventions
- Standard section organization
- Best practices for clarity
- Quality indicators

### Step 4: Build Your Own
Create your skill with confidence, knowing:
- What's expected (from official examples)
- What works (from production community skills)
- What to avoid (from quality analysis)
- Where to publish (skills.sh ecosystem)

## Technical Details

**Language:** Python 3.6+
**Dependencies:** requests, python-dotenv
**Data Source:** GitHub API (official, not scraping)
**Rate Limits:** ~60/hour without auth, 5,000/hour with GITHUB_TOKEN

### Required Setup

For best results, set a GitHub token:

```bash
export GITHUB_TOKEN=your_github_token_here
```

This increases rate limits and improves reliability.

## Output Examples

Skill Hunter provides:

**Discovery results** — JSON file with 270+ skills and metadata
**Extracted files** — 100+ complete SKILL.md files to study
**Quality analysis** — Rankings and explanations
**Best practices** — Patterns identified across ecosystem
**Learning paths** — Recommended examples in progression order

## Blog Series

Explore deeper insights in the accompanying blog series:

- **Post 1:** How I Built a Skill
- **Post 2:** What the Data Shows
- **Post 3:** How I Automated It
- **Post 4:** Skills Worth Highlighting
- **Post 5:** Getting Started with Skills

[Read on Medium](https://medium.com/@jdluther2020)

## Source Code

Full implementation available:

```
├── discovery_phase_1_v3.py       # Main discovery tool
├── extracted_skills/             # 100 sample SKILL.md files
├── GITHUB_SEARCH_RESULTS_V3.json # All 270 discovered skills
├── SKILL_QUALITY_RANKINGS.md     # Quality analysis
└── COMPREHENSIVE_SKILL_DIRECTORY.md # Full index
```

## Tips for Best Results

1. **Start with a specific goal** — "I want to build a skill for..."
2. **Ask for examples** — "Show me well-made skills in this domain"
3. **Learn the patterns** — "What makes this one well-designed?"
4. **Study multiple examples** — Understand the range of approaches
5. **Reference best practices** — Use insights when building

## FAQ

**Q: Is this real-time data?**
A: No, this is a point-in-time snapshot. The ecosystem updates constantly, but patterns remain stable.

**Q: Does it search private repositories?**
A: No, only public GitHub repositories are searched via the public API.

**Q: Can I extend this?**
A: Yes! The code is open source. You can modify the discovery script or add analysis.

**Q: What's the learning curve?**
A: Minimal. Just ask for examples in your domain, and Skill Hunter provides guidance.

## Resources

- [Agent Skills Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Official Skills](https://github.com/anthropics/skills)
- [Community Skills (obra/superpowers)](https://github.com/obra/superpowers)

---

**Ready to explore?**
Ask Skill Hunter: *"Show me well-designed skills in my domain"*

**Want to build skills?**
Ask: *"What do I need to know to build a production-quality skill?"*

**Curious about the ecosystem?**
Ask: *"What trends are emerging in skill design?"*
