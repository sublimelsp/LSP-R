import sublime

from LSP.plugin import register_plugin
from LSP.plugin import unregister_plugin
from LSP.plugin import AbstractPlugin


def get_r_binary():
    r_binary = None
    window = sublime.active_window()
    if window:
        view = window.active_view()
        if view:
            r_ide_project_settings = view.settings().get("R-IDE", {})
            if "r_binary" in r_ide_project_settings:
                r_binary = r_ide_project_settings["r_binary"]
    if not r_binary:
        ride_settings = sublime.load_settings("R-IDE.sublime-settings")
        r_binary = ride_settings.get("r_binary")
    if not r_binary:
        r_binary = "R"
    return r_binary


class LspRPlugin(AbstractPlugin):
    @classmethod
    def name(cls):
        return __package__

    @classmethod
    def configuration(cls):
        basename = "LSP-R.sublime-settings"
        filepath = "Packages/LSP-R/{}".format(basename)
        return sublime.load_settings(basename), filepath

    @classmethod
    def additional_variables(cls):
        return {
            "r_binary": get_r_binary()
        }


class rlangPlugin(AbstractPlugin):
    @classmethod
    def name(cls):
        return "rlang"

    @classmethod
    def configuration(cls):
        print("rlang is disabled by LSP-R.")
        basename = "rlang.hidden-sublime-settings"
        filepath = "Packages/LSP-R/{}".format(basename)
        return sublime.load_settings(basename), filepath


def plugin_loaded():
    register_plugin(LspRPlugin)
    register_plugin(rlangPlugin)


def plugin_unloaded():
    unregister_plugin(LspRPlugin)
    unregister_plugin(rlangPlugin)
