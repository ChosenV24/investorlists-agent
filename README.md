# InvestorLists

The InvestorLists agent for startup founders raising capital. It works in Claude (chat, Cowork and Claude Code) with the InvestorLists database of person-checked US startup investors: VCs, corporate VCs, family offices, syndicates and accelerators, with their decision-makers, verified contacts and latest news.

## What it does

- **Raise profile.** Reads your website, deck and LinkedIn profile URL in the conversation and drafts a short profile of your company and your round. You correct it, and only the version you approve is saved.
- **Investor shortlists.** Builds a pool of relevant firms from the whole database, then the five to aim for first, with a sourced reason for each firm.
- **Investor briefs.** One to five firms: what they back, latest news, portfolio and possible conflicts, decision-makers, and meeting prep.
- **Path to connect.** One firm at a time: who can introduce you, and the direct paths (verified work emails, LinkedIn profiles, the firm's own submission form).
- **Investor messages.** Your pitch message, cold emails, LinkedIn messages, intro requests, follow-ups and replies, written for you. An email goes out only when you say yes to that email.
- **Pipeline memory.** Where every investor stands, what is due, and what changed in the database for the firms on your lists.

## How to start

1. Add the InvestorLists plugin from the Claude directory.
2. In a new conversation, type: **Hi InvestorLists, let's get started.**
3. Sign in to InvestorLists with the code emailed to you and approve the connection. A new email address gets a free account.

The agent asks for your website, a deck and your LinkedIn profile URL, drafts your raise profile, and offers one first step.

## Example prompts

- "Hi InvestorLists, let's get started."
- "Find seed investors for our B2B fintech round, New York first."
- "Research the top three firms on my shortlist."
- "How do I reach the partner at the first firm?"
- "Write the cold email to that partner."
- "What's due this week?"

## What is inside

| Part | Purpose |
|---|---|
| `.mcp.json` | Connects one remote server: the InvestorLists MCP server at https://investorlists.vc/mcp. Sign-in is OAuth on investorlists.vc; the plugin holds no keys, tokens or secrets. |
| `skills/investorlists-agent` | The front door: onboarding on the first conversation, then where you stand and one next step. Routes to the five skills below. |
| `skills/il-shortlist` | Investor Shortlist: the pool of relevant firms, then batches of five with a sourced reason for each. |
| `skills/il-brief` | Investor Brief: record, latest news, portfolio and conflicts, hooks for a first message, meeting prep. |
| `skills/il-path-to-connect` | Path to Connect: warm paths and direct paths to one firm, with a recommended first move. |
| `skills/il-messages` | Investor Messages: your message set and the messages for one investor and path. |
| `skills/il-pipeline` | Raise Pipeline: the agent's memory, read from your notes. Includes `scripts/parse_notes.py`. |

## What it connects to

One server only: https://investorlists.vc/mcp, operated by InvestorLists.vc (Chosen V. Inc.). The plugin declares no other server, downloads nothing and installs no packages.

## Data handling

**Sent to InvestorLists** (the MCP server above):

- Your sign-in email, used for the OAuth sign-in on investorlists.vc.
- The searches you run (filters and the short description of your company a search matches on) and the ids of the firms you open or unlock.
- What you choose to save: lists of firms, one-line notes per firm (status, next step, due date, chosen path), and workspace notes (your approved raise profile, your message set, your connectors, your preferences, and a daily count of emails sent). You can see, edit and delete them in your portal at investorlists.vc.

**Never sent to InvestorLists:** your deck or website text, the content of your mailbox or calendar, investor replies, and your conversations with Claude.

**Done in your own Claude session**, with tools you already have there:

- Reading the website, deck and LinkedIn profile URL you paste or attach.
- Web searches and visits to investment firms' own websites, for briefs, portfolio checks and paths. Every finding is shown with its date and link. The agent never opens LinkedIn; it gives you links to click.
- Your mailbox and calendar, only if you connected them in Claude and only when you say yes to a specific scan or message. Emails are sent from your own mailbox only on a yes for each email, at most 15 a day.
- Saving pages to an `InvestorLists/` folder, only where your client can write files (Cowork, Claude Code).
- The Pipeline skill can run `scripts/parse_notes.py` (Python 3, standard library only) on your notes to build a status board. It reads and writes local files only and makes no network calls.

Nothing else is sent, fetched or run by this plugin. The agent never creates scheduled tasks or reminders.

Privacy policy: https://investorlists.vc/terms-of-service-and-privacy-policy#privacy

## Free account and full access

- **Free account:** the 10 investors that fit you best, previews of matching firms with the details locked, and 10 firms unlocked in full for good (every decision-maker with name, position, verified work email and LinkedIn profile).
- **Full access:** every skill above, full records for every firm, saved lists, notes, the pipeline, and exports.

Plan details: https://investorlists.vc/ai#plans

## How it behaves

- It offers one next step at a time. Nothing is written, sent, scanned or saved unless you asked for it or said yes.
- Every fact names its source: the database record, a dated news item, or the firm's own website. Blank beats a guess.
- It asks before acting and shows every draft before saving or sending it.

## Support

Email office@investorlists.vc. With your consent, the agent can email a short support report from your own mailbox to that address. Documentation: https://investorlists.vc/ai

Terms of Service: https://investorlists.vc/terms-of-service-and-privacy-policy#terms

## License

Proprietary. Copyright 2026 Chosen V. Inc. All rights reserved. See [LICENSE](LICENSE).
