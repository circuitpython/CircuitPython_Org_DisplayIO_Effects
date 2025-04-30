# SPDX-FileCopyrightText: Copyright (c) 2021 Alec Delaney
#
# SPDX-License-Identifier: Unlicense

"""
Use the random fluctuation effect for the Gauge.
"""

import time

import board
import displayio
from displayio_gauge import Gauge

from displayio_effects import WidgetType, fluctuation_effect

display = board.DISPLAY

# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.root_group = main_group

fluctuation_effect.hook_fluctuation_effect(Gauge, WidgetType.GAUGE)

my_gauge = Gauge(
    x=90,
    y=50,
    radius=37,
    thickness=15,
    level=70,
    outline_color=0xFFFFFF,
    foreground_color=0x00FF00,
    background_color=0x000000,
)
main_group.append(my_gauge)

my_gauge.fluctuation_amplitude = 1
my_gauge.fluctuation_move_rate = 0.01


while True:
    my_gauge.update_fluctuation()
