SublimeLog
==========

A bare-bones console logger for Sublime Text 2 and 3.


### Description

[Sublime Text 2 and 3](http://www.sublimetext.com) provide a console (accessible via ``Control-` ``) for interaction with their Python-based innards and plug-in architecture. This plug-in logs the console contents into a plain-text file ornamented with logger activation/deactivation timestamps.

The log is erased and recreated each time Sublime Text is launched.

### Installation

The most straightforward installation method is by far via [Will Bond's](http://wbond.net/) superb [Package Control](http://wbond.net/sublime_packages/package_control/package_developers). Alternatively, you may clone (or copy the contents of) this repository into your Sublime Text `./Packages` folder:

    git clone https://github.com/yrammos/SublimeLog.git

### Commands

For now SublimeLog supplies a single command that toggles the logger. The default key-binding is `Command-Control-C` on OS X or `Alt-Control-C` on Windows/Linux. You may also invoke it via the command palette (⌘-Shift-P on a Mac or Ctrl-Shift-P otherwise): `SublimeLog: Toggle logger (on/off)`

The key-binding is adjustable in the default JSON file appropriate to your platform:

    ./Packages/SublimeLog/Default ({OSX | Linux | Windows}).sublime-keymapping

or, to prevent overwrites following plugin updates, in a corresponding file within the User subfolder:

    ./Packages/User/SublimeLog ({OSX | Linux | Windows}).sublime-keymapping

### Retrieving the log

By default, the console is logged in the following plain-text file:

    {HOME}/.subl.log

This default destination is adjustable in:

    ./Packages/SublimeLog/SublimeLog.sublime-settings

or, preferably, in the User subfolder:

	./Packages/User/SublimeLog.sublime-settings
    
Whatever path-filename you declare for the log is relative to your root folder, so please be sure you have adequate write permissions or the plug-in will complain politely.

Note that Sublime Text no longer needs to be restarted for changes to these settings to take effect.

### Limitations

Due to technical limitations beyond my control, the plug does not capture "system" messages output to the console by Sublime Text itself. Among them are, for example, `Reloading plugin...` messages. This should be inconsequential for most users of `SublimeLog` but Your Mileage May Vary. See [this thread](http://www.sublimetext.com/forum/viewtopic.php?f=5&t=7655) if you are interested in further details.

### Serving suggestion

I wrote this plug-in as a complement to my dissertation LaTeX workflow. Within a dedicated terminal session, or a tmux pane for that matter, I constantly monitor the log file for changes:

    tail -f ~/.subl.log

This provides me with a dynamic view of the console stream in a separate window, without the space- and time-consuming tedium of opening and closing the console itself.

### Version history

#### 4/18/2013
- NEW: Adds support for Sublime Text 3
- NEW: Settings modifications no longer necessitate an editor restart to take effect.

#### 7/17/2012
- NEW: Adds preferences menu (Sublime Text 2 > Preferences > Package Settings > SublimeLog).
- FIXED: Default and user preferences are now honored as expected.

#### 6/26/2012
- NEW: Plugin now available via [Package Control](http://wbond.net/sublime_packages/package_control/package_developers).

#### 6/22/2012
- NEW: First release.

Copyright © 2012-3 by [Yannis Rammos](twitter.com/yannisrammos). This work is made available under the terms of the Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) license, <http://creativecommons.org/licenses/by-sa/3.0/>.
