#
#
# Agora Real Time Engagement
# Created by Wei Hu in 2024-08.
# Copyright (c) 2024 Agora IO. All rights reserved.
#
#
from rte import (
    Extension,
    RteEnv,
    Cmd,
    Data,
    PcmFrame,
    ImageFrame,
    StatusCode,
    CmdResult,
)
from .log import logger
DATA_IN_TEXT_DATA_PROPERTY_TEXT = "text"

class Extension(Extension):
    def on_start(self, rte_env: RteEnv) -> None:

        # TODO: read properties, initialize resources

        rte_env.on_start_done()

    def on_stop(self, rte_env: RteEnv) -> None:

        # TODO: clean up resources

        rte_env.on_stop_done()

    def on_cmd(self, rte_env: RteEnv, cmd: Cmd) -> None:
        cmd_name = cmd.get_name()
        logger.info("on_cmd name {}".format(cmd_name))

        # TODO: process cmd

        cmd_result = CmdResult.create(StatusCode.OK)
        rte_env.return_result(cmd_result, cmd)

    def on_data(self, rte_env: RteEnv, data: Data) -> None:
        input_text = data.get_property_string(DATA_IN_TEXT_DATA_PROPERTY_TEXT)
        logger.info(f"finddatadata:{input_text}")



    