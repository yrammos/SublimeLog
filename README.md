SublimeLog
==========

A bare-bones console logger for Sublime Text 2.


### Description

Sublime Text 2 provides a console (accessible via ``Control-` ``) for interaction with its Python-based innards and plug-in architecture. This plug-in logs the console contents into a plain-text file ornamented with logger activation/deactivation timestamps.

The log is erased and recreated each time Sublime Text is launched.

### Installation

At some point I will submit this to [Will Bond's](http://wbond.net/) excellent [Package Control](http://wbond.net/sublime_packages/package_control/package_developers) repository for easy installation. For now, please install manually by cloning (or copying the contents of) this repository into your Sublime Text `./Packages` folder:

    git clone https://github.com/yrammos/SublimeLog.git

### Commands

For now SublimeLog supplies a single command that toggles the logger. The default key-binding is `Command-Control-C` on OS X or `Alt-Control-C` on Windows/Linux. You may also invoke it manually via the console:

    sublime.run_command("log_console_output")

The key-binding is adjustable in the JSON file appropriate to your platform:

    ./Packages/SublimeLog/Default ([OSX | Linux | Windows]).sublime-keymapping

I have not yet been able to test the plug-in or the default key-binding on Windows or Linux, so please do let me know of any issues.

### Retrieving the log

By default, the console is logged in the following plain-text file:

    [HOME]/.subl.log

This destination is adjustable in:

    ./Packages/SublimeLog/SublimeLog.sublime-settings
    
Whatever path-filename you declare for the log is relative to your root folder, so please be sure you have adequate write permissions or the plug-in will complain politely.

Note that Sublime Text must be restarted for changes to take effect.

### Serving suggestion

I wrote this plug-in as a complement to my dissertation LaTeX workflow. I just keep a terminal session open (a pane in a tmux session, to be exact) and have it constantly monitor the log file for changes:

    tail -f ~/.subl.log

This provides me with a dynamic view of the console stream in a separate window, without the space- and time-consuming tedium of opening and closing the console itself.


Available under the [MIT License](http://www.opensource.org/licenses/mit-license.php). Feel free to modify and redistribute.

© 2012 Yannis Rammos

