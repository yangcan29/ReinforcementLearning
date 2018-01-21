import numpy as np

subway_dict = [
    ["1-苹果园", "1-古城", 2606],
    ["1-古城", "1-八角游乐园", 1921],
    ["1-八角游乐园", "1-八宝山", 1953],
    ["1-八宝山", "1-玉泉路", 1479],
    ["1-玉泉路", "1-五棵松", 1810],
    ["1-五棵松", "1-万寿路", 1778],
    ["1-万寿路", "1-公主坟", 1313],
    ["1-公主坟", "1-军事博物馆", 1172],
    ["1-军事博物馆", "1-木樨地", 1166],
    ["1-木樨地", "1-南礼士路", 1291],
    ["1-南礼士路", "1-复兴门", 424],
    ["1-复兴门", "1-西单", 1590],
    ["1-西单", "1-天安门西", 1217],
    ["1-天安门西", "1-天安门东", 925],
    ["1-天安门东", "1-王府井", 852],
    ["1-王府井", "1-东单", 774],
    ["1-东单", "1-建国门", 1230],
    ["1-建国门", "1-永安里", 1377],
    ["1-永安里", "1-国贸", 790],
    ["1-国贸", "1-大望路", 1385],
    ["1-大望路", "1-四惠", 1673],
    ["1-四惠", "1-四惠东", 1714],
    ["2-西直门", "2-车公庄", 909],
    ["2-车公庄", "2-阜成门", 960],
    ["2-阜成门", "2-复兴门", 1832],
    ["2-复兴门", "2-长椿街", 1234],
    ["2-长椿街", "2-宣武门", 929],
    ["2-宣武门", "2-和平门", 851],
    ["2-和平门", "2-前门", 1171],
    ["2-前门", "2-崇文门", 1634],
    ["2-崇文门", "2-北京站", 1023],
    ["2-北京站", "2-建国门", 945],
    ["2-建国门", "2-朝阳门", 1763],
    ["2-朝阳门", "2-东四十条", 1027],
    ["2-东四十条", "2-东直门", 824],
    ["2-东直门", "2-雍和宫", 2228],
    ["2-雍和宫", "2-安定门", 794],
    ["2-安定门", "2-鼓楼大街", 1237],
    ["2-鼓楼大街", "2-积水潭", 1766],
    ["2-积水潭", "2-西直门", 1899],
    ["4-安河桥北", "4-北宫门", 1363],
    ["4-北宫门", "4-西苑", 1251],
    ["4-西苑", "4-圆明园", 1672],
    ["4-圆明园", "4-北京大学东门", 1295],
    ["4-北京大学东门", "4-中关村", 887],
    ["4-中关村", "4-海淀黄庄", 900],
    ["4-海淀黄庄", "4-人民大学", 1063],
    ["4-人民大学", "4-魏公村", 1051],
    ["4-魏公村", "4-国家图书馆", 1658],
    ["4-国家图书馆", "4-动物园", 1517],
    ["4-动物园", "4-西直门", 1441],
    ["4-西直门", "4-新街口", 1025],
    ["4-新街口", "4-平安里", 1100],
    ["4-平安里", "4-西四", 1100],
    ["4-西四", "4-灵境胡同", 869],
    ["4-灵境胡同", "4-西单", 1011],
    ["4-西单", "4-宣武门", 815],
    ["4-宣武门", "4-菜市口", 1152],
    ["4-菜市口", "4-陶然亭", 1200],
    ["4-陶然亭", "4-北京南站", 1643],
    ["4-北京南站", "4-马家堡", 1480],
    ["4-马家堡", "4-角门西", 827],
    ["4-角门西", "4-公益西桥", 989],
    ["5-天通苑北", "5-天通苑", 939],
    ["5-天通苑", "5-天通苑南", 965],
    ["5-天通苑南", "5-立水桥", 1544],
    ["5-立水桥", "5-立水桥南", 1305],
    ["5-立水桥南", "5-北苑路北", 1286],
    ["5-北苑路北", "5-大屯路东", 3000],
    ["5-大屯路东", "5-惠新西街北口", 1838],
    ["5-惠新西街北口", "5-惠新西街南口", 1122],
    ["5-惠新西街南口", "5-和平西桥", 1025],
    ["5-和平西桥", "5-和平里北街", 1059],
    ["5-和平里北街", "5-雍和宫", 1151],
    ["5-雍和宫", "5-北新桥", 866],
    ["5-北新桥", "5-张自忠路", 791],
    ["5-张自忠路", "5-东四", 1016],
    ["5-东四", "5-灯市口", 848],
    ["5-灯市口", "5-东单", 945],
    ["5-东单", "5-崇文门", 821],
    ["5-崇文门", "5-磁器口", 876],
    ["5-磁器口", "5-天坛东门", 1183],
    ["5-天坛东门", "5-蒲黄榆", 1900],
    ["5-蒲黄榆", "5-刘家窑", 905],
    ["5-刘家窑", "5-宋家庄", 1670],
    ["6-海淀五路居", "6-慈寿寺", 1508],
    ["6-慈寿寺", "6-花园桥", 1431],
    ["6-花园桥", "6-白石桥南", 1166],
    ["6-白石桥南", "6-车公庄西", 1664],
    ["6-车公庄西", "6-车公庄", 887],
    ["6-车公庄", "6-平安里", 1443],
    ["6-平安里", "6-北海北", 1321],
    ["6-北海北", "6-南锣鼓巷", 1349],
    ["6-南锣鼓巷", "6-东四", 1937],
    ["6-东四", "6-朝阳门", 1399],
    ["6-朝阳门", "6-东大桥", 1668],
    ["6-东大桥", "6-呼家楼", 845],
    ["6-呼家楼", "6-金台路", 1450],
    ["6-金台路", "6-十里堡", 2036],
    ["6-十里堡", "6-青年路", 1282],
    ["6-青年路", "6-褡裢坡", 3999],
    ["6-褡裢坡", "6-黄渠", 1238],
    ["6-黄渠", "6-常营", 1854],
    ["6-常营", "6-草房", 1405],
    ["6-草房", "6-物资学院路", 2115],
    ["6-物资学院路", "6-通州北关", 2557],
    ["6-通州北关", "6-通运门", 1468],
    ["6-通运门", "6-北运河西", 1543],
    ["6-北运河西", "6-北运河东", 1599],
    ["6-北运河东", "6-郝家府", 929],
    ["6-郝家府", "6-东夏园", 1346],
    ["6-东夏园", "6-潞城", 1194],
    ["7-北京西站", "7-湾子", 935],
    ["7-湾子", "7-达官营", 734],
    ["7-达官营", "7-广安门内", 1874],
    ["7-广安门内", "7-菜市口", 1374],
    ["7-菜市口", "7-虎坊桥", 885],
    ["7-虎坊桥", "7-珠市口", 1205],
    ["7-珠市口", "7-桥湾", 869],
    ["7-桥湾", "7-磁器口", 1016],
    ["7-磁器口", "7-广渠门内", 1138],
    ["7-广渠门内", "7-广渠门外", 1332],
    ["7-广渠门外", "7-双井", 1241],
    ["7-双井", "7-九龙山", 1311],
    ["7-九龙山", "7-大郊亭", 781],
    ["7-大郊亭", "7-百子湾", 865],
    ["7-百子湾", "7-化工", 903],
    ["7-化工", "7-南楼梓庄", 1464],
    ["7-南楼梓庄", "7-欢乐谷景区", 906],
    ["7-欢乐谷景区", "7-垡头", 1679],
    ["7-垡头", "7-双合", 1304],
    ["7-双合", "7-焦化厂", 1021],
    ["8-朱辛庄", "8-育知路", 2318],
    ["8-育知路", "8-平西府", 1985],
    ["8-平西府", "8-回龙观东大街", 2056],
    ["8-回龙观东大街", "8-霍营", 1114],
    ["8-霍营", "8-育新", 1894],
    ["8-育新", "8-西小口", 1543],
    ["8-西小口", "8-永泰庄", 1041],
    ["8-永泰庄", "8-林萃桥", 2553],
    ["8-林萃桥", "8-森林公园南门", 2555],
    ["8-森林公园南门", "8-奥林匹克公园", 1016],
    ["8-奥林匹克公园", "8-奥体中心", 1667],
    ["8-奥体中心", "8-北土城", 900],
    ["8-北土城", "8-安华桥", 1018],
    ["8-安华桥", "8-安德里北街", 1274],
    ["8-安德里北街", "8-鼓楼大街", 1083],
    ["8-鼓楼大街", "8-什刹海", 1188],
    ["8-什刹海", "8-南锣鼓巷", 902],
    ["9-国家图书馆", "9-白石桥南", 1096],
    ["9-白石桥南", "9-白堆子", 943],
    ["9-白堆子", "9-军事博物馆", 1912],
    ["9-军事博物馆", "9-北京西站", 1398],
    ["9-北京西站", "9-六里桥东", 1170],
    ["9-六里桥东", "9-六里桥", 1309],
    ["9-六里桥", "9-七里庄", 1778],
    ["9-七里庄", "9-丰台东大街", 1325],
    ["9-丰台东大街", "9-丰台南路", 1585],
    ["9-丰台南路", "9-科怡路", 980],
    ["9-科怡路", "9-丰台科技园", 788],
    ["9-丰台科技园", "9-郭公庄", 1347],
    ["10-巴沟", "10-苏州街", 1110],
    ["10-苏州街", "10-海淀黄庄", 950],
    ["10-海淀黄庄", "10-知春里", 975],
    ["10-知春里", "10-知春路", 1058],
    ["10-知春路", "10-西土城", 1101],
    ["10-西土城", "10-牡丹园", 1330],
    ["10-牡丹园", "10-健德门", 973],
    ["10-健德门", "10-北土城", 1100],
    ["10-北土城", "10-安贞门", 1020],
    ["10-安贞门", "10-惠新西街南口", 982],
    ["10-惠新西街南口", "10-芍药居", 1712],
    ["10-芍药居", "10-太阳宫", 1003],
    ["10-太阳宫", "10-三元桥", 1759],
    ["10-三元桥", "10-亮马桥", 1506],
    ["10-亮马桥", "10-农业展览馆", 914],
    ["10-农业展览馆", "10-团结湖", 853],
    ["10-团结湖", "10-呼家楼", 1149],
    ["10-呼家楼", "10-金台夕照", 734],
    ["10-金台夕照", "10-国贸", 835],
    ["10-国贸", "10-双井", 1759],
    ["10-双井", "10-劲松", 1006],
    ["10-劲松", "10-潘家园", 1021],
    ["10-潘家园", "10-十里河", 1097],
    ["10-十里河", "10-分钟寺", 1804],
    ["10-分钟寺", "10-成寿寺", 1058],
    ["10-成寿寺", "10-宋家庄", 1677],
    ["10-宋家庄", "10-石榴庄", 1269],
    ["10-石榴庄", "10-大红门", 1244],
    ["10-大红门", "10-角门东", 1130],
    ["10-角门东", "10-角门西", 1254],
    ["10-角门西", "10-草桥", 1688],
    ["10-草桥", "10-纪家庙", 1547],
    ["10-纪家庙", "10-首经贸", 1143],
    ["10-首经贸", "10-丰台站", 1717],
    ["10-丰台站", "10-泥洼", 954],
    ["10-泥洼", "10-西局", 749],
    ["10-西局", "10-六里桥", 1584],
    ["10-六里桥", "10-莲花桥", 2392],
    ["10-莲花桥", "10-公主坟", 1016],
    ["10-公主坟", "10-西钓鱼台", 2386],
    ["10-西钓鱼台", "10-慈寿寺", 1214],
    ["10-慈寿寺", "10-车道沟", 1590],
    ["10-车道沟", "10-长春桥", 1205],
    ["10-长春桥", "10-火器营", 961],
    ["10-火器营", "10-巴沟", 1495],
    ["13-西直门", "13-大钟寺", 2839],
    ["13-大钟寺", "13-知春路", 1206],
    ["13-知春路", "13-五道口", 1829],
    ["13-五道口", "13-上地", 4866],
    ["13-上地", "13-西二旗", 2538],
    ["13-西二旗", "13-龙泽", 3623],
    ["13-龙泽", "13-回龙观", 1423],
    ["13-回龙观", "13-霍营", 2110],
    ["13-霍营", "13-立水桥", 4785],
    ["13-立水桥", "13-北苑", 2272],
    ["13-北苑", "13-望京西", 6720],
    ["13-望京西", "13-芍药居", 2152],
    ["13-芍药居", "13-光熙门", 1110],
    ["13-光熙门", "13-柳芳", 1135],
    ["13-柳芳", "13-东直门", 1769],
    ["14W-张郭庄", "14W-园博园", 1345],
    ["14W-园博园", "14W-大瓦窑", 4073],
    ["14W-大瓦窑", "14W-郭庄子", 1236],
    ["14W-郭庄子", "14W-大井", 2044],
    ["14W-大井", "14W-七里庄", 1579],
    ["14W-七里庄", "14W-西局", 845],
    ["14E-北京南站", "14E-陶然桥", 887],
    ["14E-陶然桥", "14E-永定门外", 1063],
    ["14E-永定门外", "14E-景泰", 1119],
    ["14E-景泰", "14E-蒲黄榆", 1025],
    ["14E-蒲黄榆", "14E-方庄", 1486],
    ["14E-方庄", "14E-十里河", 1618],
    ["14E-十里河", "14E-南八里庄", 1147],
    ["14E-南八里庄", "14E-北工大西门", 1276],
    ["14E-北工大西门", "14E-平乐园", 1128],
    ["14E-平乐园", "14E-九龙山", 897],
    ["14E-九龙山", "14E-大望路", 1780],
    ["14E-大望路", "14E-红庙", 708],
    ["14E-红庙", "14E-金台路", 894],
    ["14E-金台路", "14E-朝阳公园", 1085],
    ["14E-朝阳公园", "14E-枣营", 1221],
    ["14E-枣营", "14E-东风北桥", 2173],
    ["14E-东风北桥", "14E-将台", 1600],
    ["14E-将台", "14E-高家园", 1171],
    ["14E-高家园", "14E-望京南", 676],
    ["14E-望京南", "14E-阜通", 1168],
    ["14E-阜通", "14E-望京", 903],
    ["14E-望京", "14E-东湖渠", 1283],
    ["14E-东湖渠", "14E-来广营", 1100],
    ["14E-来广营", "14E-善各庄", 1364],
    ["15-清华东路西口", "15-六道口", 1144],
    ["15-六道口", "15-北沙滩", 1337],
    ["15-北沙滩", "15-奥林匹克公园", 1999],
    ["15-奥林匹克公园", "15-安立路", 1368],
    ["15-安立路", "15-大屯路东", 938],
    ["15-大屯路东", "15-关庄", 1087],
    ["15-关庄", "15-望京西", 2071],
    ["15-望京西", "15-望京", 1758],
    ["15-望京", "15-望京东", 1652],
    ["15-望京东", "15-崔各庄", 2295],
    ["15-崔各庄", "15-马泉营", 2008],
    ["15-马泉营", "15-孙河", 3309],
    ["15-孙河", "15-国展", 3386],
    ["15-国展", "15-花梨坎", 1615],
    ["15-花梨坎", "15-后沙峪", 3354],
    ["15-后沙峪", "15-南法信", 4576],
    ["15-南法信", "15-石门", 2712],
    ["15-石门", "15-顺义", 1331],
    ["15-顺义", "15-俸伯", 2441],
    ["BT-四惠", "BT-四惠东", 1715],  # BT 八通线
    ["BT-四惠东", "BT-高碑店", 1375],
    ["BT-高碑店", "BT-传媒大学", 2002],
    ["BT-传媒大学", "BT-双桥", 1894],
    ["BT-双桥", "BT-管庄", 1912],
    ["BT-管庄", "BT-八里桥", 1763],
    ["BT-八里桥", "BT-通州北苑", 1700],
    ["BT-通州北苑", "BT-果园", 1465],
    ["BT-果园", "BT-九棵树", 990],
    ["BT-九棵树", "BT-梨园", 1225],  # BT 八通线
    ["BT-梨园", "BT-临河里", 1257],
    ["BT-临河里", "BT-土桥", 776],
    ["DX-公益西桥", "DX-新宫", 2798],  # DX 大兴线
    ["DX-新宫", "DX-西红门", 5102],
    ["DX-西红门", "DX-高米店北", 1810],
    ["DX-高米店北", "DX-高米店南", 1128],
    ["DX-高米店南", "DX-枣园", 1096],
    ["DX-枣园", "DX-清源路", 1200],
    ["DX-清源路", "DX-黄村西大街", 1214],
    ["DX-黄村西大街", "DX-黄村火车站", 987],
    ["DX-黄村火车站", "DX-义和庄", 2035],
    ["DX-义和庄", "DX-生物医药基地", 2918],
    ["DX-生物医药基地", "DX-天宫院", 1811],
    ["YZ-宋家庄", "YZ-肖村", 2631],  # YZ 亦庄线
    ["YZ-肖村", "YZ-小红门", 1275],
    ["YZ-小红门", "YZ-旧宫", 2366],
    ["YZ-旧宫", "YZ-亦庄桥", 1982],
    ["YZ-亦庄桥", "YZ-亦庄文化园", 993],
    ["YZ-亦庄文化园", "YZ-万源街", 1728],
    ["YZ-万源街", "YZ-荣京东街", 1090],
    ["YZ-荣京东街", "YZ-荣昌东街", 1355],
    ["YZ-荣昌东街", "YZ-同济南路", 2337],
    ["YZ-同济南路", "YZ-经海路", 2301],
    ["YZ-经海路", "YZ-次渠南", 2055],
    ["YZ-次渠南", "YZ-次渠", 1281],
    ["CP-南邵", "CP-沙河高教园", 5357],  # CP 昌平线
    ["CP-沙河高教园", "CP-沙河", 1964],
    ["CP-沙河", "CP-巩华城", 2025],
    ["CP-巩华城", "CP-朱辛庄", 3799],
    ["CP-朱辛庄", "CP-生命科学园", 2367],
    ["CP-生命科学园", "CP-西二旗", 5440],
    ["FS-郭公庄", "FS-大葆台", 1405],  # FS 房山线
    ["FS-大葆台", "FS-稻田", 6466],
    ["FS-稻田", "FS-长阳", 4041],
    ["FS-长阳", "FS-篱笆房", 2150],
    ["FS-篱笆房", "FS-广阳城", 1474],
    ["FS-广阳城", "FS-良乡大学城北", 2003],
    ["FS-良乡大学城北", "FS-良乡大学城", 1188],
    ["FS-良乡大学城", "FS-良乡大学城西", 1738],
    ["FS-良乡大学城西", "FS-良乡南关", 1332],
    ["FS-良乡南关", "FS-苏庄", 1330]
]

transfer_dict = [
    ["1-复兴门", "2-复兴门", 110],  # 时间，s
    ["2-复兴门", "1-复兴门", 70],  # 时间，s
    ["1-建国门", "2-建国门", 70],  # 时间，s
    ["2-建国门", "1-建国门", 70],  # 时间，s
    ["1-西单", "4-西单", 110],  # 时间，s
    ["4-西单", "1-西单", 130],  # 时间，s
    ["1-东单", "5-东单", 120],  # 时间，s
    ["5-东单", "1-东单", 120],  # 时间，s
    ["1-军事博物馆", "9-军事博物馆", 110],  # 时间，s
    ["9-军事博物馆", "1-军事博物馆", 200],  # 时间，s
    ["1-公主坟", "10-公主坟", 60],  # 时间，s
    ["10-公主坟", "1-公主坟", 60],  # 时间，s
    ["1-国贸", "10-国贸", 120],  # 时间，s
    ["10-国贸", "1-国贸", 110],  # 时间，s
    ["1-大望路", "14E-大望路", 150],  # 时间，s
    ["14E-大望路", "1-大望路", 160],  # 时间，s
    ["2-西直门", "4-西直门", 10],  # 时间，s
    ["4-西直门", "2-西直门", 80],  # 时间，s
    ["2-西直门", "13-西直门", 190],  # 时间，s
    ["13-西直门", "2-西直门", 200],  # 时间，s
    ["4-西直门", "13-西直门", 140],  # 时间，s
    ["13-西直门", "4-西直门", 150],  # 时间，s
    ["1-四惠", "BT-四惠", 40],  # 时间，s
    ["BT-四惠东", "1-四惠东", 60],  # 时间，s
    ["2-宣武门", "4-宣武门", 30],  # 时间，s
    ["4-宣武门", "2-宣武门", 40],  # 时间，s
    ["2-雍和宫", "5-雍和宫", 40],  # 时间，s
    ["5-雍和宫", "2-雍和宫", 160],  # 时间，s
    ["2-崇文门", "5-崇文门", 90],  # 时间，s
    ["5-崇文门", "2-崇文门", 110],  # 时间，s
    ["2-车公庄", "6-车公庄", 70],  # 时间，s
    ["6-车公庄", "2-车公庄", 90],  # 时间，s
    ["2-朝阳门", "6-朝阳门", 70],  # 时间，s
    ["6-朝阳门", "2-朝阳门", 110],  # 时间，s
    ["2-鼓楼大街", "8-鼓楼大街", 110],  # 时间，s
    ["8-鼓楼大街", "2-鼓楼大街", 120],  # 时间，s
    ["2-东直门", "13-东直门", 260],  # 时间，s
    ["13-东直门", "2-东直门", 150],  # 时间，s
    ["4-平安里", "6-平安里", 120],  # 时间，s
    ["6-平安里", "4-平安里", 110],  # 时间，s
    ["4-菜市口", "7-菜市口", 60],  # 时间，s
    ["7-菜市口", "4-菜市口", 20],  # 时间，s
    ["4-国家图书馆", "9-国家图书馆", 10],  # 时间，s
    ["9-国家图书馆", "4-国家图书馆", 10],  # 时间，s
    ["4-海淀黄庄", "10-海淀黄庄", 30],  # 时间，s
    ["10-海淀黄庄", "4-海淀黄庄", 40],  # 时间，s
    ["4-角门西", "10-角门西", 70],  # 时间，s
    ["10-角门西", "4-角门西", 80],  # 时间，s
    ["4-北京南站", "14E-北京南站", 20],  # 时间，s
    ["14E-北京南站", "4-北京南站", 50],  # 时间，s
    ["4-西苑", "16-西苑", 110],  # 时间，s
    ["16-西苑", "4-西苑", 110],  # 时间，s
    ["5-东四", "6-东四", 120],  # 时间，s
    ["6-东四", "5-东四", 130],  # 时间，s
    ["5-磁器口", "7-磁器口", 50],  # 时间，s
    ["7-磁器口", "5-磁器口", 60],  # 时间，s
    ["5-惠新西街南口", "10-惠新西街南口", 20],  # 时间，s
    ["10-惠新西街南口", "5-惠新西街南口", 20],  # 时间，s
    ["5-宋家庄", "10-宋家庄", 30],  # 时间，s
    ["10-宋家庄", "5-宋家庄", 30],  # 时间，s
    ["5-宋家庄", "YZ-宋家庄", 30],  # 时间，s
    ["YZ-宋家庄", "5-宋家庄", 70],  # 时间，s
    ["10-宋家庄", "YZ-宋家庄", 70],  # 时间，s
    ["YZ-宋家庄", "10-宋家庄", 80],  # 时间，s
    ["5-立水桥", "13-立水桥", 60],  # 时间，s
    ["13-立水桥", "5-立水桥", 60],  # 时间，s
    ["5-蒲黄榆", "14E-蒲黄榆", 60],  # 时间，s
    ["14E-蒲黄榆", "5-蒲黄榆", 60],  # 时间，s
    ["5-大屯路东", "15-大屯路东", 140],  # 时间，s
    ["15-大屯路东", "5-大屯路东", 140],  # 时间，s
    ["6-南锣鼓巷", "8-南锣鼓巷", 50],  # 时间，s
    ["8-南锣鼓巷", "6-南锣鼓巷", 50],  # 时间，s
    ["6-白石桥南", "9-白石桥南", 40],  # 时间，s
    ["9-白石桥南", "6-白石桥南", 20],  # 时间，s
    ["6-慈寿寺", "10-慈寿寺", 50],  # 时间，s
    ["10-慈寿寺", "6-慈寿寺", 20],  # 时间，s
    ["6-呼家楼", "10-呼家楼", 20],  # 时间，s
    ["10-呼家楼", "6-呼家楼", 20],  # 时间，s
    ["6-金台路", "14E-金台路", 30],  # 时间，s
    ["14E-金台路", "6-金台路", 60],  # 时间，s
    ["7-北京西站", "9-北京西站", 20],  # 时间，s
    ["9-北京西站", "7-北京西站", 20],  # 时间，s
    ["7-九龙山", "14E-九龙山", 60],  # 时间，s
    ["14E-九龙山", "7-九龙山", 30],  # 时间，s
    ["8-北土城", "10-北土城", 40],  # 时间，s
    ["10-北土城", "8-北土城", 10],  # 时间，s
    ["8-霍营", "13-霍营", 110],  # 时间，s
    ["13-霍营", "8-霍营", 110],  # 时间，s
    ["8-奥林匹克公园", "15-奥林匹克公园", 160],  # 时间，s
    ["15-奥林匹克公园", "8-奥林匹克公园", 160],  # 时间，s
    ["8-朱辛庄", "CP-朱辛庄", 30],  # 时间，s
    ["CP-朱辛庄", "8-朱辛庄", 30],  # 时间，s
    ["9-六里桥", "10-六里桥", 10],  # 时间，s
    ["10-六里桥", "9-六里桥", 20],  # 时间，s
    ["9-七里庄", "14W-七里庄", 20],  # 时间，s
    ["14W-七里庄", "9-七里庄", 20],  # 时间，s
    ["9-郭公庄", "FS-郭公庄", 10],  # 时间，s
    ["FS-郭公庄", "9-郭公庄", 10],  # 时间，s
    ["10-知春路", "13-知春路", 130],  # 时间，s
    ["13-知春路", "10-知春路", 120],  # 时间，s
    ["10-芍药居", "13-芍药居", 100],  # 时间，s
    ["13-芍药居", "10-芍药居", 90],  # 时间，s
    ["10-西局", "14W-西局", 50],  # 时间，s
    ["14W-西局", "10-西局", 20],  # 时间，s
    ["10-十里河", "14E-十里河", 100],  # 时间，s
    ["14E-十里河", "10-十里河", 80],  # 时间，s
    ["13-望京西", "15-望京西", 160],  # 时间，s
    ["15-望京西", "13-望京西", 150],  # 时间，s
    ["13-西二旗", "CP-西二旗", 20],  # 时间，s
    ["CP-西二旗", "13-西二旗", 20],  # 时间，s
    ["14E-望京", "15-望京", 80],  # 时间，s
    ["15-望京", "14E-望京", 80]  # 时间，s
]


# 定义了换乘的时间和站与站的距离

# 定义了点包含本身地铁站和连接的地铁站
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


# 构建了地铁图，包含所有的地铁点
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class subway_gym:
    def __init__(self, start_key='9-北京西站', end_key='10-知春路'):
        g = Graph()
        vel = 10  # 地铁的速度 m/s
        for x in subway_dict:
            g.addEdge(x[0], x[1], (float)(x[2]) / vel)  # 由距离得到时间
            g.addEdge(x[1], x[0], (float)(x[2]) / vel)  # 双向都有
        for x in transfer_dict:
            g.addEdge(x[0], x[1], (float)(x[2]))  # 换站给的直接就是时间
        self.graph = g
        self.start = start_key
        self.state = self.start
        self.end = end_key

    def reset(self):
        self.state = self.start
        return self.start

    def step(self, action):
        ver = self.graph.getVertex(self.state)
        next_state = list(ver.getConnections())[action]
        reward = -ver.connectedTo[next_state]
        if next_state == self.end:
            reward = 1000
            is_done = True
        else:
            is_done = False
        self.state = next_state
        return self.state, reward, is_done, None


class RL:
    def __init__(self):
        self.my_env = subway_gym()
        self.allstate = self.my_env.graph.vertList
        self.exploreRate = 0.01
        self.gamma = 0.9
        for key in self.allstate.keys():
            ac_len = len(self.allstate[key].getConnections())
            self.allstate[key] = [self.allstate[key], 0]
        self.traj = []

    def choose_action(self, state):
        if np.random.binomial(1, self.exploreRate):
            return np.random.randint(len(self.allstate[state][0].getConnections()))
        else:
            nextall = self.allstate[state][0].connectedTo
            action = 0
            for i in range(1,len(nextall.keys())):
                s1 = list(nextall.keys())[i]
                s2 = list(nextall.keys())[action]
                t1 = -nextall[s1]+ self.gamma*self.allstate[s1][1]
                t2 = -nextall[s2]+ self.gamma*self.allstate[s2][1]
                if t1 > t2:
                    action = i
            return action

    def store(self, info):
        self.traj = info

    def learn(self):
        observation, action, reward, observation_next = self.traj
        temp = self.allstate[observation][1]
        self.allstate[observation][1] = reward + self.gamma*self.allstate[observation_next][1]
        return abs(temp-self.allstate[observation][1])


if __name__ == "__main__":

    env = subway_gym()
    algor = RL()
    for i in range(100):
        observation = env.reset()
        loss = 0
        while True:
            action = algor.choose_action(observation)
            observation_next, reward, is_done, info = env.step(action)
            algor.store((observation, action, reward, observation_next))
            loss += algor.learn()
            if is_done:
                break
            observation = observation_next
        print("第%d轮，损失是%f"%(i+1,loss))