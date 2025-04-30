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

WIDGET_TYPE_ATTR = "_widget_type"


# pylint: disable=too-few-public-methods
class WidgetType:
    """Enum values  for customizable widget types.  Valid options are:

    - ``WidgetType.DIAL`` - Dial widget
    - ``WidgetType.GAUGE`` - Gauge widget
    """

    DIAL = 0
    GAUGE = 1
