# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney for CircuitPython Organization
#
# SPDX-License-Identifier: MIT
"""
`displayio_effects.throttle_effect`
================================================================================

Add the throttle effect to your widgets


* Author(s): Alec Delaney

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

import random

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/tekktrik/CircuitPython_Org_DisplayIO_Effects.git"


@property
def throttle_effect(self):
    """The furtherest the throttle effect can randomly set the widget value relative
    to its true position, in either direction.
    """
    return self._throttle_setting

@throttle_effect.setter
def throttle_effect(self, setting):
    if setting < 0:
        raise ValueError("Throttle effect setting must be larger than 0")
    if setting:
        self._throttle_hold_value = self.value
    self._throttle_setting = setting

@property
def throttle_effect_move_rate(self):
    """The speed at which the throttle effect moves the widget vaalue
    per update"""

    return self._throttle_move_rate

@throttle_effect_move_rate.setter
def throttle_effect_move_rate(self, rate):
    self._throttle_move_rate = rate

def throttle_update(self):
    """Updates the widget value and propagates the throttle effect refresh"""

    if self._throttle_setting == 0:
        self._throttle_destination = None
        return

    if self._throttle_destination in (None, self._throttle_hold_value):
        limit_bound = self._throttle_setting * 10
        self._throttle_destination = (
            random.uniform(-limit_bound, limit_bound) / 10
            + self._throttle_hold_value
        )

    self.value = (
        self.value + self._throttle_move_rate
        if self._throttle_destination > self.value
        else self.value - self._throttle_move_rate
    )

    threshold_check = (
        self.value >= self._throttle_destination
        if self._throttle_destination >= self._throttle_hold_value
        else self.value <= self._throttle_destination
    )
    if threshold_check:
        self._throttle_destination = self._throttle_hold_value

def hook_throttle_effect(*widget_classes):
    for widget_class in widget_classes:

        setattr(widget_class, "_throttle_destination", None)
        setattr(widget_class, "_throttle_value", 0)

        setattr(widget_class, "throttle_effect", throttle_effect)
        setattr(widget_class, "_throttle_effect", 0)
        setattr(widget_class, "throttle_effect_move_rate", throttle_effect_move_rate)
        setattr(widget_class, "_throttle_move_rate", 0.1)

        setattr(widget_class, "throttle_update", throttle_update)
