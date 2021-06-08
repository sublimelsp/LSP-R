import sublime

from LSP.plugin import register_plugin
from LSP.plugin import unregister_plugin
from LSP.plugin import AbstractPlugin


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
        # TODO: don't hardcode
        return {"r_binary": "R"}


class rlangPlugin(AbstractPlugin):
    @classmethod
    def name(cls):
        return "rlang"

    @classmethod
    def configuration(cls):
        basename = "rlang.hidden-sublime-settings"
        filepath = "Packages/LSP-R/{}".format(basename)
        return sublime.load_settings(basename), filepath


def plugin_loaded():
    register_plugin(LspRPlugin)
    register_plugin(rlangPlugin)


def plugin_unloaded():
    unregister_plugin(LspRPlugin)
    unregister_plugin(rlangPlugin)
