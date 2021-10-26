#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:06:00 2021

@author: sunhaoxian
"""

import pandas as pd
import altair as alt
import altair_viewer
df = pd.read_csv("entertainments.csv")

base = alt.Chart(df).encode(
    x=alt.X("date:N", scale=alt.Scale(zero=False), title = 'date'),
    y=alt.Y("sum:Q", scale=alt.Scale(zero=False), title = 'Total Expenditure'),
    color="from:N",
    size = "sum:Q",
    tooltip=["date:N", "sum:Q", "from:N"]
)

img = (base.mark_point() + base.mark_line(size=4))

img.show()
img.save('altair.html')