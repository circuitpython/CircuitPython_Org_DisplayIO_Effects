# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
# pylint: disable=protected-access
"""
`displayio_effects.colorwheel_effect`
================================================================================

Add the colorwheel effect to your widgets


* Author(s): Alec Delaney

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

from adafruit_itertools import cycle
from rainbowio import colorwheel

from displayio_effects import WIDGET_TYPE_ATTR, WidgetType

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/tekktrik/CircuitPython_Org_DisplayIO_Effects.git"


COLORWHEEL_WIDGET_VALUES = {
    WidgetType.DIAL: {
        "path": ["_needle", "pixel_shader"],
        "index": 0,
    },
    WidgetType.GAUGE: {
        "path": ["_palette"],
        "index": 2,
    },
}

COLORWHEEL_COLORS = cycle([colorwheel(color_value) for color_value in range(256)])


def _get_widget_value(instance):
    widget_type = getattr(instance, WIDGET_TYPE_ATTR)
    return COLORWHEEL_WIDGET_VALUES[widget_type]


def hook_colorwheel_effect(widget_class, widget_type):
    """Adds the colorwheel effect for the given class

    :param widget_class: The widget class that should have this effect hooked
        into it
    :param int widget_type: The enum value of this widget type, must be a
        valid ~WidgetType

    For example, to hook this into the ``Dial`` widget, you would use the
    following code:

    .. code-block:: python

        from displayio_dial import Dial
        from displayio_effects import WidgetType, colorwheel_effect

        fluctuation_effect.hook_colorwheel_effect(Dial, WidgetType.DIAL)

    """

    if not COLORWHEEL_WIDGET_VALUES.get(widget_type):
        raise ValueError("The given widget does not have the ability to use this effect")

    setattr(widget_class, WIDGET_TYPE_ATTR, widget_type)

    setattr(widget_class, "update_colorwheel", update_colorwheel)


def update_colorwheel(self):
    """Updates the widget value and propagates the fluctuation effect refresh"""

    palette_map = _get_widget_value(self)
    palette_attr = self
    for attr_path in palette_map["path"]:
        palette_attr = getattr(palette_attr, attr_path)
    palette_attr[palette_map["index"]] = next(COLORWHEEL_COLORS)
