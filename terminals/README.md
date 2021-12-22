# Terminals

Metadata about different terminals.

| Terminal                                                                 | TERM           | TERM_PROGRAM   | TERM_PROGRAM_VERSION | OS            |
| ------------------------------------------------------------------------ | -------------- | -------------- | -------------------- | ------------- |
| [Warp](https://www.warp.dev/)                                            | xterm-256color | WarpTerminal   | -                    | macOS-10.15.7 |
| [iTerm2](https://iterm2.com/)                                            | xterm-256color | iTerm.app      | 3.4.14               | macOS-10.15.7 |
| [Terminal (macOS)](https://support.apple.com/guide/terminal/welcome/mac) | xterm-256color | Apple_Terminal | 433                  | macOS-10.15.7 |
| [Hyper](https://hyper.is/)                                               | xterm-256color | Hyper          | 3.1.4                | macOS-10.15.7 |

## Development

- `pipenv install --python 3.8`.
- `pipenv shell`.
- Run this script via the desired terminal: `python script.py`.

## Notes

- [is-unicode-supported](https://github.com/sindresorhus/is-unicode-supported).
- `TERM_PROGRAM`, `TERM_PROGRAM_VERSION`, and `TERM` environment variables.
- [Support TERM_PROGRAM environment variables](https://github.com/mintty/mintty/issues/776) issue.
- Table:
  - The `OS` column corresponds to the operating system where the script was run.
  - `-` represents the default value for _undefined_ environment variables.
- Hyper [themes](https://hyper.is/themes).
- Terminals or terminal emulators.
