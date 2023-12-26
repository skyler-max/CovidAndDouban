from pyecharts.charts import Map
from pyecharts import options as opts

import pandas as pd
Pro_Data = {}


data = pd.read_csv('data/ChinaProvinceData.csv')

for i in range(1, len(data['province'])):
    Pro_Data[data['province'][i] + '省'] = int(data['province_confirm'][i])


China_map = Map()
China_map.set_global_opts(
    # set title name
    title_opts=opts.TitleOpts(title='Covid-19 in China'),
    # let all the piece divided
    # set the data division color
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                      pieces=[
                                        {"min": 1001, "label": ">1000", "color": "#8A0808"},
                                        {"max": 1000, "min": 500, "label": "500-1000", "color": "#B40404"},
                                        {"max": 499, "min": 100, "label": "100-499", "color": "#DF0101"},
                                        {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
                                        {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
                                        {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
                                        ])
)

# add data, is_roam:whether open the mouse click reaction
China_map.add('Covid-19 in China', data_pair=list(Pro_Data.items()), maptype='china', is_roam=True)
China_map.render('Visualize_pictures/Covie-19_in_China.html')

