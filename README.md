# peerloop-backend
peerloop main backend repository

<br>

## Collaboration Rules

1. For every branch (so PR), open a new issue in Linear. Your branch name MUST include the Linear ticket number (ex. `PEE-18`). Follow the below branch naming rule ([Semantic Branch Names](https://gist.github.com/seunggabi/87f8c722d35cd07deb3f649d45a31082)).

    Format: `<type>/#<issueNumber>-<alias>`

    Example:

        ```
        feat/#PEE-18-init-files
        ^--^ ^-----^
        |          |
        |          +---> issue's keyword
        |
        +-------> Type: or feat, chore, docs, fix, refactor, style, or test.
        ```
    Branch type:

    | Type | Description |
    | --- | --- |
    | `feat` | New feature for the user, not a new feature for build script. |
    | `fix` | Bug fix for the user, not a fix to a build script. |
    | `docs` | Changes to the documentation. |
    | `style` | Formatting, missing semi colons, etc; no production code change. |
    | `refactor` | Refactoring production code, eg. renaming a variable. |
    | `test` | Adding missing tests, refactoring tests; no production code change. |
    | `chore` | Updating grunt tasks etc; no production code change. |

2. PR name **MUST** include Linear ticket number.

    Format: `[<issueNumber>] <PR name>`

    Example: `[PEE-81] Add email validation logic`

3. If you update the env file, run `update_env_format.py` to update `.env-format`.

    ```sh
    update_env_format.py -e .env.local
    ```

4. To apply linter & formatter, run `./lint_format.sh`.

5. Configure `pre-commit` hook.

    > Ref: [How to setup pre-commit hook](https://www.notion.so/Backend-Wiki-2fd581b9add84e43a627ce9b722fd311?p=27dfd34c60c945698751db3a3ea0e653&pm=s)

6. To commit your work, use `cz c` instead of `git commit`.

    Format: `<type>: <commitMessage>`

    Example: `🔧 fix: modify email validation logic`

    Commit type:

    | Type | Description |
    | --- | --- |
    | :sparkles: feat | Work on feature-related tasks. |
    | :wrench: fix | Fix a bug. |  |
    | :memo: docs | Add or update documentation. |
    | :recycle: refact | Refactor code. |
    | :art: style | Improve structure/format of the code or apply linter. |
    | :white_check_mark: test | Add, update, or pass tests. |
    | :broom: chore | Do other grunt works. |
    | :gear: setting | Add or update setting related tasks such as modifying dependencies, writing util scripts, etc. |
    | :label: bump | Add a release / version tag. |
    | :tada: init | Create a new project. |
