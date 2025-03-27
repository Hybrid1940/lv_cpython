import os
import sys

base_path = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(base_path, '..', 'build')))

import lvgl as lv
import time

last_tick = time.time()

def tick_cb(_):
    global last_tick

    curr_tick = time.time()
    diff = (curr_tick * 1000) - (last_tick * 1000)

    int_diff = int(diff)
    remainder = diff - int_diff

    curr_tick -= remainder / 1000
    last_tick = curr_tick

    lv.tick_inc(int_diff)

# Initialize LVGL
lv.init()

# Set tick callback
tick_dsc = lv.tick_dsc_t()
lv.tick_set_cb(tick_dsc, tick_cb, None)

# Create SDL window
disp = lv.sdl_window_create(800, 600)

# Create group and input devices
group = lv.group_create()
lv.group_set_default(group)
mouse = lv.sdl_mouse_create()
keyboard = lv.sdl_keyboard_create()
lv.indev_set_group(keyboard, group)

# Get active screen
screen = lv.scr_act()
lv.obj_set_style_bg_color(screen, lv.color_hex(0x2D2D2D), 0)
lv.obj_set_style_bg_opa(screen, 255, 0)
lv.obj_set_scrollbar_mode(screen, lv.SCROLLBAR_MODE_OFF)

print(dir(lv))

# Create main container
main_container = lv.obj_create(screen)
lv.obj_set_size(main_container, 500, 500)
lv.obj_align(main_container, lv.ALIGN_CENTER, 0, 0)
lv.obj_set_style_pad_all(main_container, 5, 0)
lv.obj_set_style_bg_color(main_container, lv.color_hex(0x3D3D3D), 0)
lv.obj_set_style_bg_opa(main_container, 255, 0)
lv.obj_set_style_border_width(main_container, 2, 0)
lv.obj_set_style_border_color(main_container, lv.color_hex(0x555555), 0)
#lv.obj_set_layout(main_container, LV_LAYOUT_GRID)
lv.obj_set_style_grid_row_align(main_container, lv.GRID_ALIGN_SPACE_EVENLY, 0)
lv.obj_set_style_grid_column_align(main_container, lv.GRID_ALIGN_SPACE_EVENLY, 0)

grid_col_dsc = [lv.grid_fr(1)] * 8
grid_row_dsc = [lv.grid_fr(1)] * 8
lv.obj_set_grid_dsc_array(main_container, grid_col_dsc, grid_row_dsc)
"""
# Create squares
squares = []
for row in range(8):
    row_squares = []
    for col in range(8):
        square = lv.btn_create(main_container)

        lv.obj_set_grid_cell(square, lv.GRID_ALIGN_STRETCH, col, 1, lv.GRID_ALIGN_STRETCH, row, 1)
        
        # Set colors in a checkerboard pattern
        if (row + col) % 2 == 0:
            lv.obj_set_style_bg_color(square, lv.color_hex(0x808080), 0)
        else:
            lv.obj_set_style_bg_color(square, lv.color_hex(0x404040), 0)
        
        # Set active state color
        lv.obj_set_style_bg_color(square, lv.color_hex(0x00AA00), lv.STATE_PRESSED)
        
        # Store row and column as user data
        square_data = {"row": row, "col": col, "active": False}     
        # Click event handler
        def square_click_handler(e):
            btn = e.get_target()
            
            # Toggle active state
            data = btn.get_user_data()
            data["active"] = not data["active"]
            
            if data["active"]:
                lv.obj_add_state(btn, lv.STATE_CHECKED)
                lv.obj_set_style_bg_color(btn, lv.color_hex(0x00AA00), 0)
            else:
                lv.obj_clear_state(btn, lv.STATE_CHECKED)
                if (data["row"] + data["col"]) % 2 == 0:
                    lv.obj_set_style_bg_color(btn, lv.color_hex(0x808080), 0)
                else:
                    lv.obj_set_style_bg_color(btn, lv.color_hex(0x404040), 0)
            
            print(f"Square clicked at row: {data['row']}, col: {data['col']}, active: {data['active']}")
        
        square.add_event_cb(square_click_handler, lv.EVENT.CLICKED, None)
        square.set_user_data(square_data)
        
        row_squares.append(square)
    squares.append(row_squares)

# Create a title label
title = lv.label(screen)
lv.label_set_text(title, "8x8 Grid")
lv.obj_align(title, lv.ALIGN_TOP_MID, 0, 10)
lv.obj_set_style_text_font(title, lv.font_montserrat_22, 0)
lv.obj_set_style_text_color(title, lv.color_hex(0xFFFFFF), 0)

# Create a status label
status = lv.label(screen)
lv.label_set_text(status, "Click on squares to toggle them")
lv.obj_align(status, lv.ALIGN_BOTTOM_MID, 0, -10)
lv.obj_set_style_text_color(status, lv.color_hex(0xCCCCCC), 0) """


# Main loop
while True:
    time.sleep(0.001)
    lv.task_handler()
