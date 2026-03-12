# Azure DevOps PR Operations

All operations use MCP tools. Parameters like `org`, `project`, and `repo` come from the remote detection step in the main skill.

## Find PR for Current Branch

Use `mcp_azure_devops_repo_list_pull_requests_by_repo_or_project` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `status`: `active`

Filter results to find the PR whose `sourceRefName` matches `refs/heads/<current-branch>`.

Store the `pullRequestId` for subsequent operations.

## Create PR

Use `mcp_azure_devops_repo_create_pull_request` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `title`: PR title (from plan feature name or user input)
- `description`: PR body (summary of changes, link to plan file)
- `sourceBranch`: current branch name (without `refs/heads/` prefix — the tool handles it)
- `targetBranch`: `main` (or ask user if different)

Returns the created PR with its `pullRequestId`.

## Update PR

Use `mcp_azure_devops_repo_update_pull_request` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `pullRequestId`: the PR ID
- Fields to update: `title`, `description`, `status`, etc.

## Read Threads and Comments

1. List all threads on the PR using `mcp_azure_devops_repo_list_pull_request_threads` with:
   - `projectName`: `PROJECT`
   - `repositoryName`: `REPO`
   - `pullRequestId`: the PR ID

2. For each thread, read its comments using `mcp_azure_devops_repo_list_pull_request_thread_comments` with:
   - `projectName`: `PROJECT`
   - `repositoryName`: `REPO`
   - `pullRequestId`: the PR ID
   - `threadId`: from the thread listing

3. Present threads grouped by status (Active, Resolved, etc.) and indicate:
   - Whether they are general or file-specific (inline)
   - The file path and line number for inline comments
   - The comment content and author

## Post General Comment

Use `mcp_azure_devops_repo_create_pull_request_thread` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `pullRequestId`: the PR ID
- `comment`: the comment text
- Do NOT include `filePath` or line parameters (this makes it a general comment)

## Post Inline Comment

Use `mcp_azure_devops_repo_create_pull_request_thread` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `pullRequestId`: the PR ID
- `comment`: the comment text
- `filePath`: path to the file (relative to repo root, prefixed with `/`)
- `startLine` and `endLine`: line range for the comment

## Reply to a Thread

Use `mcp_azure_devops_repo_reply_to_comment` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `pullRequestId`: the PR ID
- `threadId`: the thread to reply to
- `comment`: the reply text

## Resolve a Thread

Use `mcp_azure_devops_repo_resolve_comment` with:
- `projectName`: `PROJECT`
- `repositoryName`: `REPO`
- `pullRequestId`: the PR ID
- `threadId`: the thread to resolve

## Check PR Status

Use `mcp_azure_devops_repo_get_pull_request_by_id` with:
- `projectName`: `PROJECT`
- `pullRequestId`: the PR ID

Review the returned status, merge status, and reviewer votes.
