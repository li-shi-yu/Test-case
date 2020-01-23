# -*- encoding=utf8 -*-
__author__ = "shiyu.li"

import sys
sys.path.append('/Users/shiyu.li/.jenkins/workspace/test/ride.air/ride.py)
from common import *

scooterNo = os.getenv("scooterNo")

arr = [
    {
        "type":"click",
        "element":"scan_to_unlock",
        "assert":{
            "img":"tpl1579585539562.png"  
                 },
        "click":{
            "value":"com.zen.zbike:id/button_scan_to_unlock"
        }
    },
    {
        "type":"permisson_allow",
        "element":"permisson_camera",
        "assert":{
            "allow": "tpl1579585793615.png"
        },
         "click":{
           "value":"com.android.packageinstaller:id/permission_allow_button",
        }
    },
    {
        "type":"click",
        "element":"input_scooterNo_button",
        "assert":{
            "img":"tpl1579585946910.png"
        },
        "click":{
            "value":"com.zen.zbike:id/button_input_number"
        }
    },
    {
        "type":"click",
        "element":"scooterNo_inputbox",
         "assert":{
            "img": "tpl1579587002625.png"
        },
        "click":{
            "value":"com.zen.zbike:id/bike_number_edit_text"
        }
    },
    {
        "type":"sendText",
        "element":"scooterNo",
        "assert":{
            "img":"tpl1579587273324.png"
        },
        "sendText":{
            "value":"com.zen.zbike:id/bike_number_edit_text",
            "text":scooterNo
        }
    },
    {
        "type":"click",
        "element":"unlock",
        "assert":{
            "img":"tpl1579587318998.png"
        },
        "click":{
            "value":"com.zen.zbike:id/button_unlock"
        }
    },
    {
        "type":"notice",
        "element":"unlock_failed",
        "assert":{
            "unlock_failed":"tpl1579592455098.png"
        },
        "click":
        {
            "value":"android.widget.LinearLayout"
        }
    },
    {
        "type":"click",
        "element":"how_to_ride",
        "assert":{
            "img":"tpl1579587590905.png"
        },
        "click":{
            "value":"com.zen.zbike:id/got_view"
        }
    },
    {
        "type":"sleep",
        "time":90
    },
    {
        "type":"click",
        "element":"lock",
        "assert":{
            "duration":"tpl1579587867601.png",
            "cost":"tpl1579587874787.png"
        },
        "click":{
            "value":"com.zen.zbike:id/end_to_ride_btn"
        }
    },
    {
        "type":"click",
        "element":"park_got_it",
        "assert":{
            "img":"tpl1579588771290.png"
        },
        "click":{
            "value":"com.zen.zbike:id/got_view"
        }
    },
    {
        "type":"sleep",
        "time":15
    },
    {
        "type":"permisson_allow",
        "element":"permisson_phtots",
        "assert":{
            "folder": "tpl1579588909789.png"
        },
         "click":{
           "value":"com.android.packageinstaller:id/permission_allow_button",
        }
    },
    {
        "type":"click",
        "element":"take_photo",
        "assert":{
            "img":"tpl1579593043881.png"
        },
        "click":{            
          "value":"com.zen.zbike:id/button_back"
        }
    },
    {
        "type":"rate_us",
        "element":"rate_us",
        "assert":{
            "img":"tpl1579589165493.png"
        },
        "click":{
            "value":"com.zen.zbike:id/cancel_rating"
        }
    },
    {
        "type":"questionnaire",
        "element":"question_answer",
        "assert":{
            "img":"tpl1579589666843.png"
        },
        "click":{
            "value":"com.zen.zbike:id/checkbox_view"
        }
    },
    {
        "type":"clcik",
        "element":"questionnaire_submit",
        "assert":{
            "img":"tpl1579589686172.png"
        },
        "click":{
            "value":"com.zen.zbike:id/submit_view"
        }
    },
    {
        "type":"click",
        "element":"trip_sumamry",
        "assert":{
            "trip_summary":"tpl1579589712018.png",
            "trip_cost":"tpl1579589733523.png",
            "reload":"tpl1579589756688.png"
        },
         "click":{
            "value":"com.zen.zbike:id/back_view"
        }
    }
]

def ride(arr, scooterNo):
    
    for i in arr:
        if i["type"] is "click":
            for img in i["assert"]:
                assert_exists(i["assert"][img])
            click(i["click"]["value"])
        elif i["type"] in ("permisson_allow", "notice", "rate_us",
                           "questionnaire"):
            if exists(i["click"]["value"]) is True:
                click(i["click"]["value"])
            else:
                continue
        elif i["type"] is "sendText":
            assert_exists(i["assert"]["img"])
            set_text(i["sendText"]["value"], i["sendText"]["text"])
        elif i["type"] is "sleep":
            sleep(i["time"]) 

def run(arr, scooterNo):
    
    deviceList = get_deviceList()
    for i in deviceList:
        dev = i[0]
        connect_device("android:///" + dev)
        print('current device is %s'%dev)
        ride(arr, scooterNo)
                   
run(arr,scooterNo)