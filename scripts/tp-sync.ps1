# Two-way sync between this local clone and GitHub (ThinkProfits/Claude-Code).
# Run by the Windows task "tp-repo-sync" every 30 minutes; safe to run by hand.
#   1. pull --rebase --autostash  (bring in teammates' / cloud-session changes)
#   2. if anything changed locally: add -A, commit "auto-sync <time>", push
# On a rebase conflict it aborts, logs, and leaves your files alone. Fix it manually
# (or ask Claude), then the next run carries on.

$repo = Split-Path -Parent $PSScriptRoot
$logDir = Join-Path $PSScriptRoot 'logs'
New-Item -ItemType Directory -Force $logDir | Out-Null
$log = Join-Path $logDir 'tp-sync.log'
function Log($msg) { "{0}  {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg | Add-Content $log -Encoding utf8 }

Set-Location $repo

# Keep the log small.
if ((Test-Path $log) -and (Get-Item $log).Length -gt 1MB) { Get-Content $log -Tail 500 | Set-Content $log -Encoding utf8 }

# Don't run on top of an unfinished rebase/merge.
if ((Test-Path '.git\rebase-merge') -or (Test-Path '.git\rebase-apply') -or (Test-Path '.git\MERGE_HEAD')) {
    Log 'SKIPPED: a rebase/merge is in progress. Resolve it first.'
    exit 1
}

git pull --rebase --autostash --quiet 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    git rebase --abort 2>&1 | Out-Null
    Log 'CONFLICT on pull. Rebase aborted, nothing pushed. Resolve manually.'
    exit 1
}

if (git status --porcelain) {
    git add -A
    git commit --quiet -m ("auto-sync {0} ({1})" -f (Get-Date -Format 'yyyy-MM-dd HH:mm'), $env:COMPUTERNAME) 2>&1 | Out-Null
}

# Push anything not yet on GitHub (new auto-sync commit or commits Claude made).
$ahead = git rev-list --count '@{u}..HEAD' 2>$null
if ($ahead -and [int]$ahead -gt 0) {
    git push --quiet 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) { Log "PUSH FAILED ($ahead commit(s) waiting)."; exit 1 }
    Log "pushed $ahead commit(s)"
}
exit 0
