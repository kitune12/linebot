{\rtf1\ansi\ansicpg932\cocoartf1671\cocoasubrtf100
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset128 HiraginoSans-W3;}
{\colortbl;\red255\green255\blue255;\red252\green103\blue131;\red41\green53\blue57;\red220\green220\blue220;
\red140\green155\blue158;\red55\green169\blue206;\red124\green221\blue60;\red230\green203\blue56;\red151\green101\blue242;
}
{\*\expandedcolortbl;;\cssrgb\c100000\c50196\c58431;\cssrgb\c21176\c27059\c28627;\cssrgb\c89020\c89020\c89020;
\cssrgb\c61569\c67059\c68235;\cssrgb\c25490\c71765\c84314;\cssrgb\c54510\c87451\c29804;\cssrgb\c92157\c82353\c27843;\cssrgb\c66275\c50196\c96078;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww25400\viewh13620\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28\fsmilli14400 \cf2 \cb3 \expnd0\expndtw0\kerning0
from\cf4  flask \cf2 import\cf4  Flask, request, abort\
\
\cf2 from\cf4  linebot \cf2 import\cf4  (\
    LineBotApi, WebhookHandler\
)\
\cf2 from\cf4  linebot.exceptions \cf2 import\cf4  (\
    InvalidSignatureError\
)\
\cf2 from\cf4  linebot.models \cf2 import\cf4  (\
    MessageEvent, TextMessage, TextSendMessage,\
)\
\cf2 import\cf4  os\
\
app \cf2 =\cf4  Flask(__name__)\
\
\pard\pardeftab720\partightenfactor0
\cf5 #
\f1 \'8a\'c2\'8b\'ab\'95\'cf\'90\'94\'8e\'e6\'93\'be
\f0 \cf4 \
YOUR_CHANNEL_ACCESS_TOKEN \cf2 =\cf4  os\cf2 .\cf4 environ[\cf6 "YOUR_CHANNEL_ACCESS_TOKEN"\cf4 ]\
YOUR_CHANNEL_SECRET \cf2 =\cf4  os\cf2 .\cf4 environ[\cf6 "YOUR_CHANNEL_SECRET"\cf4 ]\
\
line_bot_api \cf2 =\cf4  LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)\
handler \cf2 =\cf4  WebhookHandler(YOUR_CHANNEL_SECRET)\
\
\pard\pardeftab720\partightenfactor0
\cf7 @app.route\cf4 (\cf6 "/callback"\cf4 , methods\cf2 =\cf4 [\cf6 'POST'\cf4 ])\
\pard\pardeftab720\partightenfactor0
\cf8 def\cf4  \cf7 callback\cf4 ():\
    \cf5 # get X-Line-Signature header value\cf4 \
    signature \cf2 =\cf4  request\cf2 .\cf4 headers[\cf6 'X-Line-Signature'\cf4 ]\
\
    \cf5 # get request body as text\cf4 \
    body \cf2 =\cf4  request\cf2 .\cf4 get_data(as_text\cf2 =\cf4 True)\
    app\cf2 .\cf4 logger\cf2 .\cf4 info(\cf6 "Request body: "\cf4  \cf2 +\cf4  body)\
\
    \cf5 # handle webhook body\cf4 \
    \cf8 try\cf4 :\
        handler\cf2 .\cf4 handle(body, signature)\
    \cf8 except\cf4  InvalidSignatureError:\
        abort(\cf9 400\cf4 )\
\
    \cf8 return\cf4  \cf6 'OK'\cf4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 @handler.add\cf4 (MessageEvent, message\cf2 =\cf4 TextMessage)\
\pard\pardeftab720\partightenfactor0
\cf8 def\cf4  \cf7 handle_message\cf4 (event):\
    line_bot_api\cf2 .\cf4 reply_message(\
        event\cf2 .\cf4 reply_token,\
        TextSendMessage(text\cf2 =\cf4 event\cf2 .\cf4 message\cf2 .\cf4 text))\
\
\
\cf8 if\cf4  __name__ \cf2 ==\cf4  \cf6 "__main__"\cf4 :\
\pard\pardeftab720\partightenfactor0
\cf5 #    app.run()\cf4 \
    port \cf2 =\cf4  int(os\cf2 .\cf4 getenv(\cf6 "PORT"\cf4 , \cf9 5000\cf4 ))\
    app\cf2 .\cf4 run(host\cf2 =\cf6 "0.0.0.0"\cf4 , port\cf2 =\cf4 port)}