# GitHub PR Operations

All operations use the `gh` CLI. Parameters like `OWNER` and `REPO` come from the remote detection step in the main skill.

> **Prerequisite**: Verify `gh` is installed and authenticated by running `gh auth status`. If not authenticated, inform the user and stop.

## Find PR for Current Branch

```bash
gh pr view --json number,title,state,url
```

This auto-detects the PR for the current branch. If no PR exists, it returns an error.

Alternatively, list PRs and filter:
```bash
gh pr list --head <branch-name> --json number,title,state,url
```

Store the PR `number` for subsequent operations.

## Create PR

```bash
gh pr create --title "<title>" --body "<body>" --base main
```

- `--title`: PR title (from plan feature name or user input)
- `--body`: PR body (summary of changes, link to plan file)
- `--base`: target branch (`main` unless user specifies otherwise)

The source branch is the current branch.

## Update PR

```bash
gh pr edit <number> --title "<new-title>" --body "<new-body>"
```

Only include the flags for fields that need updating.

## Read Comments

General PR comments:
```bash
gh pr view <number> --comments --json comments
```

Review comments (inline code comments):
```bash
gh api repos/{OWNER}/{REPO}/pulls/<number>/comments --jq '.[] | {id, path, line, body, user: .user.login, created_at: .created_at}'
```

Review threads (to see reply chains):
```bash
gh api repos/{OWNER}/{REPO}/pulls/<number>/reviews --jq '.[] | {id, state, body, user: .user.login}'
```

Present comments grouped by:
- General vs inline
- File path and line number for inline comments
- Thread/conversation grouping where possible

## Post General Comment

```bash
gh pr comment <number> --body "<comment-text>"
```

## Post Inline Comment (Code Review)

Inline comments on GitHub require submitting a pull request review. Use a single-comment review:

```bash
gh api repos/{OWNER}/{REPO}/pulls/<number>/reviews \
  --method POST \
  --field body="" \
  --field event="COMMENT" \
  --field 'comments=[{"path":"<file-path>","line":<line-number>,"body":"<comment-text>"}]'
```

For multiple inline comments in one review:
```bash
gh api repos/{OWNER}/{REPO}/pulls/<number>/reviews \
  --method POST \
  --field body="<overall-review-summary>" \
  --field event="COMMENT" \
  --field 'comments=[{"path":"file1.py","line":10,"body":"Issue 1"},{"path":"file2.py","line":25,"body":"Issue 2"}]'
```

## Reply to a Comment

Reply to a review comment by its comment ID:
```bash
gh api repos/{OWNER}/{REPO}/pulls/<number>/comments/<comment-id>/replies \
  --method POST \
  --field body="<reply-text>"
```

## Resolve a Conversation

GitHub uses GraphQL to resolve/unresolve review threads. First, find the thread node ID:

```bash
gh api graphql -f query='
  query {
    repository(owner: "{OWNER}", name: "{REPO}") {
      pullRequest(number: <number>) {
        reviewThreads(first: 100) {
          nodes {
            id
            isResolved
            comments(first: 1) {
              nodes { body path }
            }
          }
        }
      }
    }
  }
'
```

Then resolve the thread by its node ID:
```bash
gh api graphql -f query='
  mutation {
    resolveReviewThread(input: {threadId: "<thread-node-id>"}) {
      thread { isResolved }
    }
  }
'
```

## Check PR Status

```bash
gh pr view <number> --json state,mergeable,reviewDecision,statusCheckRollup,url
```

For CI check details:
```bash
gh pr checks <number>
```
