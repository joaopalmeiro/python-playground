# Terminals

Metadata about different terminals.

| Terminal                      | TERM           | TERM_PROGRAM | TERM_PROGRAM_VERSION |
| ----------------------------- | -------------- | ------------ | -------------------- |
| [Warp](https://www.warp.dev/) | xterm-256color | WarpTerminal | -                    |
| [iTerm2](https://iterm2.com/) | xterm-256color | iTerm.app    | 3.4.14               |

## Development

- `pipenv install --python 3.8`.
- `pipenv shell`.
- Run this script via the desired terminal: `python script.py`.

## Notes

- [is-unicode-supported](https://github.com/sindresorhus/is-unicode-supported).
- `TERM_PROGRAM`, `TERM_PROGRAM_VERSION`, and `TERM` environment variables.
- [Support TERM_PROGRAM environment variables](https://github.com/mintty/mintty/issues/776) issue.
