import os
from flask import Flask, render_template, send_from_directory
from scrapers.rtx3070ti.rtx3070ti_cyberpuerta import rtxList as cyberPuertaRTX3070Ti
from scrapers.rtx3070ti.rtx3070ti_amazon import rtxList as amazonRTX3070Ti
from scrapers.rtx3070ti.rtx3070ti_ebay import rtxList as ebayRTX3070Ti
from scrapers.rtx3080.rtx3080_cyberpuerta import rtxList as cyberPuertaRTX3080
from scrapers.rtx3080.rtx3080_amazon import rtxList as amazonRTX3080
from scrapers.rtx3080.rtx3080_ebay import rtxList as ebayRTX3080
from scrapers.rtx3080ti.rtx3080ti_cyberpuerta import rtxList as cyberPuertaRTX3080Ti
from scrapers.rtx3080ti.rtx3080ti_amazon import rtxList as amazonRTX3080Ti
from scrapers.rtx3080ti.rtx3080ti_ebay import rtxList as ebayRTX3080Ti
from scrapers.playstation5.playstation5_cyberpuerta import playstationList as cyberPuertaPS5
from scrapers.playstation5.playstation5_amazon import playstationList as amazonPS5
from scrapers.playstation5.playstation5_ebay import playstationList as ebayPS5
from scrapers.xboxSeriesS.xboxSeriesS_cyberpuerta import xboxList as cyberPuertaXboxS
from scrapers.xboxSeriesS.xboxSeriesS_amazon import xboxList as amazonXboxS
from scrapers.xboxSeriesS.xboxSeriesS_ebay import xboxList as ebayXboxS
from scrapers.xboxSeriesX.xboxSeriesX_amazon import xboxList as amazonXboxX
from scrapers.xboxSeriesX.xboxSeriesX_ebay import xboxList as ebayXboxX
from scrapers.nintendoSwitch.nintendoSwitch_cyberpuerta import switchList as cyberPuertaSwitch
from scrapers.nintendoSwitch.nintendoSwitch_amazon import switchList as amazonSwitch
from scrapers.nintendoSwitch.nintendoSwitch_newegg import switchList as neweggSwitch
from scrapers.nintendoSwitch.nintendoSwitch_ebay import switchList as ebaySwitch
from scrapers.rx6900xt.rx6900xt_cyberpuerta import rxList as cyberPuertaRX
from scrapers.rx6900xt.rx6900xt_amazon import rxList as amazonRX
from scrapers.rx6900xt.rx6900xt_ebay import rtxList as ebayRX
from scrapers.samsung.samsung_cyberpuerta import samsungList as cyberPuertaSamsung
from scrapers.samsung.samsung_amazon import samsungList as amazonSamsung
from scrapers.samsung.samsung_ebay import samsungList as ebaySamsung
from scrapers.iphone.iphone_amazon import iphoneList as amazonIphone
from scrapers.iphone.iphone_ebay import iphoneList as ebayIphone
from scrapers.huawei.huawei_cyberpuerta import huaweiList as cyberPuertaHuawei
from scrapers.huawei.huawei_amazon import huaweiList as amazonHuawei
from scrapers.huawei.huawei_ebay import huaweiList as ebayHuawei
from scrapers.pcs.pc_cyberpuerta import pcList as cyberPuertaPC
from scrapers.pcs.pc_amazon import pcList as amazonPC
from scrapers.pcs.pc_ebay import pcList as ebayPC
from scrapers.gamerPcs.gamerPc_cyberpuerta import pcList as cyberPuertaPCGamer
from scrapers.gamerPcs.gamerPc_amazon import pcList as amazonPCGamer
from scrapers.gamerPcs.gamerPc_ebay import pcList as ebayPCGamer

data3080 = cyberPuertaRTX3080 + amazonRTX3080 + ebayRTX3080
data3080ti = cyberPuertaRTX3080Ti + amazonRTX3080Ti + ebayRTX3080Ti
data3070ti = cyberPuertaRTX3070Ti + amazonRTX3070Ti + ebayRTX3070Ti
dataPS5 = cyberPuertaPS5 + amazonPS5 + ebayPS5
dataXboxS = cyberPuertaXboxS + amazonXboxS + ebayXboxS
dataXboxX = amazonXboxX + ebayXboxX
dataSwitch = cyberPuertaSwitch + amazonSwitch + neweggSwitch + ebaySwitch
dataRX = cyberPuertaRX + amazonRX + ebayRX
dataSamsung = cyberPuertaSamsung + amazonSamsung + ebaySamsung
dataIphone = amazonIphone + ebayIphone
dataHuawei = cyberPuertaHuawei + amazonHuawei + ebayHuawei
dataPC = cyberPuertaPC + amazonPC + ebayPC
dataPCGamer = cyberPuertaPCGamer + amazonPCGamer + ebayPCGamer


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/home/home.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/nvidia')
def nvidia():
    return render_template('/nvidia/nvidia.html')


@app.route('/nvidia/rtx-3070-ti')
def rtx3070ti():
    return render_template('/rtx3070ti/info.html', data=data3070ti)


@ app.route('/nvidia/rtx-3080')
def rtx3080():
    return render_template('/rtx3080/info.html', data=data3080)


@ app.route('/nvidia/rtx-3080-ti')
def rtx3080ti():
    return render_template('/rtx3080ti/info.html', data=data3080ti)


@ app.route('/amd/rx-6900-xt')
def rx6900xt():
    return render_template('/rx6900xt/info.html', data=dataRX)


@ app.route('/consoles')
def consoles():
    return render_template('/consoles/consoles.html')


@ app.route('/consoles/playstation-5')
def playstation5():
    return render_template('/playstation-5/info.html', data=dataPS5)


@ app.route('/consoles/xbox-series-s')
def xboxSeriesS():
    return render_template('/xbox-series-s/info.html', data=dataXboxS)


@ app.route('/consoles/xbox-series-x')
def xboxSeriesX():
    return render_template('/xbox-series-x/info.html', data=dataXboxX)


@ app.route('/consoles/nintendo-switch')
def nintendoSwitch():
    return render_template('/nintendo-switch/info.html', data=dataSwitch)


@app.route('/cellphones')
def cellphones():
    return render_template('/cellphones/cellphones.html')


@app.route('/cellphones/samsung')
def samsung():
    return render_template('/samsung/info.html', data=dataSamsung)


@app.route('/cellphones/iphone')
def iphone():
    return render_template('/iphone/info.html', data=dataIphone)


@app.route('/cellphones/huawei')
def huawei():
    return render_template('/huawei/info.html', data=dataHuawei)


@app.route('/pcs')
def pcs():
    return render_template('/pcs/info.html', data=dataPC)


@app.route('/gamer-pcs')
def gamerpcs():
    return render_template('/gamer-pcs/info.html', data=dataPCGamer)


if __name__ == '__main__':
    app.run(debug=True)
