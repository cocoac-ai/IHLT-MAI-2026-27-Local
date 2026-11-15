# TextServer (FreeLing) in the labs

Decision of 2026-11-10: no more TextServer queries. The service has a daily demo quota per user and service: HTTP 401 with `[TS-126] Maximum daily demo usage for this user and service reached.` (the `entities` service stopped after 48 queries on 2026-11-05). The code stays in the notebooks, switched off; the cached answers are used where they exist.

| Lab | Service | Switch | Cache (`common/`) | State |
|---|---|---|---|---|
| Lab02 | `tokenizer` | `RUN_TEXTSERVER = False` | `textserver_tokenizer.json`, 50 of 338 sentences | code without results; outputs and text not updated |
| Lab03 | `morpho` | `RUN_TEXTSERVER = False` | `textserver_morpho.json`, never created | code without results; outputs and text not updated |
| Lab06 | `senses` (UKB) | — | `ukb_senses.json`, 338 sentences, complete | the only complete cache; gives the FreeLing pipeline and UKB |
| Lab07 | `entities` | `USE_ENTITIES_SERVICE = False` | `entities.json`, never created | FreeLing NEs taken from `ukb_senses.json` instead |

In `ukb_senses.json` the `NP` tags already give the NE class: `NP00SP0` person, `NP00G00` location, `NP00O00` organization, `NP00V00` other. This matched the 48 `entities` answers (9 NEs), which were not saved.

Notes:

- `common/textserver.py` is the original client from the course, with only `timeout=60` added (a request once hung forever).
- Parallel queries get HTTP 503; query one sentence at a time.
- `common/credentials.json` holds the user and password and is ignored by git.
