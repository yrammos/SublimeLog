SublimeLog
==========

A bare-bones console logger for Sublime Editor 2.


### Description

Sublime Editor 2 provides a console (accessible via ``Control-` ``) for interaction with its Python-based innards and plug-in architecture. This plug-in logs the console contents into a plain-text file ornamented with logger activation/deactivation timestamps.

The log file is erased and recreated every time Sublime Editor is launched.

### Installation

At some point I will submit this to [Will Bond's](http://wbond.net/) excellent [Package Control](http://wbond.net/sublime_packages/package_control/package_developers) repository for easy installation. For now, please install manually by cloning (or copying the contents of) this repository into your Sublime Editor `./Packages` folder (or the `./Packages/User` subfolder to prevent overwrites whenever Sublime Editor is upgraded).

### Commands

For now SublimeLog supplies only one command, which simply toggles the logger. You may invoke it with a key-binding, by default `Command-Control-C` on OS X and `Alt-Control-C` on Windows/Linux, or manually via the console:

    sublime.run_command("log_console_output")

As usual, you may modify this binding in the sublime-keymapping file appropriate to your platform:

    ./Packages/SublimeLog/Default ([OSX | Linux | Windows]).sublime-keymapping

I have not yet been able to test the plug-in or the default key-binding on Windows or Linux, so please do let me know of any issues.

### Retrieving the log

By default, the log is stored in the following plain-text file:

    [HOME]/.subl.log

You may change this in the file:

    ./Packages/SublimeLog/SublimeLog.sublime-settings
    
Whatever path-filename you enter there is relative to your root folder, so please be sure you have adequate write permissions or the plug-in will complain politely.

Also note that Sublime Editor must be restarted for changes to take effect.

### Serving suggestion

I created this to complement my LaTeX workflow during my dissertation writing. I have a terminal session (a pane in a tmux session, to be exact, but that's another story altogether) which is constantly monitoring the log file for changes:

    tail -f ~/.subl.log

This allows me to selectively view and store the Sublime Editor console stream in real-time, and in a separate window, without having to open and close the console itself.


Available under the [MIT License](http://www.opensource.org/licenses/mit-license.php). Feel free to modify and redistribute.

© 2012 Yannis Rammos

