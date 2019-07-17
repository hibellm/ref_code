#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
CREATED    :
AUTHOR     :
DESCRIPTION:
"""


# STANDARD SETUP
tools = "pan, box_select, zoom_in, zoom_out, save, reset"

# COLOUR PALETTE TO SELECT FORM
palette = ["#c9d9d3", "#718dbf", "#e84d60"]

# ADD TOOLTIPS
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Car</h3>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>HP: </strong>@Horsepower</div>
    <div><img src="@Image" alt="" width="200" /></div>
  </div>
"""
p.add_tools(hover)
