#
#
# Agora Real Time Engagement
# Created by Wei Hu in 2024-08.
# Copyright (c) 2024 Agora IO. All rights reserved.
#
#
from rte import (
    Addon,
    register_addon_as_extension,
    RteEnv,
)
from .extension import Extension
from .log import logger

@register_addon_as_extension("wirite_data")
class ExtensionAddon(Addon):
    def on_create_instance(self, rte_env: RteEnv, name: str, context) -> None:
        rte_env.on_create_instance_done(Extension(name), context)
