# ai-claude-code-talk CLAUDE.md

## 📌 Repository Overview
- **Repo Type**: Public Medium Blog Repository
- **Publication**: AI & ML Human Training/Coaching
- **Topic**: Claude Code Talk & Related Series
- **Purpose**: Central repository for all blog articles, technical assets, and supporting materials

---

## 🚀 Workflow: Adding a New Blog Article

### Prerequisites
Gather these 3 details about the article:
1. **Article Title** (with emojis/formatting if desired)
2. **Blog Series/Context** (e.g., "Claude Code Talk", "Anthropic Developer Talk", "AI Term of the Day")
3. **Medium URL** (full link to published article)

### Step 1: Create Blog Folder
Create a folder with kebab-case name in the repo root:
```
the-future-of-agentic-coding-with-claude-code/
```

### Step 2: Create CLAUDE.md and README.md in Blog Folder
Each blog folder needs **both files**.

Create a `CLAUDE.md` file with YAML frontmatter:

```yaml
---
topic: "Article Title Here (quote if it contains colons)"
context: "Blog Series Name"
reference: "https://medium.com/..."
---

Optional description/notes about the article (follows the pattern of other CLAUDE.md files)
```

Create a `README.md` file following this pattern:

```markdown
# Article Title Here

**Source:** Blog Series Name

One-line description of the article.

## Published Article

[Article Title Here](https://medium.com/...)
```

**IMPORTANT GOTCHAS:**
- ⚠️ **Always quote the `topic` value** if it contains colons (`:`) — YAML requires this for special characters
- Keep description short and reference the Medium link
- Follow the pattern from other blog CLAUDE.md files in the repo

### Step 3: Add Entry to README.md
Update `README.md` at the repo root. Add entry at the **top** of `## 📚 Article Index (Newest First)`:

```markdown
* **[📟 Title Here](https://medium.com/...)** — Brief one-line description. [[Technical Assets](./folder-name)]
```

**Format Pattern:**
- Include emoji from title (if present)
- Include full title with link
- Brief description (one sentence)
- Link to local assets folder

### Step 4: Commit & Push
```bash
git add README.md the-folder-name/CLAUDE.md
git commit -m "Add new blog: [Blog Title]

- Add article to README index (newest first)
- Create CLAUDE.md for [folder-name]
- Document article metadata

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
git push origin main
```

---

## 📋 Repository Structure

```
ai-claude-code-talk/
├── README.md                          # Chronological index of all articles
├── CLAUDE.md                          # This file - process documentation
├── folder-1/
│   ├── CLAUDE.md                      # Article metadata (YAML + description)
│   ├── transcript.md                  # Article transcript/assets
│   └── ...other assets
├── folder-2/
│   ├── CLAUDE.md
│   ├── ...
```

---

## ✅ Checklist for Next Time

- [ ] Gather title, context, and Medium URL
- [ ] Create blog folder (kebab-case name)
- [ ] Create CLAUDE.md with YAML frontmatter
  - [ ] **Topic value is quoted** (if it has colons or special characters)
- [ ] Create README.md with title, source, description, and article link
  - [ ] Context field matches blog series name
  - [ ] Reference is full Medium URL
- [ ] Update README.md (add at top of list)
- [ ] Verify YAML syntax is valid (no "mapping values" errors)
- [ ] Commit with both files staged
- [ ] Push to origin main

---

## 🔗 Related Files
- Each blog folder's `CLAUDE.md` contains metadata
- `README.md` is the public-facing index
- `transcript.md` typically contains article transcripts or main content
