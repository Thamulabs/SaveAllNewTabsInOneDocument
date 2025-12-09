import sublime
import sublime_plugin
import os

class SaveNewTabsCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Gather all "new" tabs: no file on disk, but has content
        new_tabs = []
        for view in self.window.views():
            if view.file_name() is None and view.size() > 0:
                new_tabs.append(view)

        if not new_tabs:
            sublime.status_message("No new unsaved tabs found.")
            return

        # Prepare content
        separator = "\n" + ("-" * 80) + "\n"
        full_content = ""
        
        for i, view in enumerate(new_tabs):
            name = view.name() or "Tab {}".format(view.id())
            content = view.substr(sublime.Region(0, view.size()))
            
            if i > 0:
                full_content += separator
            
            full_content += "### SOURCE: {} ###\n\n".format(name)
            full_content += content
            full_content += "\n"

        def on_done(filepath):
            if not filepath:
                return
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(full_content)
            except Exception as e:
                sublime.error_message("Error saving file: {}".format(str(e)))
                return
            
            # If successful, close the tabs
            for view in new_tabs:
                view.set_scratch(True) # Don't prompt to save
                view.close()
            
            sublime.status_message("Saved {} tabs to {}".format(len(new_tabs), filepath))
            # Optionally open the result
            self.window.open_file(filepath)

        # To be safe and compliant:
        if hasattr(sublime, 'save_dialog'):
             sublime.save_dialog(on_done)
        else:
            # ST3 fallback: simpler interaction
            # Create a new view, set text.
            out_view = self.window.new_file()
            out_view.set_name("Combined Tabs.txt")
            out_view.run_command("append", {"characters": full_content})
            sublime.message_dialog("Sublime Text < 4 detected.\n\nCreated a new view with combined content.\nPlease save this file manually.\nThe original tabs were NOT closed automatically for safety.")
