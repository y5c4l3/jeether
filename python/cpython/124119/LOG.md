# Win32

Windows console applications is required to set `ENABLE_VIRTUAL_TERMINAL_INPUT`
to turn on VT sequences:

https://github.com/microsoft/terminal/issues/12385

Otherwise, only virtual keys are received.

Sequences:

https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences
