# confirm dead heal importedCase

import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts

data = pd.read_csv('工作簿1.csv')
# 第N周
monthsName = ['第' + str(i) + '周' for i in range(1, 25)]
# type converting
# for i in range(1, 38):
#     columnName = str(i) + '区'
regionData = data['1区']
regionData1 = data['2区']
regionData2 = data['3区']
regionData3 = data['4区']
regionData4 = data['5区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('1区', list(regionData))
    .add_yaxis('2区', list(regionData1))
    .add_yaxis('3区', list(regionData2))
    .add_yaxis('4区', list(regionData3))
    .add_yaxis('5区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying1-5.html')

regionData = data['6区']
regionData1 = data['7区']
regionData2 = data['8区']
regionData3 = data['9区']
regionData4 = data['10区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('6区', list(regionData))
    .add_yaxis('7区', list(regionData1))
    .add_yaxis('8区', list(regionData2))
    .add_yaxis('9区', list(regionData3))
    .add_yaxis('10区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuyying6-10.html')

regionData = data['11区']
regionData1 = data['12区']
regionData2 = data['13区']
regionData3 = data['14区']
regionData4 = data['15区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('11区', list(regionData))
    .add_yaxis('12区', list(regionData1))
    .add_yaxis('13区', list(regionData2))
    .add_yaxis('14区', list(regionData3))
    .add_yaxis('15区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutSaleTop11-15.html')

regionData = data['16区']
regionData1 = data['17区']
regionData2 = data['18区']
regionData3 = data['19区']
regionData4 = data['20区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('16区', list(regionData))
    .add_yaxis('17区', list(regionData1))
    .add_yaxis('18区', list(regionData2))
    .add_yaxis('19区', list(regionData3))
    .add_yaxis('20区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying15-20.html')

regionData = data['21区']
regionData1 = data['22区']
regionData2 = data['23区']
regionData3 = data['24区']
regionData4 = data['25区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('21区', list(regionData))
    .add_yaxis('22区', list(regionData1))
    .add_yaxis('23区', list(regionData2))
    .add_yaxis('24区', list(regionData3))
    .add_yaxis('25区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying21-25.html')

regionData = data['26区']
regionData1 = data['27区']
regionData2 = data['28区']
regionData3 = data['29区']
regionData4 = data['30区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('26区', list(regionData))
    .add_yaxis('27区', list(regionData1))
    .add_yaxis('28区', list(regionData2))
    .add_yaxis('29区', list(regionData3))
    .add_yaxis('30区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying26-30.html')
regionData = data['31区']
regionData1 = data['32区']
regionData2 = data['33区']
regionData3 = data['34区']
regionData4 = data['35区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('31区', list(regionData))
    .add_yaxis('32区', list(regionData1))
    .add_yaxis('33区', list(regionData2))
    .add_yaxis('34区', list(regionData3))
    .add_yaxis('35区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying31-35.html')

regionData = data['36区']
regionData1 = data['37区']
# regionData2 = data['33区']
# regionData3 = data['34区']
# regionData4 = data['35区']
# regionData5 = data['6区']
# regionData6 = data['7区']
# regionData7 = data['8区']
# regionData8 = data['8区']
# regionData9 = data['10区']


table = (
    Line()
    .add_xaxis(monthsName)

    .add_yaxis('36区', list(regionData))
    .add_yaxis('37区', list(regionData1))
    # .add_yaxis('33区', list(regionData2))
    # .add_yaxis('34区', list(regionData3))
    # .add_yaxis('35区', list(regionData4))
    # .add_yaxis('6区', list(regionData5))
    # .add_yaxis('7区', list(regionData6))
    # .add_yaxis('8区', list(regionData7))
    # .add_yaxis('9区', list(regionData8))
    # .add_yaxis('10区', list(regionData9))



    .set_global_opts(title_opts=opts.TitleOpts(title='月为单位的回购率'))

    )

table.render('TrendsAboutRebuying36-37.html')