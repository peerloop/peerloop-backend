## peerloop-backend
peerloop main backend repository

## Collaboration Rules

1. For every branch (so PR), open a new issue in Linear. Your branch name MUST include the Linear ticket number (ex. `PEE-18`). Follow the below branch naming rule ([Semantic Branch Names](https://gist.github.com/seunggabi/87f8c722d35cd07deb3f649d45a31082)).

Format: `<type>/#<issueNumber>-<alias>`

Example
```
feat/#PEE-18-init-files
^--^ ^-----^
|          |
|          +---> issue's keyword
|
+-------> Type: or feat, chore, docs, fix, refactor, style, or test.
```
More Examples:

* `feat`: (new feature for the user, not a new feature for build script)
* `fix`: (bug fix for the user, not a fix to a build script)
* `docs`: (changes to the documentation)
* `style`: (formatting, missing semi colons, etc; no production code change)
* `refactor`: (refactoring production code, eg. renaming a variable)
* `test`: (adding missing tests, refactoring tests; no production code change)
* `chore`: (updating grunt tasks etc; no production code change)

2. PR name **MUST** include Linear ticket number.

Format: `[<issueNumber>] <PR name>`

Example: `[PEE-81] Add email validation logic`

3. If you update the env file, run `update_env_format.py` to update `.env-format`.

```sh
update_env_format.py -e .env.local
```

4. To apply linter & formatter, run `./lint_format.sh`.

5. Configure `pre-commit` hook.

Reference: [How to setup pre-commit hook](https://www.notion.so/Backend-Wiki-2fd581b9add84e43a627ce9b722fd311?p=27dfd34c60c945698751db3a3ea0e653&pm=s)