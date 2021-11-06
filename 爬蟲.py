import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
import xlsxwriter

all_att=[]

link=[
"https://hk.trip.com/travel-guide/attraction/macau/the-venetian-macao-84889/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-tower-97655/",
"https://hk.trip.com/travel-guide/attraction/macau/ruins-of-st-paul-s-76060/",
"https://hk.trip.com/travel-guide/attraction/zhuhai/hong-kong-zhuhai-macao-bridge-10539235/",
"https://hk.trip.com/travel-guide/attraction/macau/golden-reel-31044673/",
"https://hk.trip.com/travel-guide/attraction/macau/the-house-of-dancing-water-10558311/",
"https://hk.trip.com/travel-guide/attraction/macau/studio-city-macau-23058059/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-da-cunha-94434/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-eiffel-tower-30464880/",
"https://hk.trip.com/travel-guide/attraction/macau/venetian-gondola-experience-33524155/",
"https://hk.trip.com/travel-guide/attraction/macau/wynn-palace-skycab-31082382/",
"https://hk.trip.com/travel-guide/attraction/macau/city-of-dreams-94488/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-fisherman-s-wharf-81974/",
"https://hk.trip.com/travel-guide/attraction/macau/a-ma-temple-76047/",
"https://hk.trip.com/travel-guide/attraction/macau/macao-science-center-10520728/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-tower-bungee-jumping-18091086/",
"https://hk.trip.com/travel-guide/attraction/macau/teamlab-supernature-macao-78724129/",
"https://hk.trip.com/travel-guide/attraction/macau/st-dominic-s-church-76061/",
"https://hk.trip.com/travel-guide/attraction/macau/the-parisian-56814166/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-museum-82223/",
"https://hk.trip.com/travel-guide/attraction/macau/hac-sa-beach-76810/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-peninsula-10559043/",
"https://hk.trip.com/travel-guide/attraction/macau/galaxy-macau-13452339/",
"https://hk.trip.com/travel-guide/attraction/macau/coloane-10520729/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-broadway-21135280/",
"https://hk.trip.com/travel-guide/attraction/macau/wynn-palace-69412976/",
"https://hk.trip.com/travel-guide/attraction/macau/travessa-da-paixao-23865287/",
"https://hk.trip.com/travel-guide/attraction/macau/grand-resort-deck-32914889/",
"https://hk.trip.com/travel-guide/attraction/macau/wynn-music-fountain-24601422/",
"https://hk.trip.com/travel-guide/attraction/macau/ua-galaxy-cinemas-30637132/",
"https://hk.trip.com/travel-guide/attraction/macau/travessa-do-armazem-velho-24651110/",
"https://hk.trip.com/travel-guide/attraction/macau/sands-macao-58190117/",
"https://hk.trip.com/travel-guide/attraction/macau/qube-39305585/",
"https://hk.trip.com/travel-guide/attraction/macau/senado-square-82844/",
"https://hk.trip.com/travel-guide/attraction/macau/historic-centre-of-macau-82839/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-giant-panda-pavilion-24648576/",
"https://hk.trip.com/travel-guide/attraction/macau/taipa-village-22847601/",
"https://hk.trip.com/travel-guide/attraction/macau/mandarin-s-house-81972/",
"https://hk.trip.com/travel-guide/attraction/macau/batman-dark-flight-31044699/",
"https://hk.trip.com/travel-guide/attraction/macau/taipa-housesmuseum-76808/",
"https://hk.trip.com/travel-guide/attraction/macau/leal-senado-building-78460/",
"https://hk.trip.com/travel-guide/attraction/macau/grand-prix-museum-84722/",
"https://hk.trip.com/travel-guide/attraction/macau/colina-da-penha-20905937/",
"https://hk.trip.com/travel-guide/attraction/macau/our-lady-of-penha-76059/",
"https://hk.trip.com/travel-guide/attraction/macau/lotus-square-81973/",
"https://hk.trip.com/travel-guide/attraction/macau/guia-lighthouse-22847431/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-de-s-paulo-street-10644498/",
"https://hk.trip.com/travel-guide/attraction/macau/cotai-strip-resorts-22847428/",
"https://hk.trip.com/travel-guide/attraction/macau/st-francis-xavier-church-76068/",
"https://hk.trip.com/travel-guide/attraction/macau/maritime-museum-76038/",
"https://hk.trip.com/travel-guide/attraction/macau/ao-dang-bridge-18552309/",
"https://hk.trip.com/travel-guide/attraction/macau/the-cathedral-of-the-nativity-of-our-lady-macau-76055/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-da-felicidade-23865290/",
"https://hk.trip.com/travel-guide/attraction/macau/lou-lim-ieoc-garden-76043/",
"https://hk.trip.com/travel-guide/attraction/macau/saint-lawrence-s-church-76065/",
"https://hk.trip.com/travel-guide/attraction/macau/portas-do-cerco-10559039/",
"https://hk.trip.com/travel-guide/attraction/macau/st-dominic-s-square-58276675/",
"https://hk.trip.com/travel-guide/attraction/macau/nezha-temple-81954/",
"https://hk.trip.com/travel-guide/attraction/macau/lou-kau-mansion-81961/",
"https://hk.trip.com/travel-guide/attraction/macau/yongli-jixiang-tree-fugui-dragon-24601427/",
"https://hk.trip.com/travel-guide/attraction/macau/largo-de-santo-agostinho-82862/",
"https://hk.trip.com/travel-guide/attraction/macau/holy-house-of-mercy-81962/",
"https://hk.trip.com/travel-guide/attraction/macau/bronze-statue-of-goddess-guanyin-38334154/",
"https://hk.trip.com/travel-guide/attraction/macau/taipa-10521131/",
"https://hk.trip.com/travel-guide/attraction/macau/guia-hill-cable-car-38333620/",
"https://hk.trip.com/travel-guide/attraction/macau/wine-museum-76039/",
"https://hk.trip.com/travel-guide/attraction/macau/kun-iam-statue-13293732/",
"https://hk.trip.com/travel-guide/attraction/macau/largo-do-lilau-82843/",
"https://hk.trip.com/travel-guide/attraction/macau/r-do-regedor-94435/",
"https://hk.trip.com/travel-guide/attraction/macau/correlos-de-macau-94956/",
"https://hk.trip.com/travel-guide/attraction/macau/venetian-theatre-28637850/",
"https://hk.trip.com/travel-guide/attraction/macau/dom-pedro-v-theatre-10558889/",
"https://hk.trip.com/travel-guide/attraction/macau/sir-robert-ho-tung-library-81965/",
"https://hk.trip.com/travel-guide/attraction/macau/flora-garden-76042/",
"https://hk.trip.com/travel-guide/attraction/macau/camoes-garden-and-grotto-76041/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-museum-of-art-82224/",
"https://hk.trip.com/travel-guide/attraction/macau/university-of-macau-10520736/",
"https://hk.trip.com/travel-guide/attraction/macau/matsu-cultural-village-84720/",
"https://hk.trip.com/travel-guide/attraction/macau/st-anthony-s-church-76062/",
"https://hk.trip.com/travel-guide/attraction/macau/igreja-de-nossa-senhora-do-carmo-76067/",
"https://hk.trip.com/travel-guide/attraction/macau/camoes-garden-20905936/",
"https://hk.trip.com/travel-guide/attraction/macau/mgm-grand-praca-24601470/",
"https://hk.trip.com/travel-guide/attraction/macau/igreja-de-santo-agostinho-76063/",
"https://hk.trip.com/travel-guide/attraction/macau/st-joseph-seminary-and-church-81964/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-cinco-de-outubro-13364211/",
"https://hk.trip.com/travel-guide/attraction/macau/guia-marco-91564/",
"https://hk.trip.com/travel-guide/attraction/macau/our-lady-of-ftima-church-macau-76058/",
"https://hk.trip.com/travel-guide/attraction/macau/moorish-barracks-10520743/",
"https://hk.trip.com/travel-guide/attraction/macau/the-parisian-theatre-30276481/",
"https://hk.trip.com/travel-guide/attraction/macau/avenida-de-almeida-ribeiro-20905954/",
"https://hk.trip.com/travel-guide/attraction/macau/sam-kai-vui-kun-temple-76049/",
"https://hk.trip.com/travel-guide/attraction/macau/pek-tai-temple-84742/",
"https://hk.trip.com/travel-guide/attraction/macau/cheoc-van-beach-76809/",
"https://hk.trip.com/travel-guide/attraction/macau/treasure-of-sacred-art-museum-20905951/",
"https://hk.trip.com/travel-guide/attraction/macau/dangzi-bridge-22847440/",
"https://hk.trip.com/travel-guide/attraction/macau/coloane-kun-iam-temple-84755/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-cultural-centre-20905939/",
"https://hk.trip.com/travel-guide/attraction/macau/milky-way-hotel-diamond-hall-39445483/",
"https://hk.trip.com/travel-guide/attraction/macau/st-michaels-chapel-and-cemetery-22847448/",
"https://hk.trip.com/travel-guide/attraction/macau/mgm-macau-10572519/",
"https://hk.trip.com/travel-guide/attraction/macau/kun-iam-temple-76048/",
"https://hk.trip.com/travel-guide/attraction/macau/jardim-da-montanha-russa-76044/",
"https://hk.trip.com/travel-guide/attraction/macau/museum-of-taipa-and-coloane-history-18700358/",
"https://hk.trip.com/travel-guide/attraction/macau/the-city-of-dreams-dragon-light-show-10572516/",
"https://hk.trip.com/travel-guide/attraction/macau/jardm-de-sfranclsco-76045/",
"https://hk.trip.com/travel-guide/attraction/macau/chapel-of-our-lady-guia-76056/",
"https://hk.trip.com/travel-guide/attraction/macau/aomenyihao-square-10644497/",
"https://hk.trip.com/travel-guide/attraction/macau/st-lazarus-church-district-20905959/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-city-hall-23865349/",
"https://hk.trip.com/travel-guide/attraction/macau/cotai-arena-28637849/",
"https://hk.trip.com/travel-guide/attraction/macau/tam-kung-temple-76054/",
"https://hk.trip.com/travel-guide/attraction/macau/kid-s-city-22847438/",
"https://hk.trip.com/travel-guide/attraction/macau/lin-fung-temple-76050/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-canidrome-13384581/",
"https://hk.trip.com/travel-guide/attraction/macau/seac-pai-van-park-56806433/",
"https://hk.trip.com/travel-guide/attraction/macau/pou-tai-un-temple-76053/",
"https://hk.trip.com/travel-guide/attraction/macau/coloane-village-20905934/",
"https://hk.trip.com/travel-guide/attraction/macau/tak-seng-on-pawnshop-museum-20905941/",
"https://hk.trip.com/travel-guide/attraction/macau/jiamo-park-24650651/",
"https://hk.trip.com/travel-guide/attraction/macau/bajiaoting-library-22847437/",
"https://hk.trip.com/travel-guide/attraction/macau/nam-van-lake-56810168/",
"https://hk.trip.com/travel-guide/attraction/macau/museum-of-sacred-art-20905940/",
"https://hk.trip.com/travel-guide/attraction/macau/tashi-square-13293701/",
"https://hk.trip.com/travel-guide/attraction/macau/the-fire-services-museum-20905950/",
"https://hk.trip.com/travel-guide/attraction/macau/sai-van-lake-24653716/",
"https://hk.trip.com/travel-guide/attraction/macau/parque-de-d-assumpcao-20905947/",
"https://hk.trip.com/travel-guide/attraction/macau/sound-of-the-century-the-museum-of-vintage-sound-machines-20905955/",
"https://hk.trip.com/travel-guide/attraction/macau/loi-wo-temple-10534933/",
"https://hk.trip.com/travel-guide/attraction/macau/celebrity-wax-museum-30007132/",
"https://hk.trip.com/travel-guide/attraction/macau/st-lazarus-church-76066/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-sightseeing-tower-skywalk-33785584/",
"https://hk.trip.com/travel-guide/attraction/macau/tianzhujiao-art-museum-38332842/",
"https://hk.trip.com/travel-guide/attraction/macau/old-protestant-cemetery-78459/",
"https://hk.trip.com/travel-guide/attraction/macau/pao-gong-temple-76052/",
"https://hk.trip.com/travel-guide/attraction/macau/hac-sa-reservoir-country-park-24650259/",
"https://hk.trip.com/travel-guide/attraction/macau/patio-de-chon-sau-31693292/",
"https://hk.trip.com/travel-guide/attraction/macau/carmel-garden-22847685/",
"https://hk.trip.com/travel-guide/attraction/macau/domingos-road-70345884/",
"https://hk.trip.com/travel-guide/attraction/macau/gates-of-understanding-20905945/",
"https://hk.trip.com/travel-guide/attraction/macau/a-ma-statue-20905932/",
"https://hk.trip.com/travel-guide/attraction/macau/pozi-house-18700359/",
"https://hk.trip.com/travel-guide/attraction/macau/macao-convention-29890908/",
"https://hk.trip.com/travel-guide/attraction/macau/coloane-library-22847603/",
"https://hk.trip.com/travel-guide/attraction/macau/garden-of-flower-city-10534960/",
"https://hk.trip.com/travel-guide/attraction/macau/reservoir-13293702/",
"https://hk.trip.com/travel-guide/attraction/macau/jardim-de-vasco-da-gama-31690399/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-museum-of-souvenir-24648579/",
"https://hk.trip.com/travel-guide/attraction/macau/nine-macau-chapel-of-our-lady-of-seven-sorrows-76069/",
"https://hk.trip.com/travel-guide/attraction/macau/macao-open-top-bus-18535222/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-east-asian-games-dome-20905946/",
"https://hk.trip.com/travel-guide/attraction/macau/datanshan-jiaoye-park-10534970/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-grand-prix-24601359/",
"https://hk.trip.com/travel-guide/attraction/macau/avenida-da-republic-24651709/",
"https://hk.trip.com/travel-guide/attraction/macau/qube-at-the-venetian-31981564/",
"https://hk.trip.com/travel-guide/attraction/macau/museum-of-the-macau-security-forces-20905952/",
"https://hk.trip.com/travel-guide/attraction/macau/tap-seac-gallery-22847435/",
"https://hk.trip.com/travel-guide/attraction/macau/governor-s-palace-24648581/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-tea-culture-house-13293699/",
"https://hk.trip.com/travel-guide/attraction/macau/macao-historical-archives-22847433/",
"https://hk.trip.com/travel-guide/attraction/macau/jardim-do-sao-francisco-22847605/",
"https://hk.trip.com/travel-guide/attraction/macau/lin-kai-temple-76051/",
"https://hk.trip.com/travel-guide/attraction/macau/chapel-of-st-james-76057/",
"https://hk.trip.com/travel-guide/attraction/macau/fengtang-no-10-creative-park-18700357/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-design-center-50675633/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-tower-skyjump-34375560/",
"https://hk.trip.com/travel-guide/attraction/macau/communications-museum-13293675/",
"https://hk.trip.com/travel-guide/attraction/macau/saint-francis-xavier-s-church-76064/",
"https://hk.trip.com/travel-guide/attraction/macau/tap-seac-square-22847602/",
"https://hk.trip.com/travel-guide/attraction/macau/ilha-verde-91695/",
"https://hk.trip.com/travel-guide/attraction/macau/adream-workshop-3d-30007129/",
"https://hk.trip.com/travel-guide/attraction/macau/aomenmeishi-square-39267458/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-da-palha-31690183/",
"https://hk.trip.com/travel-guide/attraction/macau/aomen-yuren-matou-makeboluo-lutian-square-51626125/",
"https://hk.trip.com/travel-guide/attraction/macau/natural-and-agrarian-museum-20905949/",
"https://hk.trip.com/travel-guide/attraction/macau/tin-hau-temple-22847441/",
"https://hk.trip.com/travel-guide/attraction/macau/studio-city-auditorium-39016900/",
"https://hk.trip.com/travel-guide/attraction/macau/friendship-bridge-and-macau-taipa-bridge-24650875/",
"https://hk.trip.com/travel-guide/attraction/macau/avenida-da-amizade-22847442/",
"https://hk.trip.com/travel-guide/attraction/macau/four-faced-buddha-10534957/",
"https://hk.trip.com/travel-guide/attraction/macau/dr-carlos-d-assumpcao-park-31690673/",
"https://hk.trip.com/travel-guide/attraction/macau/avenida-horta-e-costa-58310078/",
"https://hk.trip.com/travel-guide/attraction/macau/space-museum-of-macau-24648580/",
"https://hk.trip.com/travel-guide/attraction/macau/arts-garden-22847686/",
"https://hk.trip.com/travel-guide/attraction/macau/future-bright-amusement-park-22847449/",
"https://hk.trip.com/travel-guide/attraction/macau/sight-62100038/",
"https://hk.trip.com/travel-guide/attraction/macau/guia-hill-military-tunnels-50558247/",
"https://hk.trip.com/travel-guide/attraction/macau/tang-city-24653142/",
"https://hk.trip.com/travel-guide/attraction/macau/rua-dos-ervanarios-50529245/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-tung-sin-tong-charitable-society-22847429/",
"https://hk.trip.com/travel-guide/attraction/macau/arco-oriente-38964466/",
"https://hk.trip.com/travel-guide/attraction/macau/victory-garden-58338300/",
"https://hk.trip.com/travel-guide/attraction/macau/animarte-nam-van-55832604/",
"https://hk.trip.com/travel-guide/attraction/macau/mast-climb-33351946/",
"https://hk.trip.com/travel-guide/attraction/macau/povoacao-de-ka-ho-50594917/",
"https://hk.trip.com/travel-guide/attraction/macau/small-taipa-2000-circuit-82333584/",
"https://hk.trip.com/travel-guide/attraction/macau/legend-heroes-park-73514833/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-coca-cola-museum-80267044/",
"https://hk.trip.com/travel-guide/attraction/macau/st-laorenzo-church-fengshun-church-51628563/",
"https://hk.trip.com/travel-guide/attraction/macau/parque-infantil-do-chunambeiro-51628610/",
"https://hk.trip.com/travel-guide/attraction/macau/zhuhai-ocean-ecology-museum-50614002/",
"https://hk.trip.com/travel-guide/attraction/macau/zero-latency-vr-experience-hall-79848476/",
"https://hk.trip.com/travel-guide/attraction/macau/aomenzhongyang-library-61933388/",
"https://hk.trip.com/travel-guide/attraction/macau/crypt-coffin-chamber-38960394/",
"https://hk.trip.com/travel-guide/attraction/macau/magnificent-carmo-market-67820727/",
"https://hk.trip.com/travel-guide/attraction/macau/street-steel-heavy-metal-bike-gallery-macau-77446603/",
"https://hk.trip.com/travel-guide/attraction/macau/the-patane-night-watch-house-39443786/",
"https://hk.trip.com/travel-guide/attraction/macau/aomen-lvyou-ta-huwai-square-51625507/",
"https://hk.trip.com/travel-guide/attraction/macau/yinzuo-square-51629121/",
"https://hk.trip.com/travel-guide/attraction/macau/macau-timepiece-museum-81956073/",
"https://hk.trip.com/travel-guide/attraction/macau/lianhua-square-51634273/"
]
c=0
for url in link:
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.find("div", {"class": "basicName"}) is None:
        tittle =""
    else:
        tittle = soup.find("div", {"class": "basicName"}).text

    if soup.find("i", {"class": "gs-trip-iconfont icon-opentime"}) is None:
        opentime =""
    else:
        opentime = soup.find("i", {"class": "gs-trip-iconfont icon-opentime"}).findNext("div").find("span", {"class": "field"}).text

    if soup.find("i", {"class": "gs-trip-iconfont icon-info"}) is None:
        rec_time =""
    else:
        rec_time = soup.find("i", {"class": "gs-trip-iconfont icon-info"}).findNext("div").find("span", {"class": "field"}).text

    if soup.find("i", {"class": "gs-trip-iconfont icon-address"}) is None:
        address =""
    else:
        address = soup.find("i", {"class": "gs-trip-iconfont icon-address"}).findNext("div").find("span", {"class": "field"}).text

    if soup.find("i", {"class": "gs-trip-iconfont icon-phone"}) is None:
        phone =""
    else:
        phone = soup.find("i", {"class": "gs-trip-iconfont icon-phone"}).findNext("div").find("span", {"class": "field"}).text

    if soup.find("span", {"class": "price"}) is None:
        price =""
    else:
        price = soup.find("span", {"class": "price"}).text

    if soup.find("div", {"class": "two-box"}) is None:
        content =""
    else:
        content = soup.find("div", {"class": "two-box"}).find("div").find("div").find("div").text




    att =[tittle,opentime,rec_time,address,phone,price,content]
    all_att.append(att)

with xlsxwriter.Workbook('data.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(all_att):
        worksheet.write_row(row_num, 0, data)


