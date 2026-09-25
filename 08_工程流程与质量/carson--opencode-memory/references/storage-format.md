# OpenCode Storage Format

Reference for the local data layout. The skill uses direct `sqlite3` and focused
file queries against this structure. OpenCode has migrated from mostly
file-based JSON to SQLite-backed durable state; keep legacy paths in mind, but
treat SQLite as the current source of truth.

## Data Root

```
~/.local/share/opencode/
|-- opencode.db              # Main SQLite database for stable/latest/prod
|-- opencode-<channel>.db    # Channel-specific DB for non-stable builds
|-- opencode.db-shm          # SQLite shared memory
|-- opencode.db-wal          # SQLite write-ahead log
|-- plans/                   # Saved plan markdown files
|   `-- <timestamp>-<slug>.md
|-- snapshot/                # Internal file snapshots per project
|   `-- <project-id>/
|-- storage/
|   |-- session_diff/        # Changed-file diffs per session
|   |   `-- <session-id>.json
|   |-- session/             # Legacy session JSON from older/file-storage builds
|   |-- message/             # Legacy message JSON from older/file-storage builds
|   |-- part/                # Legacy part JSON from older/file-storage builds
|   `-- project/             # Legacy project registry
|-- tool-output/             # Cached tool outputs
|-- log/                     # Application logs
`-- bin/                     # Bundled binaries (pyright, etc.)
```

Database selection rules:

- Prefer `opencode db path` when the CLI is on `PATH`; it returns the active database file.
- `$OPENCODE_DB` wins. Absolute paths are used as-is; relative filenames are resolved inside the data root.
- Stable/latest/prod builds normally use `opencode.db`.
- Other channels can use `opencode-<channel>.db` unless channel DBs are disabled.

## State Root

```
~/.local/state/opencode/
├── prompt-history.jsonl  # Raw prompt history (one JSON object per line)
└── frecency.jsonl        # File access frequency/recency data
```

## Config Root

```
~/.config/opencode/
|-- opencode.json         # Main config
|-- tui.json              # TUI config
|-- agent/ or agents/     # Custom agent definitions
|-- command/ or commands/ # Custom command definitions
|-- skill/ or skills/     # Global skills
`-- plugin/ or plugins/   # Local plugins
```

## Project Link

Each git repo tracked by OpenCode has a file:

```
<repo>/.git/opencode      # Contains the project ID hash
```

This ID maps to the `project` table in the database.

## SQLite Schema

### project

| Column       | Type    | Notes                          |
|-------------|---------|--------------------------------|
| id          | TEXT PK | SHA hash of worktree path      |
| worktree    | TEXT    | Absolute path to git worktree  |
| vcs         | TEXT    | VCS type if detected           |
| name        | TEXT    | May be NULL; derive from path  |
| icon_url    | TEXT    | Project icon metadata          |
| icon_color  | TEXT    | Project icon metadata          |
| time_created| INTEGER | Unix milliseconds              |
| time_updated| INTEGER | Unix milliseconds              |
| time_initialized | INTEGER | Project init time in milliseconds |
| sandboxes   | TEXT    | JSON array                     |
| commands    | TEXT    | JSON object                    |
| icon_url_override | TEXT | User override                |

### project_directory

| Column       | Type    | Notes                                  |
|-------------|---------|----------------------------------------|
| project_id  | TEXT PK | References project.id                  |
| directory   | TEXT PK | Absolute directory path                |
| type        | TEXT    | main, root, git_worktree, or NULL      |
| strategy    | TEXT    | Project resolution strategy metadata   |
| time_created| INTEGER | Unix milliseconds                      |

### session

| Column        | Type    | Notes                                    |
|--------------|---------|------------------------------------------|
| id           | TEXT PK | e.g. `ses_xxx`                           |
| project_id   | TEXT FK | References project.id                    |
| workspace_id | TEXT    | Optional workspace reference             |
| parent_id    | TEXT    | NULL for main sessions, set for subagent |
| slug         | TEXT    | URL/display slug                          |
| directory    | TEXT    | Working directory for the session        |
| path         | TEXT    | Optional path metadata                    |
| title        | TEXT    | Auto-generated or user-set title         |
| version      | TEXT    | OpenCode version                          |
| share_url    | TEXT    | Share URL if shared                       |
| summary_additions | INTEGER | File diff summary count             |
| summary_deletions | INTEGER | File diff summary count             |
| summary_files | INTEGER | File diff summary count                |
| summary_diffs | TEXT   | JSON diff summary                         |
| revert       | TEXT    | JSON revert state                         |
| permission   | TEXT    | JSON permission snapshot                  |
| agent        | TEXT    | Active agent                              |
| model        | TEXT    | JSON model/provider info                  |
| cost         | REAL    | Accumulated cost                          |
| tokens_input | INTEGER | Accumulated token count                   |
| tokens_output | INTEGER | Accumulated token count                 |
| tokens_reasoning | INTEGER | Accumulated token count              |
| tokens_cache_read | INTEGER | Accumulated token count             |
| tokens_cache_write | INTEGER | Accumulated token count            |
| metadata     | TEXT    | JSON metadata                             |
| time_created | INTEGER | Unix milliseconds                        |
| time_updated | INTEGER | Unix milliseconds                        |
| time_compacting | INTEGER | Compaction time in milliseconds        |
| time_archived | INTEGER | Archive time in milliseconds            |

### message

| Column        | Type    | Notes                                |
|--------------|---------|--------------------------------------|
| id           | TEXT PK | e.g. `msg_xxx`                       |
| session_id   | TEXT FK | References session.id                |
| data         | TEXT    | JSON blob with role, model, metadata |
| time_created | INTEGER | Unix milliseconds                    |
| time_updated | INTEGER | Unix milliseconds                    |

Key JSON fields in `message.data`:
- `$.role` — `"user"` or `"assistant"`
- Common assistant metadata: `$.modelID`, `$.providerID`, `$.tokens`, `$.cost`, `$.finish`, `$.summary`, `$.error`

### part

| Column        | Type    | Notes                                    |
|--------------|---------|------------------------------------------|
| id           | TEXT PK | e.g. `prt_xxx`                           |
| message_id   | TEXT FK | References message.id                    |
| session_id   | TEXT FK | References session.id                    |
| data         | TEXT    | JSON blob with type, text, tool payloads |
| time_created | INTEGER | Unix milliseconds                        |
| time_updated | INTEGER | Unix milliseconds                        |

Common `part.data` shapes:

| Type          | Common keys                                  | Notes |
|---------------|----------------------------------------------|-------|
| text          | type, text, time, metadata, synthetic         | Chat text |
| tool          | type, tool, callID, state, metadata           | Tool calls/results; arguments and outputs may be sensitive |
| reasoning     | type, text, time, metadata                    | Model reasoning summaries/content |
| patch         | type, hash, files                             | Changed-file patch metadata |
| file          | type, filename, mime, url, source, synthetic  | Attached or referenced files |
| step-start    | type, snapshot                                | Assistant step boundary |
| step-finish   | type, cost, tokens, reason, snapshot          | Assistant step boundary |
| compaction    | type, auto, overflow, tail_start_id           | Compaction marker |
| subtask       | type, agent, model, command, description, prompt | Subagent invocation |

### todo

| Column        | Type    | Notes                              |
|--------------|---------|------------------------------------|
| session_id   | TEXT PK | References session.id              |
| content      | TEXT    | Todo item text                     |
| status       | TEXT    | pending, in_progress, completed... |
| priority     | TEXT    | high, medium, low                  |
| position     | INTEGER PK | Position within session         |
| time_created | INTEGER | Unix milliseconds                  |
| time_updated | INTEGER | Unix milliseconds                  |

### session_message

V2 projection rows for session-level messages/events.

| Column        | Type    | Notes                              |
|--------------|---------|------------------------------------|
| id           | TEXT PK | Session message ID                 |
| session_id   | TEXT FK | References session.id              |
| type         | TEXT    | e.g. agent-switched, model-switched |
| seq          | INTEGER | Sequence inside session            |
| data         | TEXT    | JSON payload                       |
| time_created | INTEGER | Unix milliseconds                  |
| time_updated | INTEGER | Unix milliseconds                  |

### session_input

Durable prompt-admission inbox. Normal conversation recall should use
`message`/`part`; this table is useful for debugging pending or replayed inputs.

| Column        | Type    | Notes                              |
|--------------|---------|------------------------------------|
| id           | TEXT PK | Input/session message ID           |
| session_id   | TEXT FK | References session.id              |
| prompt       | TEXT    | JSON prompt payload                 |
| delivery     | TEXT    | Delivery mode                       |
| admitted_seq | INTEGER | Admission sequence                  |
| promoted_seq | INTEGER | Set when promoted into history      |
| time_created | INTEGER | Unix milliseconds                   |

### session_context_epoch

Tracks system-context snapshots for V2 execution.

| Column        | Type    | Notes                         |
|--------------|---------|-------------------------------|
| session_id   | TEXT PK | References session.id         |
| baseline     | TEXT    | Baseline identifier           |
| snapshot     | TEXT    | JSON context snapshot         |
| baseline_seq | INTEGER | Sequence for the baseline     |

### event and event_sequence

Internal event store. Useful for OpenCode debugging, usually unnecessary for
memory recall.

| Table          | Key columns                    |
|----------------|--------------------------------|
| event_sequence | aggregate_id, seq, owner_id    |
| event          | id, aggregate_id, seq, type, data |

### sensitive/internal tables

Avoid `account`, `account_state`, `control_account`, and `credential` unless the
user explicitly asks. These relate to provider/auth state and are not needed for
conversation memory.

## Useful Raw Queries

### Count main sessions
```sql
SELECT COUNT(*) FROM session WHERE parent_id IS NULL;
```

### List current tables
```sql
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;
```

### User messages with text
```sql
SELECT
  s.id AS session_id,
  COALESCE(s.title, 'untitled') AS session_title,
  m.id AS message_id,
  m.time_created AS timestamp,
  json_extract(p.data, '$.text') AS text
FROM session s
JOIN message m ON m.session_id = s.id
JOIN part p ON p.message_id = m.id
WHERE s.parent_id IS NULL
  AND json_extract(m.data, '$.role') = 'user'
  AND json_extract(p.data, '$.type') = 'text'
ORDER BY m.time_created DESC;
```

### Part type counts for a session
```sql
SELECT json_extract(data, '$.type') AS part_type, COUNT(*) AS count
FROM part
WHERE session_id = 'SESSION_ID_HERE'
GROUP BY part_type
ORDER BY count DESC;
```

### Tool usage counts for a session
```sql
SELECT json_extract(data, '$.tool') AS tool, COUNT(*) AS count
FROM part
WHERE session_id = 'SESSION_ID_HERE'
  AND json_extract(data, '$.type') = 'tool'
GROUP BY tool
ORDER BY count DESC;
```

### Session diffs
```
~/.local/share/opencode/storage/session_diff/<session-id>.json
```
Contains arrays of file paths changed during the session.
