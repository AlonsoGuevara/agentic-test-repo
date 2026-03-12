---
name: pr-management
description: "Manage pull requests across Azure DevOps and GitHub repositories. Use when: creating PRs, reading PR comments, posting PR comments, replying to comments, resolving threads, updating PRs, or checking PR status. Detects remote type automatically and uses the correct tooling (Azure DevOps MCP tools or GitHub CLI)."
argument-hint: "Action to perform: create, read-comments, post-comment, reply, resolve, update, status"
---

# PR Management

Cross-platform pull request management skill that detects the repository remote (Azure DevOps or GitHub) and dispatches to the correct tooling.

## When to Use

- "Create a PR for this feature branch"
- "Read PR comments"
- "Post a review comment on the PR"
- "Reply to PR feedback"
- "Resolve a PR comment thread"
- "Update the PR description"
- "Check PR status"

## Consumers

- **Implementer Agent**: Create PRs, push updates, read review feedback, reply to comments.
- **Reviewer Agent**: Read PR threads, post review comments (general and inline), resolve threads.

## Procedure

### 1. Detect Remote Type

Run `git remote -v` and inspect the output:

- **Azure DevOps**: URL contains `dev.azure.com` or `visualstudio.com`
- **GitHub**: URL contains `github.com`

Extract and store:
- `REMOTE_TYPE`: `azdo` or `github`
- `REMOTE_URL`: the full remote URL
- For Azure DevOps: extract `ORG`, `PROJECT`, and `REPO` from the URL pattern `dev.azure.com/{org}/{project}/_git/{repo}` or `{org}.visualstudio.com/{project}/_git/{repo}`
- For GitHub: extract `OWNER` and `REPO` from the URL pattern `github.com/{owner}/{repo}`

If the remote cannot be identified, stop and inform the user.

### 2. Resolve Current Branch

Run `git branch --show-current` to get the current branch name. This is used as the source branch for PR operations.

### 3. Dispatch to Platform

Use the reference for the detected platform:
- Azure DevOps → [Azure DevOps Operations](./references/azure-devops.md)
- GitHub → [GitHub Operations](./references/github.md)

---

## Quick Reference — Operations by Role

| Operation | Implementer | Reviewer | Azure DevOps Tool | GitHub CLI |
|-----------|:-----------:|:--------:|-------------------|------------|
| Create PR | x | | `mcp_azure_devops_repo_create_pull_request` | `gh pr create` |
| Update PR | x | | `mcp_azure_devops_repo_update_pull_request` | `gh pr edit` |
| Find PR for branch | x | x | `mcp_azure_devops_repo_list_pull_requests_by_repo_or_project` | `gh pr list` / `gh pr view` |
| Read threads/comments | x | x | `mcp_azure_devops_repo_list_pull_request_threads` + `list_pull_request_thread_comments` | `gh pr view --comments` |
| Post general comment | | x | `mcp_azure_devops_repo_create_pull_request_thread` | `gh pr comment` |
| Post inline comment | | x | `mcp_azure_devops_repo_create_pull_request_thread` (with filePath + line params) | `gh api` (pull request review) |
| Reply to thread | x | x | `mcp_azure_devops_repo_reply_to_comment` | `gh api` (reply to review comment) |
| Resolve thread | | x | `mcp_azure_devops_repo_resolve_comment` | `gh api` (resolve thread) |
| Check PR status | x | x | `mcp_azure_devops_repo_get_pull_request_by_id` | `gh pr status` / `gh pr checks` |
