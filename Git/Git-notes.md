# Git & GitHub — A Complete, Practical Guide 

> This is a thorough, hands-on Markdown lesson you can copy into your notes. It starts with **why version control exists**, traces the **history from SCCS→RCS→CVS→SVN→Git**, explains **how Git works under the hood**, demystifies **GitHub’s role & architecture**, and then walks you through **branching, workflows, and a realistic pull-request demo** against a popular Python repo. Commands and screenshots focus on **Windows (Git Bash / PowerShell)**.

---

## 1) Why do we need Version Control at all?

**Before VCS** (Version Control Systems), teams shared code by emailing ZIPs or copying folders like `final`, `final2`, `final_really_final`, overwriting each other’s changes, and losing track of who changed what/when/why. Merge conflicts were manual. Rollbacks were painful. Audit trails were nonexistent.

**Version control** fixes that by tracking every change (who/what/why/when), enabling branching/merging, and letting many people work safely in parallel. See Atlassian’s primers for the core motivations and benefits. ([Atlassian][1])

---

## 2) A (very) short history of Version Control

* **SCCS (1970s)** and **RCS (1980s)** — file-level deltas, locks, single-file focus.
* **CVS (1990s)** — multi-file, client/server; branching/merge was possible but often painful.
* **Subversion/SVN (2000s)** — centralized VCS with atomic commits and better branching than CVS, but still **one central server** was the source of truth. ([Atlassian][2], [Atlassian Support][3])

### The distributed turn (mid-2000s)

Large open-source projects (notably the Linux kernel) needed extreme performance, offline work, and fast branching/merging. Distributed VCS (DVCS) like **Git** let **every developer have a full local copy of history** (fast operations, offline commits), then sync over the network. ([Atlassian][4])

---

## 3) Git: how it started (and became the standard)

In **April 2005**, after the Linux kernel community lost access to the proprietary BitKeeper tool, **Linus Torvalds** wrote Git with goals: **speed**, **data integrity**, and **distributed workflows**. The very first Git commit is dated April 7, 2005, and the project has been developed openly (GPLv2) ever since. Juníō Hamano soon became the long-time maintainer. ([The GitHub Blog][5], [LWN.net][6])

Today Git is the de-facto standard VCS. ([Wikipedia][7])

---

## 4) GitHub: the rise of a collaboration platform

**Git** is the tool; **GitHub** is the social/collaboration platform built on top of Git (hosting repos, pull requests, code review, CI, issues, wikis, etc.). GitHub launched in **2008**, later **acquired by Microsoft in 2018**. ([The New Yorker][8])

GitHub changed the developer workflow via **forks + pull requests** and a friendly UI for Git. (See early write-ups on how it “tamed” open-source collaboration.) ([WIRED][9])

---

## 5) Open source, Git, and GitHub—how they fit

* **Open source** is about **licensing & community** (permissions to use, modify, share).
* **Git** is the **DVCS engine**.
* **GitHub** is the **networked hub** where Git repos live, with social & automation features (issues, PRs, Actions, pages, packages, etc.).

*(For choosing licenses, GitHub’s ChooseALicense.com is a good practical reference.)*

---

## 6) Architectures of Version Control

### Centralized VCS (CVCS)

```
[ Dev ] <-> [ CENTRAL SERVER ] <-> [ Dev ]
```

* One central history; must be online to commit; server is a bottleneck & SPOF.
* Examples: **SVN**, **Perforce**. ([Atlassian Support][3])

### Distributed VCS (DVCS)

```
[ Dev Repo ] ↔ [ Dev Repo ] ↔ [ Shared Remote (GitHub) ] ↔ [ Dev Repo ]
```

* Every clone has **full history**; commit/rebase/log/diff are **local** & fast; push/pull syncs.
* Example: **Git**. ([Atlassian][4])

---

## 7) How **Git** works under the hood (just enough to be dangerous)

### Snapshots, not diffs (conceptually)

Most earlier tools stored *delta-of-delta* chains; **Git stores snapshots**, plus efficient compression behind the scenes. Think: **each commit points to a tree** (folder snapshot), which points to **blobs** (file contents) and sub-trees. ([Git SCM][10], [schacon.github.io][11])

**Core objects:**

* **blob** — file content
* **tree** — directory listing (names → blobs/trees)
* **commit** — metadata + root tree + parents
* **tag** — named pointer (often a release tag)
  (Stored under `.git/objects/` keyed by content hash.) ([Git SCM][10])

### Packfiles & delta compression

Over time, Git runs housekeeping (`git gc`) to pack many objects into **packfiles** with **delta compression** to save space/bandwidth. ([Git SCM][12])

### Diffs and merge algorithms

Git’s default diff is **Myers’ O(ND)** algorithm; alternate modes include **patience** and **histogram** to produce cleaner diffs in some cases. ([XMail Server][13], [Git SCM][14])

---

## 8) How **GitHub** uses Git in the backend (architecture overview)

At massive scale, GitHub stores repos on fleets of file servers and **replicates multiple copies** across datacenters via **Spokes** (formerly “DGit”). This **application-level replication** improves durability, availability, and cross-DC performance. ([The GitHub Blog][15], [InfoQ][16])

*(Takeaway: GitHub is not “a single bare repo on one disk”. It’s a distributed storage system optimized for serving Git traffic at planetary scale.)*

---

## 9) Branches, `main`, and the “master→main” shift

A **branch** is just a movable pointer (name) to a commit. The default branch is your repo’s “trunk” (historically **`master`**, now often **`main`**). In **Git 2.28 (Jul 2020)**, Git introduced `init.defaultBranch` so users/orgs could choose the initial branch name; GitHub made the **default for new repos `main` (Oct 2020)**. ([The GitHub Blog][17])

> Note: Git itself never had a “slave” branch concept. “Master/slave” terminology existed elsewhere in tech; the industry moved toward more inclusive language. ([WIRED][18])

---

## 10) Common branching strategies (and when to use them)

* **GitHub Flow** — Simple: branch off `main`, open a PR, review/CI, merge, deploy. Great for continuous delivery and web services. ([GitHub Docs][19])
* **Trunk-Based Development (TBD)** — Everyone commits frequently to `main` (short-lived feature branches at most). Requires strong CI & feature flags; maximizes flow. ([trunkbaseddevelopment.com][20])
* **Release Flow (Microsoft)** — TBD + timed release branches; hotfixes cherry-picked to release lines. Good for sprint-based releases or products needing sustained servicing. ([Microsoft for Developers][21])
* **Git Flow** — Historic model with long-lived `develop`, `release/*`, `hotfix/*`. Heavy for many teams; used when you need parallel release trains and strong isolation.

> Practical guidance: Prefer **GitHub Flow** (or **TBD**) for fast teams; use **Release Flow** if you ship on a sprint cadence and support multiple live versions.

---

## 11) End-to-end workflow concepts (quick mental model)

```
# Clone vs. branch vs. commit vs. push vs. PR

git clone <repo-url>         # Copy the whole repo + history locally
git switch -c feature/x      # Create a branch ("workspace") for a change
# ... edit files ...
git add . && git commit -m   # Save a snapshot locally (no server required)
git push -u origin feature/x # Publish your branch to the remote (GitHub)
# Open Pull Request on GitHub: feature/x -> main
# Review + CI + merge button
```

---

## 12) Hands-on demo: contribute to a well-known Python repo (fork → branch → PR)

We’ll use a docs-only change (safe for beginners). **Pick a popular Python repo** that accepts doc fixes (e.g., `pypa/sampleproject` or another library you use). Steps:

### A) One-time Windows setup

```powershell
# Install Git (if needed)
winget install --id Git.Git -e

# Configure your identity once (used in commit metadata)
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

### B) Fork & clone

1. On GitHub, **Fork** the repo to your account.
2. **Clone your fork** (note: you clone *repos*, not individual branches):

```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
```

3. Point `upstream` at the original project so you can sync later:

```bash
git remote add upstream https://github.com/<original-owner>/<repo>.git
git fetch --all --prune
```

### C) Create a topic branch and make a small change

```bash
git switch -c docs/fix-typo-readme    # or: git checkout -b docs/fix-typo-readme
# Edit README.md or /docs/*.md (fix a typo, add a clarifying sentence)
git add README.md
git commit -m "docs: fix typo and clarify install step"
```

### D) Push your branch & open a Pull Request

```bash
git push -u origin docs/fix-typo-readme
```

* Go to GitHub → your fork → **Compare & pull request**.
* Target: `original-owner/<repo>:main`.
* Fill **PR title** and **description** (why the change, links, screenshot if relevant).

### E) Code review cycle & CI

* Respond to reviewer comments, push updates:

```bash
# keep your topic branch up to date with upstream/main (if needed)
git fetch upstream
git rebase upstream/main
# resolve conflicts if prompted, then:
git push --force-with-lease
```

* When **checks pass** and **reviews approve**, maintainers **merge** your PR.

### F) Clean up locally

```bash
git switch main
git pull --ff-only upstream main
git branch -D docs/fix-typo-readme
git push origin :docs/fix-typo-readme
```

---

## 13) Branch protection & gated reviews on GitHub

Maintainers often protect `main` (or `release/*`) so changes can’t merge unless gates pass:

* **Required status checks** (CI must be green)
* **Required reviewers** (N approvals, or **CODEOWNERS** must approve)
* **Linear history**, **signed commits**, etc.
  See GitHub docs on **protected branches** and **CODEOWNERS**. ([GitHub Docs][22])

---

## 14) Git command cookbook (Windows-friendly)

> Use **Git Bash** (installed with Git) or PowerShell. Commands are identical.

### 14.1 Clone a repo (your own or someone else’s public repo)

```bash
git clone https://github.com/<owner>/<repo>.git
cd <repo>
```

### 14.2 Create & switch to a new branch

```bash
git switch -c feature/add-hello      # create + switch
# ...edit files...
git status                            # see what changed
git add .                             # stage all
git commit -m "feat: add hello module"
```

### 14.3 Push branch to GitHub and set upstream

```bash
git push -u origin feature/add-hello
```

### 14.4 Create **another** branch off `main`, commit there too

```bash
git switch main
git pull --ff-only origin main       # or upstream/main if you track upstream
git switch -c bugfix/typo
# edit, then:
git add .
git commit -m "fix: README typo"
git push -u origin bugfix/typo
```

### 14.5 Raise a Pull Request (PR)

* On GitHub, open PR from your branch → `main`. (Or use GitHub CLI `gh pr create` if installed.)

### 14.6 Keep your topic branch fresh (rebasing)

```bash
git fetch upstream
git rebase upstream/main
# resolve conflicts → `git add <file>` for each → continue:
git rebase --continue
git push --force-with-lease
```

### 14.7 Merge PR (maintainers) & delete branch

* Click **Merge** (squash/merge/rebase) after checks pass.
* Delete branch locally + remote:

```bash
git branch -D feature/add-hello
git push origin :feature/add-hello
```

---

## 15) Branching strategies: quick compare

| Strategy            | Default branch model                            | When it shines                                    | Caveats                                                                  |
| ------------------- | ----------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------ |
| **GitHub Flow**     | `main` + short-lived feature branches           | SaaS, frequent deploys, small cohesive teams      | Requires strong CI & feature flags for safe rollout. ([GitHub Docs][19]) |
| **Trunk-Based Dev** | Mostly `main` with tiny branches                | Max flow, minimal merge pain; scales with fast CI | Needs discipline + robust tests/flags. ([trunkbaseddevelopment.com][20]) |
| **Release Flow**    | `main` + periodic `release/*` branches          | Sprint releases, servicing older versions         | Requires cherry-pick hygiene. ([Microsoft for Developers][21])           |
| **Git Flow**        | Long-lived `develop` + `release/*` + `hotfix/*` | Multi-version products, heavy QA staging          | Heavier; slower flow for many modern teams.                              |

---

## 16) Internals (a bit deeper, for the curious)

* **Content-addressable store**: objects are addressed by hash (historically SHA-1) in `.git/objects/`. **Trees** link names→(blobs|trees); **commits** link parents→tree. ([Git SCM][10])
* **Packfiles**: `git gc` / `git repack` coalesce many objects into `.pack` files, using **delta compression** to reduce duplication; index files speed random access. ([Git SCM][12])
* **Diff algorithms**: default **Myers**; alternatives include **patience** and **histogram** for more readable diffs in certain layouts. Try: `git diff --patience`. ([Git SCM][14])

---

## 17) Practical tips & gotchas

* **Clone the repo**, not a branch; then **checkout** the branch you need.
* **One logical change per PR** → faster review.
* Prefer **rebasing** your topic branch on `main` (clean history) and use **`--force-with-lease`** (safer than `--force`).
* Keep PRs **small** (200–400 LOC is a sweet spot for review).
* Enable **branch protection** and **required status checks** before merging. ([GitHub Docs][22])

---

## 18) A minimal Python example you can really submit

1. Add a tiny utility file:

```bash
mkdir -p examples
printf "def greet(name: str) -> str:\n    return f\"Hello, {name}!\"\n" > examples/hello.py
git add examples/hello.py
git commit -m "feat: add hello utility example"
git push -u origin feature/add-hello
```

2. Include a short doc snippet or test.
3. Open PR with context: **what**, **why**, **how tested**.
4. Respond to review feedback; iterate until green; **merge**.

*(Look for repos that label issues “good first issue” or “documentation.”)*

---

## 19) Governance & quality gates on GitHub

* **CODEOWNERS** require reviews from domain owners before merge. ([GitHub Docs][23])
* **Required status checks** (e.g., unit tests, lint, type checks) must pass to merge. ([GitHub Docs][22])
* **Branch protection rules** can prohibit force-pushes, require linear history, and enforce signed commits. ([GitHub Docs][24])

---

## 20) Appendix — Glossary

* **Repository (repo)** — All project content + history.
* **Clone** — Full local copy of a repo.
* **Fork** — Your copy of someone else’s repo on GitHub (lets you open PRs).
* **Branch** — Named pointer to a commit (a line of development).
* **Commit** — A snapshot + message + metadata.
* **PR (Pull Request)** — A proposed change from one branch to another, with review & checks.

---

## References & further deep-dives

* **What is version control / DVCS vs CVCS (Atlassian)**. ([Atlassian][1], [Atlassian Support][3])
* **What is Git (Atlassian)**; history and benefits. ([Atlassian][25])
* **Git internals** — Pro Git: Objects & Packfiles; manpages. ([Git SCM][10])
* **Diff algorithms** — Myers paper; Git diff options. ([XMail Server][13], [Git SCM][14])
* **Git origin & dates** — GitHub 20-year Q\&A; LWN on BitKeeper → Git. ([The GitHub Blog][5], [LWN.net][6])
* **GitHub default branch = `main`** — Git 2.28 `init.defaultBranch`; GitHub change in Oct 2020. ([The GitHub Blog][17])
* **GitHub backend** — DGit/Spokes posts; cross-DC replication. ([The GitHub Blog][15], [InfoQ][16])
* **Branching strategies** — GitHub Flow; Trunk-Based; Release Flow. ([GitHub Docs][19], [trunkbaseddevelopment.com][20], [Microsoft for Developers][21])
* **Protected branches & CODEOWNERS** — GitHub Docs. ([GitHub Docs][22])
* **Context on “master→main” wording change** — industry discussion. ([WIRED][18])

---

## Bonus: quick ASCII diagrams you can paste into slides

### Centralized vs Distributed

```
CVCS (SVN)                         DVCS (Git)
-----------                        -----------
   Dev A  -->                      Dev A (full repo)
              \                    /
               > [Central Repo] <— 
              /                    \ 
   Dev B  -->                      Dev B (full repo)
```

### Git object graph (simplified)

```
[commit C] --parent--> [commit B] --parent--> [commit A]
    |                        |                   
   tree --------------------/                    
    |                                             
  (files as blobs, subtrees...)                   
```

### GitHub Flow (happy path)

```
main  o---o---o-----------------o (merge)
             \                 /
feature/x     o---o---o---o---o
```

---

# References

[1]: https://www.atlassian.com/git/tutorials/what-is-version-control?utm_source=chatgpt.com "What is version control | Atlassian Git Tutorial"
[2]: https://www.atlassian.com/blog/software-teams/version-control-centralized-dvcs?utm_source=chatgpt.com "What is version control: centralized vs. DVCS"
[3]: https://support.atlassian.com/bitbucket-cloud/docs/types-of-version-control/?utm_source=chatgpt.com "Types of version control | Bitbucket Cloud"
[4]: https://www.atlassian.com/git?utm_source=chatgpt.com "Learn Git - Tutorials, Workflows and Commands"
[5]: https://github.blog/open-source/git/git-turns-20-a-qa-with-linus-torvalds/?utm_source=chatgpt.com "Git turns 20: A Q&A with Linus Torvalds"
[6]: https://lwn.net/Articles/134404/?utm_source=chatgpt.com "Linus Torvalds' BitKeeper blunder (InfoWorld)"
[7]: https://en.wikipedia.org/wiki/Git?utm_source=chatgpt.com "Git"
[8]: https://www.newyorker.com/tech/annals-of-technology/the-software-that-builds-software?utm_source=chatgpt.com "The Software That Builds Software"
[9]: https://www.wired.com/2012/02/github-2?utm_source=chatgpt.com "Lord of the Files: How GitHub Tamed Free Software (And More)"
[10]: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects?utm_source=chatgpt.com "10.2 Git Internals - Git Objects"
[11]: https://schacon.github.io/gitbook/1_the_git_object_model.html?utm_source=chatgpt.com "Git Book - The Git Object Model - schacon.github.io"
[12]: https://git-scm.com/book/en/v2/Git-Internals-Packfiles?utm_source=chatgpt.com "Git - Packfiles"
[13]: https://www.xmailserver.org/diff2.pdf?utm_source=chatgpt.com "An O(ND) Difference Algorithm and Its Variations ∗"
[14]: https://git-scm.com/docs/git-diff?utm_source=chatgpt.com "Git - git-diff Documentation"
[15]: https://github.blog/engineering/architecture-optimization/introducing-dgit/?utm_source=chatgpt.com "Introducing DGit"
[16]: https://www.infoq.com/news/2017/10/github-spokes-replication/?utm_source=chatgpt.com "How GitHub Uses Spokes for Cross Data-Center Replication"
[17]: https://github.blog/open-source/git/highlights-from-git-2-28/?utm_source=chatgpt.com "Highlights from Git 2.28"
[18]: https://www.wired.com/story/tech-confronts-use-labels-master-slave?utm_source=chatgpt.com "Tech Confronts Its Use of the Labels 'Master' and 'Slave'"
[19]: https://docs.github.com/en/get-started/using-github/github-flow?utm_source=chatgpt.com "GitHub flow"
[20]: https://trunkbaseddevelopment.com/?utm_source=chatgpt.com "Trunk Based Development"
[21]: https://devblogs.microsoft.com/devops/release-flow-how-we-do-branching-on-the-vsts-team/?utm_source=chatgpt.com "Release Flow: How We Do Branching on the VSTS Team"
[22]: https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com "About protected branches"
[23]: https://docs.github.com/articles/about-code-owners?utm_source=chatgpt.com "About code owners"
[24]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule?utm_source=chatgpt.com "Managing a branch protection rule"
[25]: https://www.atlassian.com/git/tutorials/what-is-git?utm_source=chatgpt.com "What is Git | Atlassian Git Tutorial"
