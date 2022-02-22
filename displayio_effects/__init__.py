# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
# pylint: disable=protected-access
"""
`displayio_effects`
================================================================================

Add the some flair to your widgets!


* Author(s): Alec Delaney

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""


# pylint: disable=too-few-public-methods
class WidgetType:
    """Enum values  for customizable widget types"""

    DIAL = 0
    GAUGE = 1
