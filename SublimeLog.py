import sublime_plugin
import sys
import sublime
import os
import time


class LogConsoleOutputCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        # First we backup standard input and output pipes.
        self.active = False
        self.ready = True
        self.out_backup = sys.stdout
        self.err_backup = sys.stderr

        # Then we obtain the log filename from settings, if available, otherwise use default.
        # Path handling should be cross-platform but has only been tested on OS X (for lack of access to other systems).
        settings = sublime.load_settings("LogConsoleOutput.sublime-settings")
        self.logfilename = os.path.abspath(settings.get("logfile", os.path.join(os.path.expanduser("~"), ".subl.log")))
        print self.logfilename

        # We open and truncate log file, or create a blank one if one doesn't exist, or there's an exception and we exit.
        try:
            self.logfile = open(os.path.abspath(self.logfilename), "w", 0)
            self.logfile.truncate(0)
        except:
            sublime.status_message("Error opening log file (" + str(self.logfilename) + ").")
            self.ready = False
            return

    def run(self):
        # Here we toggle the logger, after ensuring that the log file has been properly opened.
        # There may be a more efficient way to do this but for all intents and purposes the overhead is tiny.
        if self.ready:
            if not self.active:
                self.active = True
                sublime.status_message("Console logging activated (" + self.logfilename + ").")
                sys.stdout = self
                sys.stderr = self
                print "=> => => Console logging activated (" + self.logfilename + "). Timestamp: " + time.strftime("%d %b %Y, %X", time.localtime()) + "."
            else:
                self.active = False
                sublime.status_message("Console logging deactivated (" + self.logfilename + ").")
                print "<= <= <= Console logging deactivated (" + self.logfilename + "). Timestamp: " + time.strftime("%d %b %Y, %X", time.localtime()) + "."
                sys.stdout = self.out_backup
                sys.stderr = self.err_backup
        else:
            sublime.status_message("Error opening log file (" + str(self.logfilename) + ").")
            return

    def write(self, message):
        # This method overrides sys.stdout.write() and sys.stderr.write().
        # It simply duplicates the contents of the standard output and error pipes into the log file.
        self.out_backup.write(message)
        self.logfile.write(message)
