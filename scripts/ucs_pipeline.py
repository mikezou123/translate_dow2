#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GAME_DEFS = {
    "dow2": {
        "name": "Dawn of War 2",
        "root": Path("Dawn of War 2"),
    },
    "retribution": {
        "name": "Dawn of War II - Retribution",
        "root": Path("Dawn of War II - Retribution"),
    },
}

ID_LINE = re.compile(r"^(\d+)\t(.*)$")
ASCII_WORD = re.compile(r"[A-Za-z]{3,}")

FINAL_REPLACEMENTS = (
    ("帝國衛隊士兵", "星界軍士兵"),
    ("帝國衛隊老兵", "星界軍老兵"),
    ("帝國衛隊防衛部隊", "星界軍防衛部隊"),
    ("帝國衛隊", "星界軍"),
    ("帝國防衛軍", "星界軍"),
    ("帝國衛兵", "星界軍士兵"),
    ("士官", "軍士"),
    ("無畏機兵", "無畏機甲"),
    ("電漿", "等離子"),
    ("飛彈", "導彈"),
    ("世界末日號", "阿米吉多頓號"),
    ("毀天滅地級攻擊巡洋艦", "阿米吉多頓號打擊巡洋艦"),
    ("毀天滅地", "阿米吉多頓"),
    ("末日決戰號", "阿米吉多頓號"),
    ("末日巡洋艦", "阿米吉多頓號"),
    ("末日戰艦", "阿米吉多頓號"),
    ("阿米吉多頓：", "阿米吉多頓號："),
    ("醫護指揮", "基因醫學主管"),
    ("哥迪恩", "戈迪安"),
    ("醫護中心", "醫療聖堂"),
    ("醫護裝甲", "藥劑庭裝甲"),
    ("醫護補給", "醫療補給"),
    ("戈迪安藥劑師會醫護塔庫斯的。", "戈迪安藥劑師會嘗試復活塔庫斯。"),
    ("蘇勒", "圖勒"),
    ("賽瑞斯", "賽勒斯"),
    ("異形靈化腦蟲", "靈能蟲"),
    ("異形蟲王頭目", "蟲巢暴君頭目"),
    ("異形蟲王", "蟲巢暴君"),
    ("異形王", "蟲巢暴君"),
    ("外星異形", "泰倫蟲族"),
    ("靈化腦蟲", "靈能蟲"),
    ("神靈術士", "術士"),
    ("冥靈君王", "幽冥領主"),
    ("冥靈君主", "幽冥領主"),
    ("冥靈護衛", "幽冥衛士"),
    ("冥靈大砲", "幽冥炮"),
    ("冥靈協同", "幽冥協同"),
    ("冥靈預視", "幽冥預視"),
    ("暗黑色軍團", "黑色軍團"),
    ("暗黑之神", "黑暗諸神"),
    ("腐敗之王", "納垢"),
    ("沙歷士", "色孽"),
    ("沙利士", "色孽"),
    ("鍛造之靈", "靈魂熔爐"),
    ("黑暗大師", "黑暗主人"),
    ("人類武聖", "凡人冠軍"),
    ("稀世珍寶", "奇異點"),
    ("D-型砲", "D 型砲"),
    ("文風不動", "固定式"),
    ("進行進行", "進行"),
    ("小隊小隊", "小隊"),
    ("的的", "的"),
    ("若搖動鏡頭的鏡頭", "若要平移鏡頭"),
    ("搖動鏡頭的鏡頭", "平移鏡頭"),
    ("毆克蠻人", "獸人"),
    ("裘納", "喬納"),
    ("防衛軍", "防衛部隊"),
    ("散彈槍", "霰彈槍"),
    ("太空陸戰隊", "星際戰士"),
    ("雷射炮", "激光炮"),
    ("雷射", "激光"),
    ("哇哈哈力量", "WAAAGH"),
    ("吼～之力", "WAAAGH"),
    ("阿斯塔特阿斯塔特", "阿斯塔特"),
    ("WAAAGH！點數", "WAAAGH 點數"),
    ("WAAAGH！的", "WAAAGH 的"),
    ("WAAAGH!", "WAAAGH！"),
    ("WAAAGH不足", "WAAAGH 不足"),
    ("獸人WAAAGH", "獸人 WAAAGH"),
    ("獲得WAAAGH", "獲得 WAAAGH"),
    ("使用WAAAGH", "使用 WAAAGH"),
    ("釋放WAAAGH", "釋放 WAAAGH"),
    ("引導WAAAGH", "引導 WAAAGH"),
    ("消耗WAAAGH", "消耗 WAAAGH"),
    ("強大的WAAAGH", "強大的 WAAAGH"),
    ("困在WAAAGH中", "困在 WAAAGH 中"),
    ("WAAAGH震撼", "WAAAGH 震撼"),
    ("WAAAGH的力量", "WAAAGH 的力量"),
    ("WAAAGH！。", "WAAAGH！"),
    ("艾小隊頓", "阿巴頓"),
    ("艾班頓", "阿巴頓"),
    ("藉由攻擊與殺害你的敵人可獲得 WAAAGH！", "透過戰鬥並殺死敵人來獲得 WAAAGH！"),
    ("引導 WAAAGH，使鄰近的所有小子們速度更快，且更不易被殺害。", "引導 WAAAGH 的力量，使附近所有小子移動更快，也更難被殺死。"),
    ("釋放 WAAAGH 震撼鄰近敵人", "釋放 WAAAGH 的力量震暈附近敵人"),
    ("劇本【%2SCENARIO%」", "劇本「%2SCENARIO%」"),
    ("Direct X", "DirectX"),
    ("遊戲主機端", "主機"),
    ("勝利點優勝條件", "勝利點勝利條件"),
    ("侵略者坦克", "掠食者坦克"),
    ("魔法飛彈", "魔法導彈"),
    ("側擊獸人", "側翼包抄獸人"),
    ("進行側擊", "從側翼包抄"),
    ("展開側擊", "從側翼包抄"),
    ("對他們進行側擊", "從側翼包抄他們"),
    ("另頭的防禦較少", "另一個入口的防禦可能較弱"),
    ("耗費大量的數目", "大口吞噬"),
    ("取得最後勝利", "贏得最終勝利"),
    ("獠牙老大", "豬牙老大"),
    ("終結者戰略兵", "終結者戰術兵"),
    ("星際戰略兵", "戰術星際戰士"),
    ("戰略兵", "戰術兵"),
    ("小隊：指揮官、戰術兵、突進、", "小隊：指揮官、戰術兵、突擊兵、"),
    ("成就：第一個同步殺害", "成就：首次同步擊殺"),
    ("同步殺害", "同步擊殺"),
    ("殺害泰倫巨獸小隊", "擊殺泰倫蟲族岡特蟲小隊"),
    ("已殺害部隊", "已擊殺單位"),
    ("已殺害指揮官", "已擊殺指揮官"),
    ("已殺害人數", "已擊殺步兵"),
    ("已殺害電力據點", "已摧毀電力據點"),
    ("已殺害了", "已擊殺"),
    ("已殺害", "已擊殺"),
    ("泰倫蟲族劊子手頭目", "泰倫蟲族卡尼菲克斯首領"),
    ("泰倫蟲族劊子手", "泰倫蟲族卡尼菲克斯"),
    ("劊子手頭目", "卡尼菲克斯首領"),
    ("劊子手蟲", "卡尼菲克斯"),
    ("異端劊子手", "異端卡尼菲克斯"),
    ("劊子手", "卡尼菲克斯"),
    ("強盜小子", "掠奪小子"),
    ("死亡機兵", "死無畏"),
    ("贓車坦克", "掠奪坦克"),
    ("傳送蛛司戰", "躍遷蜘蛛司戰"),
    ("傳送蛛聖殿", "躍遷蜘蛛聖殿"),
    ("傳送蛛神殿", "躍遷蜘蛛神殿"),
    ("傳送蛛道途", "躍遷蜘蛛道途"),
    ("傳送蛛裝甲", "躍遷蜘蛛裝甲"),
    ("傳送蛛小隊", "躍遷蜘蛛小隊"),
    ("傳送蛛頭目", "躍遷蜘蛛頭目"),
    ("傳送蛛英雄", "躍遷蜘蛛英雄"),
    ("傳送蛛甲", "躍遷蜘蛛甲"),
    ("傳送蛛", "躍遷蜘蛛"),
    ("利卡特原體", "利卡特首領"),
    ("吞噬蟲原體", "掘蟒蟲首領"),
    ("D 型砲武器組", "D 型砲武器小組"),
    ("解除D 型砲", "解鎖 D 型砲"),
    ("星際戰略爆彈槍小隊", "戰術星際戰士爆彈槍小隊"),
    ("解除D 型砲升級鎖定", "解鎖 D 型砲升級"),
    ("解除D型砲升級鎖定", "解鎖 D 型砲升級"),
    ("解除步兵升級鎖定", "解鎖步兵升級"),
    ("解除命運技能鎖定", "解鎖命運技能"),
    ("首腦靈能", "突觸"),
    ("給與先知", "賦予先知"),
    ("補賦予", "補給與"),
    ("科技戰士用有", "技術軍士擁有"),
    ("能有效的", "能有效"),
    ("暫時的", "暫時"),
    ("致並的", "致命的"),
    ("技術軍士用有", "技術軍士擁有"),
    ("通道已供", "通道以供"),
    ("睜大眼睛眼", "睜大眼睛"),
    ("另附近的部隊不能移動", "使附近部隊無法移動"),
    ("另一個攻擊可能會造成致命的一擊", "再一次攻擊可能造成致命一擊"),
    ("這將不會在另一場攻擊中生存下來", "它撐不過下一次攻擊"),
    ("你嚴重地傷害它。另一個攻擊將會殺了它", "你已重創它。再一次攻擊就能殺死它"),
    ("時間空間", "時間力場"),
    ("工藝世界", "方舟世界"),
    ("靈魂之石", "靈魂石"),
    ("焰晶大砲", "火棱炮"),
    ("焰晶攻擊", "火棱攻擊"),
    ("焰晶坦克", "火棱坦克"),
    ("焰晶", "火棱坦克"),
    ("戰道神龕", "戰道神殿"),
    ("鈦星人", "鈦族"),
    ("鈦種族", "鈦族"),
    ("烈火(烈火階級)", "火氏族（火氏）"),
    ("烈火階級", "火氏族"),
    ("大地(大地階級)", "土氏族（土氏）"),
    ("大地階級", "土氏族"),
    ("沅水(沅水階級)", "水氏族（水氏）"),
    ("沅水階級", "水氏族"),
    ("以鈦(以鈦階級)", "以太（以太氏族）"),
    ("以鈦階級", "以太氏族"),
    ("乙鈦階級", "以太氏族"),
    ("烈火及沅水", "火氏族和水氏族"),
    ("卅部鈦族", "三十輛鈦族"),
    ("鈦的裝甲部隊", "鈦族裝甲縱隊"),
    ("以鈦", "以太"),
    ("棍子炸彈棍", "棒槌炸彈"),
    ("棍子炸彈小子", "棒槌炸彈小子"),
    ("棍子炸彈隊", "棒槌炸彈小子"),
    ("棍子炸彈", "棒槌炸彈"),
    ("老大領導", "老大頭領"),
    ("大號獸人槍", "大槍"),
    ("瞄準？瞄什麼鬼？", "瞄準？那是啥？"),
    ("近戰隊伍", "近戰部隊"),
    ("高亮度", "高亮"),
    ("治療目標隊伍", "治療目標小隊"),
    ("敵人隊伍", "敵方小隊"),
    ("你的隊伍", "你的小隊"),
    ("支援的戰爭物資", "補給戰爭裝備"),
    ("部署瞄什麼鬼", "部署「瞄準？那是啥？」"),
    ("給予藥劑師更多的能量與能量值自然恢復", "提高藥劑師能量與能量恢復"),
    ("生命值自然恢復", "生命恢復"),
    ("能量值自然恢復", "能量恢復"),
    ("生命值自然回復", "生命恢復"),
    ("能量值自然回復", "能量恢復"),
    ("給予藥劑師更多的能量與能量值自然回復", "提高藥劑師能量與能量恢復"),
    ("動力資源", "電力資源"),
    ("需要 %1AMOUNT% 動力", "需要 %1AMOUNT% 電力"),
    ("取得軔性", "取得韌性"),
    ("軔性", "韌性"),
    ("加值", "加成"),
    ("部屬", "部署"),
    ("布署", "部署"),
    ("戰爭物件", "戰爭裝備"),
    ("砍刀小子", "砍砍小子"),
    ("老大頭領增加手槍部隊的近戰傷害", "老大頭領提高砍砍小子的近戰傷害"),
    ("老大頭領增加砍砍小子的近戰傷害", "老大頭領提高砍砍小子的近戰傷害"),
    ("裝備手槍或砍刀的近戰部隊", "裝備手槍和砍刀的近戰部隊"),
    ("升級成持用火焰噴射器", "升級火焰噴射器"),
    ("升級持用火焰噴射器", "升級火焰噴射器"),
    ("贓車掠食者", "掠奪掠食者"),
    ("火氏族和水氏族", "火氏族與水氏族"),
    ("瘋狂技師", "瘋狂技霸"),
    ("與瘋狂技霸修補", "由瘋狂技霸拼湊而成"),
    ("嚎叫女妖神官", "嚎叫女妖司戰"),
    ("躍遷蜘蛛神官", "躍遷蜘蛛司戰"),
    ("黑暗神靈", "黑暗靈族"),
    ("神靈先知", "靈族先知"),
    ("神靈哈維坦克", "異族浮空坦克"),
    ("靈能者大師", "靈能大師"),
    ("獸人技師小子", "獸人技霸小子"),
    ("技師小子", "技霸小子"),
    ("技師裝甲", "技霸裝甲"),
    ("科技牧師", "技術神甫"),
    ("天文觀測站", "天文陣列"),
    ("天文收發站", "天文陣列"),
    ("觀測站", "陣列"),
    ("獸人技師", "獸人技霸"),
    ("技師布利札嘎", "技霸布利札嘎"),
    ("此陣列可以辨認泰倫蟲巢艦隊的弱點", "這座陣列能找出泰倫蟲族蟲巢艦隊的弱點"),
    ("攝影機", "鏡頭"),
    ("傷害力", "傷害"),
    ("防禦力", "防禦"),
    ("異形艦隊", "泰倫蟲族艦隊"),
    ("異形入侵", "泰倫蟲族入侵"),
    ("異形活動", "泰倫蟲族活動"),
    ("異形部隊", "泰倫蟲族部隊"),
    ("異形生物", "泰倫蟲族生物"),
    ("異形任務", "泰倫蟲族任務"),
    ("異形侵擾", "泰倫蟲族侵擾"),
    ("異形敵人", "泰倫蟲族敵人"),
    ("異形翼蟲", "泰倫翼蟲"),
    ("異形兵蟲", "泰倫兵蟲"),
    ("異形原始基因樣本", "泰倫蟲族原始基因樣本"),
    ("異形生化炮台", "泰倫蟲族生化炮台"),
    ("異形毛細塔", "蟲族毛細塔"),
    ("奧雷利亞區", "奧雷利亞次星區"),
    ("奧雷利亞防區", "奧雷利亞次星區"),
    ("防區", "星區"),
    ("泰芬", "泰豐"),
    ("卡德里斯", "卡德利斯"),
    ("美里迪恩", "梅里迪安"),
    ("戴維恩‧圖勒", "戴維安·圖勒"),
    ("戴維恩・圖勒", "戴維安·圖勒"),
    ("戴維恩·圖勒", "戴維安·圖勒"),
    ("ping 值", "延遲值"),
    ("Ping 值", "延遲值"),
    ("依 Ping", "依延遲"),
    ("按 ping", "按延遲"),
    ("Ping/效能", "延遲/效能"),
    ("shader model", "著色器模型"),
    ("Shader Model", "著色器模型"),
    ("Shader 3.0 模式", "著色器 3.0 模式"),
    ("Shader 顯示增強", "著色器顯示增強"),
    ("Shader 品質", "著色器品質"),
    ("高階Shader品質", "高階著色器品質"),
    ("蠻荒蠻荒獸人", "獸人"),
    ("蠻荒獸人", "獸人"),
    ("野蠻獸人", "獸人"),
    ("蟲巢太空船", "蟲巢艦"),
    ("太空港口", "太空港"),
    ("終極改造戰士", "基因原體"),
    ("暗黑聖戰", "黑暗聖戰"),
    ("次元的能量", "亞空間能量"),
    ("卡爾德里斯", "卡德利斯"),
    ("卡德利", "卡德利斯"),
    ("卡德利斯斯", "卡德利斯"),
    ("阿瑪吉頓", "阿米吉多頓"),
    ("阿古斯", "阿格斯"),
    ("戴維恩·蘇勒", "戴維安·圖勒"),
    ("戴維恩‧蘇勒", "戴維安·圖勒"),
    ("安吉洛斯", "安傑羅斯"),
    ("加百列‧安傑羅", "加百列·安傑羅斯"),
    ("加百列·安傑羅 ", "加百列·安傑羅斯 "),
    ("安傑羅連長", "安傑羅斯連長"),
    ("安傑羅通話完畢", "安傑羅斯通話完畢"),
    ("安傑羅斯", "安傑洛斯"),
    ("加百列·安傑羅和", "加百列·安傑洛斯和"),
    ("加百列·安傑羅、", "加百列·安傑洛斯、"),
    ("安傑羅", "安傑洛斯"),
    ("科技戰士", "技術軍士"),
    ("死靈族", "太空死靈"),
    ("外星異族", "異族"),
    ("異星人", "異族"),
    ("防衛區", "星區"),
    ("薩德斯", "撒迪厄斯"),
    ("賽迪斯", "撒迪厄斯"),
    ("薩迪斯", "撒迪厄斯"),
    ("迪奥梅帝斯", "迪奧梅德斯"),
    ("迪奧梅帝斯", "迪奧梅德斯"),
    ("迪奥梅蒂斯", "迪奧梅德斯"),
    ("迪奧梅蒂斯", "迪奧梅德斯"),
    ("麥瑞克", "梅里克"),
    ("馬爾特魯斯", "馬特勒斯"),
    ("提生", "提升"),
    ("其它", "其他"),
    ("回復", "恢復"),
    ("無行為能力", "失去戰鬥能力"),
    ("特殊保護", "無敵效果"),
    ("喬納‧歐里恩", "喬納·奧賴恩"),
    ("喬納・歐里恩", "喬納·奧賴恩"),
    ("喬納·歐里恩", "喬納·奧賴恩"),
    ("克諾努斯", "克羅努斯"),
    ("馬蒂亞斯港", "馬提亞斯港"),
    ("第二次世界末日大戰", "第二次阿米吉多頓戰爭"),
    ("第三次世界末日大戰", "第三次阿米吉多頓戰爭"),
    ("第一次世界末日大戰", "第一次阿米吉多頓戰爭"),
    ("世界末日第一次大戰", "第一次阿米吉多頓戰爭"),
    ("安格昂", "安格隆"),
    ("阿法軍團", "阿爾法軍團"),
    ("阿爾法戰團", "阿爾法軍團"),
    ("帝國近衛兵", "星界軍"),
    ("近衛兵", "星界軍士兵"),
    ("突進跳躍", "突擊跳躍"),
    ("加乘", "加成"),
    ("參予", "參與"),
    ("強軔", "強韌"),
    ("火蜥蝪", "火蜥蜴"),
    ("鈦的戰鬥部隊", "鈦族戰鬥部隊"),
    ("鈦軍", "鈦族"),
    ("靈能機關槍", "靈能箭"),
    ("重型機關槍砲台", "重型爆彈槍砲台"),
    ("狂風爆彈槍", "風暴爆彈槍"),
    ("墮落機關槍", "腐化爆彈槍"),
    ("機關槍", "爆彈槍"),
    ("死亡兄弟", "陣亡兄弟"),
    ("需要重型武器開啟", "需要重型武器解鎖"),
    ("武器技能開啟", "武器技能解鎖"),
    ("技能開啟", "技能解鎖"),
    ("能力開啟", "能力解鎖"),
    ("武器開啟", "武器解鎖"),
    ("得到技能", "獲得技能"),
    ("得到裝備", "獲得裝備"),
    ("可使用於", "可用於"),
    ("安傑洛斯上尉", "安傑洛斯連長"),
    ("安潔羅上尉", "安傑洛斯連長"),
    ("迪奧梅德斯上尉", "迪奧梅德斯連長"),
    ("波里爾上尉", "波里爾連長"),
    ("榮譽護衛上尉", "榮譽護衛連長"),
    ("血鴉上尉", "血鴉連長"),
    ("兄弟上尉", "兄弟連長"),
    ("戴維安·圖勒上尉", "戴維安·圖勒連長"),
    ("鴉衛第八連上尉", "鴉衛第八連連長"),
    ("血鴉第三連上尉", "血鴉第三連連長"),
    ("傀儡上尉", "傀儡連長"),
    ("一名上尉針對", "一名連長針對"),
    ("一名上尉做出", "一名連長做出"),
    ("上尉是星際戰士", "連長是星際戰士"),
    ("上尉遭到", "連長遭到"),
    ("上尉在每次", "連長在每次"),
    ("使上尉", "使連長"),
    ("上尉，", "連長，"),
    ("，上尉", "，連長"),
    ("上尉。", "連長。"),
    ("上尉？", "連長？"),
    ("上尉！", "連長！"),
    ("上尉…", "連長…"),
    ("阿德拉斯蒂亞", "阿德拉提雅"),
    ("艾雷那‧德羅莎", "埃琳娜·德羅莎"),
    ("艾雷那·德羅莎", "埃琳娜·德羅莎"),
    ("艾雷那‧迪羅沙", "埃琳娜·德羅莎"),
    ("艾雷那德羅沙", "埃琳娜·德羅莎"),
    ("艾雷那", "埃琳娜"),
    ("迪羅沙", "德羅莎"),
    ("德羅沙", "德羅莎"),
    ("艾琳娜·德羅莎", "埃琳娜·德羅莎"),
    ("凡迪斯", "范迪斯"),
    ("爆彈槍架十字弓", "爆彈樁弩"),
    ("MK Iva", "MK IVa"),
    ("戴諾斯", "戴莫斯"),
    ("葛瓦沙", "戈瓦札"),
    ("戈瓦扎", "戈瓦札"),
    ("戴夫‧跩瓦", "死駕"),
    ("戴夫·跩瓦", "死駕"),
    ("布里薩加", "布利札嘎"),
    ("布利扎加", "布利札嘎"),
    ("裂砍", "殘虐裂手"),
    ("利帕-斯普利塔", "殘虐裂手"),
    ("瑞帕-斯普利塔", "殘虐裂手"),
    ("戴夫跩瓦", "死駕"),
    ("死亡駕駛", "死駕"),
    ("葛林杜夫峽谷", "綠牙峽谷"),
    ("坦克車", "坦克"),
    ("您們", "你們"),
    ("星際戰士人員", "星際戰士"),
    ("星際戰士員", "星際戰士"),
    ("哨兵軍士", "偵察兵軍士"),
    ("哨兵小隊", "偵察兵小隊"),
    ("哨兵盔甲", "偵察兵裝甲"),
    ("哨兵裝甲", "偵察兵裝甲"),
    ("哨兵卡羅裝束", "偵察兵卡羅裝束"),
    ("哨兵寂靜天使", "偵察兵寂靜天使"),
    ("血鴉哨兵", "血鴉偵察兵"),
    ("哨兵、暗殺者", "偵察兵、刺客"),
    ("擔任哨兵的新兵", "擔任偵察兵的新兵"),
    ("擔任哨兵軍士", "擔任偵察兵軍士"),
    ("哨兵新兵", "偵察兵新兵"),
    ("疣豬運兵車", "剃刀背運兵車"),
    ("疣豬", "剃刀背"),
    ("剃刀鯨", "剃刀背"),
    ("新進者", "新兵"),
    ("新血", "新兵"),
    ("普萊安", "普里阿姆"),
    ("阿茲塔戰團", "阿斯塔特修會"),
    ("阿茲塔", "阿斯塔特"),
    ("阿比提思樣式", "仲裁庭型"),
    ("阿比提思MKIX", "仲裁庭 MK IX"),
    ("滲透的哨兵", "滲透的偵察兵"),
    ("滲透的偵察小隊", "滲透的偵察兵小隊"),
    ("偵察小隊", "偵察兵小隊"),
    ("卡莫斗篷", "偽裝斗篷"),
    ("無名哨兵", "無名偵察兵"),
    ("其他帝皇戰士", "帝皇麾下其他戰士"),
    ("進行殺害", "完成擊殺"),
    ("網絡聯集", "網道樞紐"),
    ("網絡傳送門", "網道傳送門"),
    ("網道集會所", "網道樞紐"),
    ("網道組件", "網道樞紐"),
    ("網道門", "網道傳送門"),
    ("燄晶坦克", "火棱坦克"),
    ("火稜鏡", "火棱坦克"),
    ("蓋恩聖者", "凱恩化身"),
    ("和化身", "和凱恩化身"),
    ("D型砲", "D 型砲"),
    ("解除火棱坦克，D 型砲武器與凱恩化身鎖定", "解鎖火棱坦克、D 型砲武器小組與凱恩化身"),
    ("混沌滅絕者小隊", "混沌浩劫小隊"),
    ("滅絕者小隊", "浩劫小隊"),
    ("滅絕者", "浩劫者"),
    ("10五", "15"),
    ("生化等離子", "生體等離子"),
    ("靈能網絡", "靈能網路"),
    ("蟲王護衛", "暴君守衛"),
    ("卡尼菲克", "卡尼菲克斯"),
    ("卡尼菲克斯斯", "卡尼菲克斯"),
    ("特馬根蟲群", "槍蟲群"),
    ("特馬根", "槍蟲"),
    ("賀馬根蟲群", "刀蟲群"),
    ("賀馬根蟲", "刀蟲"),
    ("賀馬根", "刀蟲"),
    ("槍蟲蟲", "槍蟲"),
    ("刀蟲蟲", "刀蟲"),
    ("菁英", "精英"),
    ("網絡", "網路"),
    ("突觸網路核心處的結。", "突觸網路核心處的節點。"),
    ("帝羅莎", "德羅莎"),
    ("安提司", "安提亞斯"),
    ("亞薩利亞", "阿扎賴亞"),
    ("‧", "·"),
    ("戰團長暨", "戰團長兼"),
    ("首席智庫暨", "首席智庫兼"),
    ("智庫守護者", "智庫館長"),
    ("。。", "。"),
    ("亞拉哈斯t-", "亞拉哈斯 - "),
    ("  - ", " - "),
    (" -  ", " - "),
    ("掃瞄", "掃描"),
    ("異形生化砲台", "泰倫蟲族生體砲台"),
    ("泰倫蟲族生物炮塔", "泰倫蟲族生體砲台"),
    ("疫病武聖", "疫病冠軍"),
    ("混沌武聖", "混沌冠軍"),
    ("野心武聖", "野心冠軍"),
    ("納垢武聖", "納垢冠軍"),
    ("仲裁庭型III", "仲裁庭 III 型"),
    ("仲裁庭型V", "仲裁庭 V 型"),
    ("MK IX霰彈槍", "MK IX 霰彈槍"),
    ("阿提加", "奧爾特加"),
    ("帕弗尼", "帕沃尼斯"),
    ("阿維圖思", "阿維圖斯"),
    ("機乎", "幾乎"),
    ("發佈", "發布"),
    ("開起", "開啟"),
    ("集節點", "集結點"),
    ("搖控", "遙控"),
    ("萊吉斯巢都尖塔", "萊吉斯居住尖塔"),
    ("維尼克圖斯巢都尖塔", "維尼克圖斯居住尖塔"),
)


def resolve_path(value: str | Path) -> Path:
    return Path(value).expanduser().resolve()


def project_root(args: argparse.Namespace) -> Path:
    if args.project_root:
        return resolve_path(args.project_root)
    return resolve_path(args.process_root) / "translation_project"


def glossary_path(args: argparse.Namespace) -> Path:
    if args.glossary:
        return resolve_path(args.glossary)
    return ROOT / "glossary" / "mainland_40k_tw.tsv"


def overrides_path(args: argparse.Namespace) -> Path:
    if args.overrides:
        return resolve_path(args.overrides)
    return project_root(args) / "work" / "manual_overrides.tsv"


def games(args: argparse.Namespace) -> dict[str, dict[str, Path | str]]:
    process_root = resolve_path(args.process_root)
    result: dict[str, dict[str, Path | str]] = {}
    for key, meta in GAME_DEFS.items():
        game_root = process_root / meta["root"]
        result[key] = {
            "name": meta["name"],
            "en": game_root / "Locale" / "English" / "DOW2.ucs",
            "zh": game_root / "Locale" / "TChinese" / "DOW2.ucs",
        }
    return result


def read_ucs(path: Path) -> OrderedDict[str, str]:
    entries: OrderedDict[str, str] = OrderedDict()
    with path.open("r", encoding="utf-16") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.rstrip("\r\n")
            if not line:
                continue
            match = ID_LINE.match(line)
            if not match:
                continue
            entries[match.group(1)] = match.group(2)
    return entries


def write_ucs(path: Path, entries: OrderedDict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-16", newline="\r\n") as handle:
        for key, value in entries.items():
            handle.write(f"{key}\t{value}\n")


def read_glossary(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def apply_avoid_replacements(text: str, glossary: list[dict[str, str]]) -> str:
    result = text
    for row in glossary:
        preferred = row.get("preferred_tw", "").strip()
        avoid = row.get("avoid_tw", "").strip()
        if not preferred or not avoid:
            continue
        avoid_terms = sorted(
            [item.strip() for item in avoid.split(";") if item.strip()],
            key=len,
            reverse=True,
        )
        for bad in avoid_terms:
            # Avoid automatic substring expansion such as 泰倫蟲族 -> 泰倫蟲族蟲族.
            # These still appear in term-report for human review.
            if bad == preferred or bad in preferred:
                continue
            result = result.replace(bad, preferred)
    return result


def apply_final_replacements(text: str) -> str:
    result = text
    for old, new in FINAL_REPLACEMENTS:
        result = result.replace(old, new)
    result = re.sub(r"(?<=[\u4e00-\u9fff])!", "！", result)
    result = re.sub(r"!(?=[\u4e00-\u9fff])", "！", result)
    return result


def classify(en_text: str, zh_text: str | None) -> str:
    if zh_text is None:
        return "missing_in_tchinese"
    if zh_text == en_text:
        return "same_as_english"
    if ASCII_WORD.search(zh_text):
        return "contains_ascii"
    return "has_tchinese"


def cmd_report(args: argparse.Namespace) -> None:
    rows = []
    for key, meta in games(args).items():
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        missing = [item for item in en if item not in zh]
        extra = [item for item in zh if item not in en]
        same = [item for item in en if item in zh and en[item] == zh[item]]
        ascii_rows = [item for item in en if item in zh and ASCII_WORD.search(zh[item])]
        rows.append({
            "game_key": key,
            "game": meta["name"],
            "english_ids": len(en),
            "tchinese_ids": len(zh),
            "missing_in_tchinese": len(missing),
            "extra_in_tchinese": len(extra),
            "same_as_english": len(same),
            "contains_ascii": len(ascii_rows),
            "first_missing_ids": ", ".join(missing[:20]),
        })

    out = project_root(args) / "reports" / "coverage.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def cmd_export(args: argparse.Namespace) -> None:
    glossary = read_glossary(glossary_path(args))
    all_games = games(args)
    targets = all_games.keys() if args.game == "all" else [args.game]
    for key in targets:
        meta = all_games[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        out = project_root(args) / "work" / f"{key}_translation.tsv"
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8-sig", newline="") as handle:
            fields = ["id", "status", "en", "zh_current", "zh_new", "notes"]
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            for text_id, en_text in en.items():
                zh_current = zh.get(text_id, "")
                zh_suggested = apply_avoid_replacements(zh_current, glossary) if zh_current else ""
                writer.writerow({
                    "id": text_id,
                    "status": classify(en_text, zh_current if text_id in zh else None),
                    "en": en_text,
                    "zh_current": zh_current,
                    "zh_new": zh_suggested if zh_suggested != zh_current else "",
                    "notes": "",
                })
        print(out)


def cmd_build(args: argparse.Namespace) -> None:
    all_games = games(args)
    targets = all_games.keys() if args.game == "all" else [args.game]
    manual_overrides: dict[tuple[str, str], str] = {}
    manual_by_source: dict[str, str] = {}
    manual_path = overrides_path(args)
    if manual_path.exists():
        with manual_path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                value = row.get("zh_new", "")
                if value:
                    game_key = row.get("game_key", "")
                    text_id = row.get("id", "")
                    source = row.get("en", "")
                    if game_key and text_id:
                        manual_overrides[(game_key, text_id)] = value
                    if source:
                        manual_by_source[source] = value

    for key in targets:
        meta = all_games[key]
        en = read_ucs(meta["en"])
        zh = read_ucs(meta["zh"])
        work = project_root(args) / "work" / f"{key}_translation.tsv"
        overrides: dict[str, str] = {}
        if work.exists():
            with work.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle, delimiter="\t"):
                    value = row.get("zh_new", "")
                    if value:
                        overrides[row["id"]] = value

        output = OrderedDict()
        for text_id, en_text in en.items():
            if (key, text_id) in manual_overrides:
                output[text_id] = manual_overrides[(key, text_id)]
            elif ("all", text_id) in manual_overrides:
                output[text_id] = manual_overrides[("all", text_id)]
            elif en_text in manual_by_source:
                output[text_id] = manual_by_source[en_text]
            elif text_id in overrides:
                output[text_id] = overrides[text_id]
            elif text_id in zh:
                output[text_id] = zh[text_id]
            elif args.fill_missing == "english":
                output[text_id] = en_text
            else:
                output[text_id] = ""

            output[text_id] = apply_final_replacements(output[text_id])

        out = project_root(args) / "output" / key / "Locale" / "TChinese" / "DOW2.ucs"
        write_ucs(out, output)
        print(out)


def cmd_term_report(args: argparse.Namespace) -> None:
    glossary = read_glossary(glossary_path(args))
    rows = []
    for key, meta in games(args).items():
        zh = read_ucs(meta["zh"])
        for text_id, text in zh.items():
            for term in glossary:
                preferred = term.get("preferred_tw", "").strip()
                avoid = term.get("avoid_tw", "").strip()
                if not avoid:
                    continue
                for bad in [item.strip() for item in avoid.split(";") if item.strip()]:
                    if bad and bad != preferred and bad in text:
                        rows.append({
                            "game_key": key,
                            "id": text_id,
                            "avoid_tw": bad,
                            "preferred_tw": preferred,
                            "text": text,
                        })

    out = project_root(args) / "reports" / "term_risks.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["game_key", "id", "avoid_tw", "preferred_tw", "text"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dawn of War II UCS translation pipeline")
    default_process_root = os.environ.get("DOW2_PROCESS_ROOT", str(ROOT.parent))
    parser.add_argument(
        "--process-root",
        default=default_process_root,
        help="Local folder that contains the copied game folders, for example I:\\translate_process.",
    )
    parser.add_argument(
        "--project-root",
        default=None,
        help="Local folder for reports/work/output. Defaults to <process-root>\\translation_project.",
    )
    parser.add_argument(
        "--glossary",
        default=None,
        help="Optional glossary TSV path. Defaults to glossary/mainland_40k_tw.tsv in this repository.",
    )
    parser.add_argument(
        "--overrides",
        default=None,
        help="Optional manual overrides TSV. Defaults to <project-root>\\work\\manual_overrides.tsv.",
    )
    sub = parser.add_subparsers(required=True)

    report = sub.add_parser("report")
    report.set_defaults(func=cmd_report)

    export = sub.add_parser("export")
    export.add_argument("--game", choices=["all", *GAME_DEFS.keys()], default="all")
    export.set_defaults(func=cmd_export)

    build = sub.add_parser("build")
    build.add_argument("--game", choices=["all", *GAME_DEFS.keys()], default="all")
    build.add_argument("--fill-missing", choices=["english", "blank"], default="english")
    build.set_defaults(func=cmd_build)

    term_report = sub.add_parser("term-report")
    term_report.set_defaults(func=cmd_term_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
