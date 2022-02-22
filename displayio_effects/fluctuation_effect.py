# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
# pylint: disable=protected-access
"""
`displayio_effects.fluctuation_effect`
================================================================================

Add the fluctuation effect to your widgets


* Author(s): Alec Delaney

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

import random
from displayio_effects import WidgetType

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/tekktrik/CircuitPython_Org_DisplayIO_Effects.git"


FLUCTUATION_WIDGET_VALUES = {
    WidgetType.DIAL: "value",
    WidgetType.GAUGE: "level",
}


@property
def fluctuation_amplitude(self):
    """The furtherest the fluctuation effect can randomly set the widget value relative
    to its true position, in either direction.
    """
    return self._fluctuation_amplitude


@fluctuation_amplitude.setter
def fluctuation_amplitude(self, amplitude):
    if amplitude < 0:
        raise ValueError("Fluctuation effect setting must be larger than 0")
    if amplitude:
        self._fluctuation_hold_value = getattr(self, self._value_name)
    self._fluctuation_amplitude = amplitude


@property
def fluctuation_move_rate(self):
    """The speed at which the fluctuation effect moves the widget vaalue
    per update"""

    return self._fluctuation_move_rate


@fluctuation_move_rate.setter
def fluctuation_move_rate(self, rate):
    self._fluctuation_move_rate = rate


def update_fluctuation(self):
    """Updates the widget value and propagates the fluctuation effect refresh"""

    if self._fluctuation_amplitude == 0:
        self._fluctuation_destination = None
        return

    if self._fluctuation_destination in (None, self._fluctuation_hold_value):
        limit_bound = self._fluctuation_amplitude * 10
        self._fluctuation_destination = (
            random.uniform(-limit_bound, limit_bound) / 10
            + self._fluctuation_hold_value
        )

    value = getattr(self, self._value_name)
    value = (
        value + self._fluctuation_move_rate
        if self._fluctuation_destination > value
        else value - self._fluctuation_move_rate
    )
    setattr(self, self._value_name, value)

    threshold_check = (
        value >= self._fluctuation_destination
        if self._fluctuation_destination >= self._fluctuation_hold_value
        else value <= self._fluctuation_destination
    )
    if threshold_check:
        self._fluctuation_destination = self._fluctuation_hold_value


def hook_fluctuation_effect(widget_class, widget_type):
    """Adds the fluctuation effect for the given class

    :param widget_class: The widget that should have this effect hooked
        into them.
    :param int widget_type: The enum value of this widget type, must be a
        valid ~WidgetType

    For example, to hook this into the ``Dial`` widget, you would use the
    following code:

    .. code-block:: python

        from displayio_dial import Dial
        from 
        from displayio_effects import WidgetType, fluctuation_effect

        fluctuation_effect.hook_fluctuation_effect(Dial, WidgetType.DIAL)

    """

    value_name = FLUCTUATION_WIDGET_VALUES.get(widget_type)
    if not value_name:
        raise ValueError("The given widget does not have the ability to use this effect")

    setattr(widget_class, "_value_name", value_name)

    setattr(widget_class, "_fluctuation_destination", None)
    setattr(widget_class, "_fluctuation_hold_value", 0)

    setattr(widget_class, "fluctuation_amplitude", fluctuation_amplitude)
    setattr(widget_class, "_fluctuation_amplitude", 0)
    setattr(widget_class, "fluctuation_move_rate", fluctuation_move_rate)
    setattr(widget_class, "_fluctuation_move_rate", 0.1)

    setattr(widget_class, "update_fluctuation", update_fluctuation)
