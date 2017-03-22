from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, NumberFormatter, PreText, Select
from bokeh.io import curdoc

# import data from excel
master = pd.read_excel(join(dirname(__file__), 'master.xlsx'), sheetname='Master Data', header=[1,2,3])
simp = pd.read_excel(join(dirname(__file__), 'master.xlsx'), sheetname='Master Data', header=3)

# create a source data table
source = ColumnDataSource(data=dict())

# update method
def update():

    # filter by project delivery method
    c1 = simp['Relevant Project 1 - Project Delivery Method'] == pdm_select.value
    c2 = simp['Relevant Project 2 - Project Delivery Method'] == pdm_select.value
    c3 = simp['Relevant Project 3 - Project Delivery Method'] == pdm_select.value
    c4 = simp['Relevant Project 4 - Project Delivery Method'] == pdm_select.value
    df = simp[c1 | c2 | c3 | c4]
    
    # filter by union
    c5 = simp[un_select.value] == 'Yes'
    df = df[c5]
    
    # select only certain columns for export
    exp = df[['Company Name','Company Address (HQ)', 'Company City (HQ)', 'Company State (HQ)', 'POC Name', 'POC Title', 'POC Email']]

    # put data in source dictionary
    source.data = {
        'name': exp['Company Name'],
        'address': exp['Company Address (HQ)'],
        'city': exp['Company City (HQ)']
    }


# create inputs
PROJECT_DELIVERY_METHODS = ['CM-at-Risk', 'Design-Build', 'Design-Bid-Build/GC']
pdm_select = Select(value='CM-at-Risk', options=PROJECT_DELIVERY_METHODS)
pdm_select.on_change('value', lambda attr, old, new: update())

UNION_OPTIONS = ['Union', 'Non-Union']
un_select = Select(value='Non-Union', options=UNION_OPTIONS)
un_select.on_change('value', lambda attr, old, new: update())

button = Button(label="Download", button_type="success")
button.callback = CustomJS(args=dict(source=source),
                           code=open(join(dirname(__file__), "download.js")).read())

# Prepare Table
columns = [
    TableColumn(field="name", title="Company Name"),
    TableColumn(field="address", title="Address"),  # formatter=NumberFormatter(format="$0,0.00")
    TableColumn(field="city", title="City")
]

data_table = DataTable(source=source, columns=columns, width=800)

controls = widgetbox(pdm_select, un_select, button)
table = widgetbox(data_table)

curdoc().add_root(row(controls, table))
curdoc().title = "Dashboard"

update()
