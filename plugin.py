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


def plugin_loaded():
    register_plugin(LspRPlugin)


def plugin_unloaded():
    unregister_plugin(LspRPlugin)
