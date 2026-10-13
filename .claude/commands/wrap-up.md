---
description: End of session. Update STATE, append the notebook entry, add decision records and RESULTS rows, offer to commit
---

Close the session by doing these steps in order. Keep each piece tight.

1. **STATE.md.** Update these sections:
   - Last updated: today's date, `git rev-parse --short HEAD` and the branch.
   - Current focus.
   - Next session: numbered, concrete steps with commands.
   - What changed this session.
   - Open decisions.
   - Open threads.
   - Where things are.

   Remove anything stale or finished. Keep the file at or under about 150 lines (`wc -l STATE.md`). Detail belongs in the notebook, not here.
2. **Notebook.** Append an entry to this month's `lab/notebook/YYYY-MM.md`. If the file doesn't exist, create it with a `# Notebook — YYYY-MM` header. Use the template in `lab/notebook/README.md`, include dead ends, and never edit earlier entries.
3. **Decision record.** If a hard-to-reverse choice was made, write `lab/decisions/NNNN-title.md` with the next free number. Examples of such choices:
   - deleting legacy files
   - changing the stack or adding templating
   - the branch policy
   - changing URLs
   - dropping a page

   Add the record to the index in `lab/decisions/README.md` and link it from the notebook entry as `[[NNNN-title]]`. If it changes an older record, update that record's Status and text as well.
4. **RESULTS.md.** Add a row for each change that went live this session, meaning it was pushed to `main`. The row has the date, the result, the SHA, the producer (files or script), the artifact path (live URL path) and the notebook link. If a change is committed but not pushed yet, put it under Open threads in STATE.md instead.
5. **ROADMAP.md and DATA.md.** Tick the items that are finished. If a content source changed (a new CV, a new photo, an added publication), update its DATA.md row.
6. **Commit.** Show `git status` and propose one concise commit message, then ask before committing. Commit only if the user agrees, and only on the branch CLAUDE.md names. Never push. Give the user the push command and say what it will change on the live site.
