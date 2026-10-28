# ThinkProfits Claude Code setup: guided walkthrough

**How to use this file (any new teammate):** open Claude Code (desktop app, Code tab), drag this file into the chat, and type:

> Walk me through this setup file, one step at a time.

Claude does the work and stops at each checkpoint to confirm with you. You only step in to sign in to things or paste a key Francis gives you.

---

## Instructions for Claude

You are setting up a new ThinkProfits teammate's Claude Code on a Windows PC so it matches the agency's standard setup: shared repo, shared skills, connectors, and a knowledge-graph memory that recalls related notes automatically.

**Rules for this walkthrough:**

1. Go one step at a time. At the start of each step, explain in 1-2 plain sentences what it is and why it helps. Then do it, check it worked, and ask the user to confirm before moving on.
2. Check first, then act. If something is already installed or done, say so and skip it.
3. Never ask the user to paste passwords into chat. For sign-ins, tell them what to click and let them do it. API keys for MCP connectors are the one exception: the user pastes them into a command or config file you write, and you never repeat a key back in chat.
4. Never commit secrets to the repo (API keys, `client_secret*.json`, `token.json`, `google-ads.yaml`).
5. Use Canadian English, and keep it friendly. The user isn't a developer, so skip jargon.
6. Before you start, ask the user two things: their full name, and the folder where they want the repo (default `C:\ThinkProfits`). In the steps below, `<REPO>` means `<that folder>\Claude-Code`.
7. If a command's syntax has changed from what's written here, check `--help` and adapt. Don't guess.
8. At the end, give a short summary of what was set up and anything that was skipped.

---

### Step 1: Install the basics

Check for and install whatever is missing:
- **Git for Windows** (`git --version`). If it's missing, have the user install it from https://git-scm.com/download/win with the default options.
- **Python 3.10 or newer** (`python --version`). If it's missing, have the user install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH".
- Set the Git identity: `git config --global user.name "<Full Name>"` and `git config --global user.email "<their>@thinkprofits.com"`.

**Checkpoint:** all three versions print, and the Git identity is set.

### Step 2: Clone the ThinkProfits repo

The repo is the team's shared brain. It holds client files, team memory, skills and standing rules.

1. Make sure the user's GitHub account is in the ThinkProfits organization. If not, stop and tell them to ask Francis.
2. Clone it: `git clone https://github.com/ThinkProfits/Claude-Code` into the chosen folder. A browser sign-in to GitHub pops up the first time; the user completes it.
3. Read `<REPO>\SETUP-NEW-DEVICE.md` and follow any remaining steps there, including the daily background sync job.
4. Tell the user: from now on, start every ThinkProfits session by opening the `<REPO>` folder in Claude Code. The repo's CLAUDE.md, skills, hooks and team memory then load automatically.

**Checkpoint:** `<REPO>\CLAUDE.md` and `<REPO>\.claude\skills\` exist. List the skills to the user in one line each.

### Step 3: Cloud connectors

These let Claude read and act in the agency's tools. The user connects them at **claude.ai → Settings → Connectors**, signing in to each:
- **Semrush** (SEO data; the agency's tool of record)
- **Gmail** and **Google Drive** (includes Docs and Sheets)
- **Slack**
- **Make.com**
- **Canva**

**Checkpoint:** the user confirms each one shows as connected.

### Step 4: Agency MCP servers that need keys

Ask the user which of these Francis has given them keys for, and add only those. All are HTTP servers, added at user scope:

| Name | URL | Header |
|---|---|---|
| `brightlocal` | `https://mcp.brightlocal.com/mcp` | `x-api-key: <key>` |
| `wp-spiedr` | `https://www.spiedr.com/wp-json/easy-mcp-ai/v1/mcp` | `Authorization: <value from Francis>` |
| `wp-mujo` | `https://www.mujo.com/wp-json/easy-mcp-ai/v1/mcp` | same pattern |
| `wp-vision` | `https://visionplumbingandheating.com/wp-json/easy-mcp-ai/v1/mcp` | same pattern |
| `wp-jamie-davis` | `https://www.jamiedavistowing.com/wp-json/easy-mcp-ai/v1/mcp` | same pattern |
| `wp-mysaskfarm` | `https://mysaskfarm.com/wp-json/easy-mcp-ai/v1/mcp` | same pattern |

Example (check `claude mcp add --help` for current syntax):

```
claude mcp add --scope user --transport http wp-spiedr https://www.spiedr.com/wp-json/easy-mcp-ai/v1/mcp --header "Authorization: <value>"
```

Skip `gsc`, `ga4`, `google-ads-keywords` and `gbp-audit` for now. They're local servers in `<REPO>\mcp-servers\` that need their own Google authentication. Set them up later only if the user needs live Search Console, Analytics or Keyword Planner data.

**Checkpoint:** `claude mcp list` shows each added server as connected. The user restarts Claude Code if needed.

### Step 5: Plugins

Plugins add ready-made skills. Check `claude plugin --help` (or the app's plugin menu) for how to install. Recommended:
- **superpowers** (`claude-plugins-official` marketplace): makes Claude plan, debug and verify properly instead of rushing.
- **document-skills** (`anthropics/skills` marketplace): Word, Excel, PowerPoint and PDF files.
- **make-skills** (`integromat/make-skills` marketplace): Make.com scenario building.
- **canva** (`claude-plugins-official`).
- Optional: **token-optimizer** (`alexgreensh/token-optimizer`) shows token use in the status line.

**Checkpoint:** the plugins show as enabled.

### Step 6: Graphify knowledge-graph memory + recall hook

This is the "connected notes" memory. **Graphify** turns the team's notes and client cards into a graph: every client, person, tool and fact is a node, and the links between them are edges. A small hook script then runs on every prompt. It matches the user's words to the graph and quietly hands Claude the 1-4 most related notes. It uses no AI, takes under a second, and stays silent when nothing matches. So when the user asks "what's next for John Sadler?", Claude already has John Sadler's status card in front of it.

**6a. Install Graphify in its own folder** (keep it outside the repo):

```
mkdir C:\Automation\graphify
cd C:\Automation\graphify
python -m venv .venv
.venv\Scripts\python.exe -m pip install graphifyy
```

Then run `.venv\Scripts\graphify.exe install` (check `--help` if that differs). This adds the `/graphify` skill to Claude. If the skill's setup step points at a different Python, edit it to use `C:\Automation\graphify\.venv\Scripts\python.exe`, so it never installs packages into the system Python.

**6b. Save the two scripts below** into `C:\Automation\graphify\`. In each one, replace `C:/ThinkProfits/Claude-Code` with the real `<REPO>` path (forward slashes).

`build_cards_graph.py` builds a graph from every client's `CARD.md` (status, next step, blockers, who's involved). It's free and uses no AI:

```python
"""Build graphs/tp-cards from <REPO>/clients/*/CARD.md.

Deterministic, no AI: cards share a fixed format (title, bold Status/Next step/
Blocked/Last activity lines, a "Where things live" table), so each card is
parsed into nodes directly. Shared values (Slack channels, people) become
shared nodes, which is what links clients to each other.
Run with the graphify venv python. graph_recall.py calls it when a card is newer
than the graph.
"""
import json
import re
from pathlib import Path

ROOT = Path("C:/ThinkProfits/Claude-Code/clients")  # <-- set to <REPO>/clients
OUT = Path(__file__).parent / "graphs" / "tp-cards" / "graphify-out"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:60]


def extract():
    nodes, edges = {}, []

    def node(nid, label, src, ftype="concept"):
        nodes.setdefault(nid, dict(id=nid, label=label, file_type=ftype, source_file=src, source_location=None,
                                   source_url=None, captured_at=None, author=None, contributor=None, _origin="semantic"))

    def edge(a, b, src, rel="references"):
        edges.append(dict(source=a, target=b, relation=rel, confidence="EXTRACTED", confidence_score=1.0,
                          source_file=src, source_location=None, weight=1.0, _origin="semantic"))

    for card in sorted(ROOT.glob("*/CARD.md")):
        src = f"{card.parent.name}/CARD.md"
        text = card.read_text(encoding="utf-8")
        title = re.search(r"^# (.+?)(?::\s*card)?\s*$", text, re.M)
        client = title.group(1).strip() if title else card.parent.name
        cid = slug(card.parent.name)
        node(cid, f"{client} ({card.parent.name}) status card", src, "document")
        for key in ("Status", "Next step", "Blocked on client", "Blocked on", "Last activity"):
            m = re.search(rf"^\*\*{key}:\*\*\s*(.+)$", text, re.M)
            if m:
                nid = f"{cid}_{slug(key)}"
                node(nid, f"{client} {key.lower()}: {m.group(1).strip()[:300]}", src)
                edge(cid, nid, src)
        for row in re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", text, re.M):
            what, where = row
            if what in ("What", "---") or set(what) <= {"-"}:
                continue
            nid = f"{cid}_{slug(what)}"
            node(nid, f"{client} {what}: {where[:200]}", src)
            edge(cid, nid, src)
            for chan in re.findall(r"#[a-z0-9_-]+", where):  # shared Slack channels link clients
                sid = "slack_" + slug(chan)
                node(sid, f"Slack {chan}", src)
                edge(nid, sid, src, "conceptually_related_to")
        for person in ("Andrew", "Francis", "Shawn", "Tina", "Colin", "Britt"):
            if re.search(rf"\b{person}\b", text):
                pid = "person_" + slug(person)
                node(pid, person, src)
                edge(cid, pid, src, "conceptually_related_to")
    return {"nodes": list(nodes.values()), "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0}


def main():
    from graphify.build import build_from_json
    from graphify.cluster import cluster
    from graphify.export import to_json
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / ".graphify_root").write_text(str(ROOT).replace("\\", "/"), encoding="utf-8")
    G = build_from_json(extract(), root=str(ROOT), directed=False)
    graph = OUT / "graph.json"
    graph.unlink(missing_ok=True)  # full rebuild every time; shrink guard would block removed cards
    to_json(G, cluster(G), str(graph))
    print(f"tp-cards: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")


if __name__ == "__main__":
    main()
```

`graph_recall.py` is the hook that runs on every prompt:

```python
"""UserPromptSubmit hook: point Claude at the memory notes related to the prompt.

No AI. Reads every graphs/*/graphify-out/graph.json, matches prompt words
against node labels, walks one hop through the graph, and prints the most
relevant source files as additionalContext. Prints nothing when no match.
"""
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

GRAPHS_DIR = Path(__file__).parent / "graphs"
CARDS_DIR = Path("C:/ThinkProfits/Claude-Code/clients")  # <-- set to <REPO>/clients
MAX_FILES = 4
MAX_SEEDS = 6
MIN_SCORE = 2.5
HUB_DEGREE = 20  # index-style hubs (INDEX.md) bridge everything; don't expand through them
LOG = Path(__file__).parent / "graph_recall.log"

STOP = set("""
a an and are as at be but by can could did do does for from get got had has have how i if in into is it its
just let like make me my need no not now of on or our out please run see should so some that the their them
then there these this to up us use was we what when where which who why will with would yes you your
check go going want start step set setup done next also than ok okay thing things way new one two
ahead sure thanks thank yes yeah both all three four first last good great fine right sounds proceed continue
""".split())


def words(text):
    out = []
    for w in re.findall(r"[a-z0-9][a-z0-9'\-]{2,}", text.lower()):
        if w in STOP:
            continue
        if len(w) > 4 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]  # crude plural fold: questions -> question
        out.append(w)
    return out


def load_graphs():
    for gj in sorted(GRAPHS_DIR.glob("*/graphify-out/graph.json")):
        root_file = gj.parent / ".graphify_root"
        root = Path(root_file.read_text(encoding="utf-8").strip()) if root_file.exists() else gj.parent.parent
        yield json.loads(gj.read_text(encoding="utf-8")), root


def recall(prompt):
    query = set(words(prompt))
    if not query:
        return None
    hits = []
    for g, root in load_graphs():
        nodes = {n["id"]: n for n in g["nodes"]}
        adj = defaultdict(set)
        for e in g.get("links", []):
            if e.get("confidence") == "AMBIGUOUS":
                continue
            adj[e["source"]].add(e["target"])
            adj[e["target"]].add(e["source"])
        toks = {nid: set(words(n.get("label", "") + " " + nid.replace("_", " "))) for nid, n in nodes.items()}
        df = defaultdict(int)
        for ts in toks.values():
            for t in ts:
                df[t] += 1
        n_nodes = max(len(nodes), 1)
        seed = {}
        for nid, ts in toks.items():
            s = sum(math.log(n_nodes / df[t]) for t in query & ts)
            sf = Path(nodes[nid].get("source_file", ""))
            stem = set(words(f"{sf.stem} {sf.parent.name}".replace("-", " ")))  # CARD.md: folder = client
            s += 4.0 * len(query & stem)  # naming a file's own subject (a client name) beats generic words
            if s >= MIN_SCORE:
                seed[nid] = s
        top = sorted(seed.items(), key=lambda kv: -kv[1])[:MAX_SEEDS]
        file_score = defaultdict(float)
        file_labels = defaultdict(list)
        for nid, s in top:
            n = nodes[nid]
            file_score[n["source_file"]] = max(file_score[n["source_file"]], s)  # best match, not a pile of weak ones
            file_labels[n["source_file"]].append(n["label"])
            if len(adj[nid]) > HUB_DEGREE:
                continue
            for nb in adj[nid]:
                m = nodes.get(nb)
                if m and len(adj[nb]) <= HUB_DEGREE:
                    file_score[m["source_file"]] += s * 0.3
        for f, s in file_score.items():
            hits.append((s, str((root / f).resolve()), file_labels.get(f, [])))
    hits.sort(key=lambda h: -h[0])
    hits = [h for h in hits if h[0] >= 0.4 * hits[0][0]][:MAX_FILES] if hits else []
    if not hits:
        return None
    lines = ["[graph recall] Memory notes related to this prompt (read only if relevant):"]
    for _, path, labels in hits:
        lines.append(f"- {path}" + (f"  ({'; '.join(l[:110] for l in labels[:2])})" if labels else "  (linked)"))
    return "\n".join(lines)


def refresh_cards_graph():
    """Rebuild graphs/tp-cards in the background when any CARD.md is newer than it."""
    import subprocess
    graph = GRAPHS_DIR / "tp-cards" / "graphify-out" / "graph.json"
    cards = list(CARDS_DIR.glob("*/CARD.md"))
    if not cards:
        return
    built = graph.stat().st_mtime if graph.exists() else 0
    if max(c.stat().st_mtime for c in cards) > built:
        subprocess.Popen([sys.executable, str(Path(__file__).parent / "build_cards_graph.py")],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         creationflags=getattr(subprocess, "DETACHED_PROCESS", 0))


def main():
    try:
        refresh_cards_graph()
        data = json.loads(sys.stdin.read() or "{}")
        prompt = data.get("prompt", "")
        if "<agent-message" in prompt or "<task-notification" in prompt:
            return  # subagent hand-backs, not the user's own words
        ctx = recall(prompt)
    except Exception as exc:  # never block the prompt
        try:
            LOG.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        except OSError:
            pass
        return
    if ctx:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}}))


if __name__ == "__main__":
    main()
```

**6c. Build the graphs:**
1. Client cards (free, a few seconds): `C:\Automation\graphify\.venv\Scripts\python.exe C:\Automation\graphify\build_cards_graph.py`. It should print a node and edge count.
2. Team memory (uses AI tokens, but the folder is small): make `C:\Automation\graphify\graphs\tp-memory`, `cd` into it (Graphify writes `graphify-out\` into the current folder), and run `/graphify <REPO>\memory`. Keep the output out of the repo.

**6d. Register the hook.** Merge this into the user's `%USERPROFILE%\.claude\settings.json`. Merge, don't overwrite, and keep any existing settings:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "C:\\Automation\\graphify\\.venv\\Scripts\\python.exe",
            "args": ["C:\\Automation\\graphify\\graph_recall.py"],
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**6e. Test it.** Pipe a fake prompt in:

```
echo {"prompt":"what is next for John Sadler"} | C:\Automation\graphify\.venv\Scripts\python.exe C:\Automation\graphify\graph_recall.py
```

It should print JSON that points to `clients\john-sadler\CARD.md`. Then have the user restart Claude Code, ask about a client by name, and confirm a `[graph recall]` note appears in the context.

**6f. Optional: Obsidian.** For a clickable, visual map of the same notes, install Obsidian (https://obsidian.md) and open `<REPO>` as a vault. Each graph also has an interactive `graph.html` in its `graphify-out\` folder that opens in any browser.

**Checkpoint:** the test prints a match, and `graph_recall.log` either doesn't exist or is empty.

### Step 7: Safety settings

Add these deny rules to `%USERPROFILE%\.claude\settings.json` (merge, don't overwrite) so Claude never reads secret files:

```json
"permissions": { "deny": ["Read(.env)", "Read(.env.*)", "Read(.secrets)"] }
```

### Step 8: Habits (explain these to the user, then finish)

- Open `<REPO>` for all ThinkProfits work. Claude pulls the latest from GitHub when it opens and should commit and push when a task is done.
- When Claude learns something durable (a client quirk, an approval, a standing rule), say "save that to team memory". It goes in `memory\` and gets listed in `memory\INDEX.md`.
- After working on a client, update their `clients\<client>\CARD.md` (status, next step, blockers). The card graph rebuilds itself.
- After big memory changes, rebuild the memory graph: `cd C:\Automation\graphify\graphs\tp-memory`, then `/graphify <REPO>\memory --update`.
- Call skills by name when unsure: "use gbp-topic-finder for Mujo", "use agency-blog-writer for SPIEDR".
- Drop new info (notes, exports, briefs) into `<REPO>\Inbox\` and ask Claude to file it.

Finish with a short summary: what's installed, what's connected, what was skipped, and how to test the memory recall.
