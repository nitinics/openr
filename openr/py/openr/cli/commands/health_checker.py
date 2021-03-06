#!/usr/bin/env python3

#
# Copyright (c) 2014-present, Facebook, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#


from builtins import object

import tabulate
from openr.clients import health_checker_client
from openr.utils import ipnetwork


class HealthCheckerCmd(object):
    def __init__(self, cli_opts):
        """ initialize the Health Checker client """

        self.client = health_checker_client.HealthCheckerClient(cli_opts)


class PeekCmd(HealthCheckerCmd):
    def run(self):
        resp = self.client.peek()
        headers = [
            "Node",
            "IP Address",
            "Last Value Sent",
            "Last Ack From Node",
            "Last Ack To Node",
        ]
        rows = []
        for name, node in resp.nodeInfo.items():
            rows.append(
                [
                    name,
                    ipnetwork.sprint_addr(node.ipAddress.addr),
                    node.lastValSent,
                    node.lastAckFromNode,
                    node.lastAckToNode,
                ]
            )

        print()
        print(tabulate.tabulate(rows, headers=headers))
        print()
