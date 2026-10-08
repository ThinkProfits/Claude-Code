# Setting up a new Windows device

How to get this repo working on another PC so it stays in sync with GitHub the same way it does on the main workstation: Claude pulls the latest when it opens, pushes when it finishes a task, and a background job commits and pushes any leftover changes once a day.

Takes about 10 minutes. You only do this once per device.

## 1. Install the basics

- **Git for Windows**: https://git-scm.com/download/win (keep the defaults; it includes Git Credential Manager).
- **Claude Code**: the desktop app or the CLI, signed in with your ThinkProfits account.
- **GitHub access**: your GitHub account needs to be a member of the ThinkProfits organization.

## 2. Tell Git who you are

Open PowerShell and run (use your own name and work email):

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@thinkprofits.com"
```

## 3. Clone the repo

Pick a folder that suits the machine. `C:\ThinkProfits` is a good default.

```powershell
mkdir C:\ThinkProfits
cd C:\ThinkProfits
git clone https://github.com/ThinkProfits/Claude-Code
cd Claude-Code
```

The first time Git talks to GitHub, a browser window opens asking you to sign in. Do that once and Git Credential Manager remembers it, so the background sync can push without asking.

## 4. Open Claude Code in the repo

Either run `claude` from the `Claude-Code` folder, or open that folder in the desktop app.

Nothing else to configure here. The repo already ships with:

- `.claude/settings.json`: a SessionStart hook that runs `git pull` every time Claude Code opens. If Claude asks you to approve the hook, say yes.
- `CLAUDE.md`: tells Claude to commit and push when it finishes a task.
- Team skills and shared `memory/`, which load automatically.

## 5. Turn on the daily background sync

This catches anything Claude didn't push itself (files you edited by hand, a session closed mid-task and so on). It runs `scripts/tp-sync.ps1`, which pulls, commits any changes as `auto-sync <date> (<PC name>)`, and pushes.

Run this once in PowerShell **from inside the `Claude-Code` folder** (no admin needed):

```powershell
$script = Join-Path (Get-Location) 'scripts\tp-sync.ps1'
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""
$trigger = New-ScheduledTaskTrigger -Daily -At 9am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName 'tp-repo-sync' -Action $action -Trigger $trigger -Settings $settings -Description 'Daily ThinkProfits repo sync'
```

It's scheduled for 9am, but `-StartWhenAvailable` means that if the PC is off at 9am, it runs as soon as you turn it on. In practice: once a day, the first time the PC is up.

Want it more often? Swap the trigger line for one that repeats every 30 minutes (what the main workstation uses):

```powershell
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 30)
```

## 6. Test it

```powershell
Start-ScheduledTask tp-repo-sync
Get-Content .\scripts\logs\tp-sync.log -Tail 5
git log -1 --oneline
```

No log lines and no new commit just means there was nothing to sync. That's fine.

## Troubleshooting

| What you see | What to do |
|---|---|
| Log says `CONFLICT on pull` | Someone else changed the same file. The script backed off and touched nothing. Run `git status` in the folder, or ask Claude to sort it out. |
| Log says `PUSH FAILED` | Usually credentials. Run `git push` by hand once and sign in when the browser opens. |
| Log says `SKIPPED: a rebase/merge is in progress` | Finish or abort the rebase (`git rebase --abort`), then the next run carries on. |
| Want to stop the sync | `Unregister-ScheduledTask tp-repo-sync -Confirm:$false` |

## Before you push anything

Never commit secrets: API keys, OAuth `client_secret*.json`, `token.json`, `google-ads.yaml`. `.gitignore` blocks the usual names, so check before forcing anything past it.

## Local MCP servers (optional)

The gsc, google-ads-keywords and gbp-audit servers need their own setup and credentials on each machine. See the table in [README.md](README.md#local-mcp-servers).
