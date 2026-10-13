from __future__ import annotations

from typing import final

from LSP.plugin import LspPlugin


@final
class LspRPlugin(LspPlugin):
    pass


def plugin_loaded() -> None:
    LspRPlugin.register()


def plugin_unloaded() -> None:
    LspRPlugin.unregister()
