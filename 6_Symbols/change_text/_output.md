(venv) rifaterdemsahin@Rifats-MacBook-Pro websocket % python3 ./run.py
 *  History restored 

rifaterdemsahin@Rifats-MacBook-Pro websocket % source path/to/venv/bin/activate
(venv) rifaterdemsahin@Rifats-MacBook-Pro websocket % python3 ./run.py                
2025-02-01 18:48:14,181 - INFO - Connecting to OBS WebSocket...
--- request header ---
2025-02-01 18:48:14,185 - DEBUG - --- request header ---
GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: K54O3Wqh6xsUr9zv6j4d3w==
Sec-WebSocket-Version: 13
Connection: Upgrade


2025-02-01 18:48:14,185 - DEBUG - GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: K54O3Wqh6xsUr9zv6j4d3w==
Sec-WebSocket-Version: 13
Connection: Upgrade


-----------------------
2025-02-01 18:48:14,185 - DEBUG - -----------------------
--- response header ---
2025-02-01 18:48:14,185 - DEBUG - --- response header ---
HTTP/1.1 101 Switching Protocols
2025-02-01 18:48:14,185 - DEBUG - HTTP/1.1 101 Switching Protocols
Connection: Upgrade
2025-02-01 18:48:14,185 - DEBUG - Connection: Upgrade
Sec-WebSocket-Accept: jTK+2YzN5j5mFiB7HEDnkiWn7ds=
2025-02-01 18:48:14,185 - DEBUG - Sec-WebSocket-Accept: jTK+2YzN5j5mFiB7HEDnkiWn7ds=
Server: WebSocket++/0.8.2
2025-02-01 18:48:14,185 - DEBUG - Server: WebSocket++/0.8.2
Upgrade: websocket
2025-02-01 18:48:14,185 - DEBUG - Upgrade: websocket
-----------------------
2025-02-01 18:48:14,185 - DEBUG - -----------------------
Websocket connected
2025-02-01 18:48:14,185 - INFO - Websocket connected
2025-02-01 18:48:14,185 - INFO - WebSocket connection opened
++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"DtoV3z3fxJf7UlpQNS/3PcuxKBohD9Nzg+Z879Vkau8=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:14,185 - DEBUG - ++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"DtoV3z3fxJf7UlpQNS/3PcuxKBohD9Nzg+Z879Vkau8=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"DtoV3z3fxJf7UlpQNS/3PcuxKBohD9Nzg+Z879Vkau8=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:14,185 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"DtoV3z3fxJf7UlpQNS/3PcuxKBohD9Nzg+Z879Vkau8=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:14,185 - INFO - Received message: {"d":{"authentication":{"challenge":"DtoV3z3fxJf7UlpQNS/3PcuxKBohD9Nzg+Z879Vkau8=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}
2025-02-01 18:48:14,185 - DEBUG - Sending request: {"op": 1, "d": {"rpcVersion": 1, "authentication": "ZFnii/vAMxzCkIpRH0Poby1FDrk2vilEB4/sqsLdKQw="}}
++Sent raw: b'\x81\xe3\xbb\xd6\xa0\xbf\xc0\xf4\xcf\xcf\x99\xec\x80\x8e\x97\xf6\x82\xdb\x99\xec\x80\xc4\x99\xa4\xd0\xdc\xed\xb3\xd2\xcc\xd2\xb9\xce\x9d\x81\xf6\x91\x93\x9b\xf4\xc1\xca\xcf\xbe\xc5\xd1\xcf\xbf\xc3\xde\xcf\xbf\xcf\xd1\x99\xec\x80\x9d\xe1\x90\xce\xd6\xd2\xf9\xd6\xfe\xf6\xae\xda\xfc\xd0\x9f\xd0\xed\xf3\xe6\xf0\xd0\xd9\xaf\x91\xf9\xff\xa4\xcb\x8d\xcd\xbf\xcc\xfa\xf9\xe2\x8f\xcc\xca\xa5\xec\xdb\xf0\x87\xd7\x82\x99\xab\xdd'
2025-02-01 18:48:14,186 - DEBUG - ++Sent raw: b'\x81\xe3\xbb\xd6\xa0\xbf\xc0\xf4\xcf\xcf\x99\xec\x80\x8e\x97\xf6\x82\xdb\x99\xec\x80\xc4\x99\xa4\xd0\xdc\xed\xb3\xd2\xcc\xd2\xb9\xce\x9d\x81\xf6\x91\x93\x9b\xf4\xc1\xca\xcf\xbe\xc5\xd1\xcf\xbf\xc3\xde\xcf\xbf\xcf\xd1\x99\xec\x80\x9d\xe1\x90\xce\xd6\xd2\xf9\xd6\xfe\xf6\xae\xda\xfc\xd0\x9f\xd0\xed\xf3\xe6\xf0\xd0\xd9\xaf\x91\xf9\xff\xa4\xcb\x8d\xcd\xbf\xcc\xfa\xf9\xe2\x8f\xcc\xca\xa5\xec\xdb\xf0\x87\xd7\x82\x99\xab\xdd'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "ZFnii/vAMxzCkIpRH0Poby1FDrk2vilEB4/sqsLdKQw="}}'
2025-02-01 18:48:14,186 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "ZFnii/vAMxzCkIpRH0Poby1FDrk2vilEB4/sqsLdKQw="}}'
2025-02-01 18:48:14,186 - INFO - Authentication completed
2025-02-01 18:48:14,186 - DEBUG - Sending request: {"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_image", "requestData": {"inputName": "XIMAGEX", "inputUuid": "15a7669f-68e8-4839-84f8-c1333c8fd54b", "inputSettings": {"file": "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"}}}}
++Sent raw: b'\x81\xfe\x01\x01A\xe4\xaeq:\xc6\xc1\x01c\xde\x8eGm\xc4\x8c\x15c\xde\x8e\nc\x96\xcb\x004\x81\xdd\x05\x15\x9d\xde\x14c\xde\x8eS\x12\x81\xda8/\x94\xdb\x05\x12\x81\xda\x05(\x8a\xc9\x02c\xc8\x8eS3\x81\xdf\x04$\x97\xda8%\xc6\x94Qc\x87\xc6\x10/\x83\xcb.(\x89\xcf\x16$\xc6\x82Qc\x96\xcb\x004\x81\xdd\x05\x05\x85\xda\x10c\xde\x8e\nc\x8d\xc0\x014\x90\xe0\x10,\x81\x8cKa\xc6\xf68\x0c\xa5\xe94\x19\xc6\x82Qc\x8d\xc0\x014\x90\xfb\x04(\x80\x8cKa\xc6\x9fD \xd3\x98Gx\x82\x83Gy\x81\x96\\u\xdc\x9dHl\xdc\x9a\x17y\xc9\xcd@r\xd7\x9d\x12y\x82\xcaDu\x86\x8c]a\xc6\xc7\x1f1\x91\xda"$\x90\xda\x18/\x83\xddS{\xc4\xd5S\'\x8d\xc2\x14c\xde\x8eSn\xb1\xdd\x143\x97\x81\x03(\x82\xcf\x05$\x96\xca\x14,\x97\xcf\x19(\x8a\x815.\x93\xc0\x1d.\x85\xca\x02n\x81\xd6\x01$\x8a\xdd\x14p\xd2\xf1\x05 \x9c\xc7_+\x94\xcb\x16c\x99\xd3\x0c<'
2025-02-01 18:48:14,186 - DEBUG - ++Sent raw: b'\x81\xfe\x01\x01A\xe4\xaeq:\xc6\xc1\x01c\xde\x8eGm\xc4\x8c\x15c\xde\x8e\nc\x96\xcb\x004\x81\xdd\x05\x15\x9d\xde\x14c\xde\x8eS\x12\x81\xda8/\x94\xdb\x05\x12\x81\xda\x05(\x8a\xc9\x02c\xc8\x8eS3\x81\xdf\x04$\x97\xda8%\xc6\x94Qc\x87\xc6\x10/\x83\xcb.(\x89\xcf\x16$\xc6\x82Qc\x96\xcb\x004\x81\xdd\x05\x05\x85\xda\x10c\xde\x8e\nc\x8d\xc0\x014\x90\xe0\x10,\x81\x8cKa\xc6\xf68\x0c\xa5\xe94\x19\xc6\x82Qc\x8d\xc0\x014\x90\xfb\x04(\x80\x8cKa\xc6\x9fD \xd3\x98Gx\x82\x83Gy\x81\x96\\u\xdc\x9dHl\xdc\x9a\x17y\xc9\xcd@r\xd7\x9d\x12y\x82\xcaDu\x86\x8c]a\xc6\xc7\x1f1\x91\xda"$\x90\xda\x18/\x83\xddS{\xc4\xd5S\'\x8d\xc2\x14c\xde\x8eSn\xb1\xdd\x143\x97\x81\x03(\x82\xcf\x05$\x96\xca\x14,\x97\xcf\x19(\x8a\x815.\x93\xc0\x1d.\x85\xca\x02n\x81\xd6\x01$\x8a\xdd\x14p\xd2\xf1\x05 \x9c\xc7_+\x94\xcb\x16c\x99\xd3\x0c<'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_image", "requestData": {"inputName": "XIMAGEX", "inputUuid": "15a7669f-68e8-4839-84f8-c1333c8fd54b", "inputSettings": {"file": "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"}}}}'
2025-02-01 18:48:14,186 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_image", "requestData": {"inputName": "XIMAGEX", "inputUuid": "15a7669f-68e8-4839-84f8-c1333c8fd54b", "inputSettings": {"file": "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"}}}}'
2025-02-01 18:48:14,186 - INFO - Image change request sent for /Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg
++Rcv raw: b'\x81u{"d":{"requestId":"change_image","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:14,186 - DEBUG - ++Rcv raw: b'\x81u{"d":{"requestId":"change_image","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_image","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:14,186 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_image","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:14,186 - INFO - Received message: {"d":{"requestId":"change_image","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}
2025-02-01 18:48:14,186 - INFO - Request successful
++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:14,186 - DEBUG - ++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:14,186 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:14,186 - INFO - Received message: {"d":{"negotiatedRpcVersion":1},"op":2}
++Rcv raw: b'\x81~\x00\xe8{"d":{"eventData":{"inputName":"XIMAGEX","inputSettings":{"file":"/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"},"inputUuid":"15a7669f-68e8-4839-84f8-c1333c8fd54b"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:48:14,230 - DEBUG - ++Rcv raw: b'\x81~\x00\xe8{"d":{"eventData":{"inputName":"XIMAGEX","inputSettings":{"file":"/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"},"inputUuid":"15a7669f-68e8-4839-84f8-c1333c8fd54b"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"XIMAGEX","inputSettings":{"file":"/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"},"inputUuid":"15a7669f-68e8-4839-84f8-c1333c8fd54b"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:48:14,230 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"XIMAGEX","inputSettings":{"file":"/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"},"inputUuid":"15a7669f-68e8-4839-84f8-c1333c8fd54b"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:48:14,230 - INFO - Received message: {"d":{"eventData":{"inputName":"XIMAGEX","inputSettings":{"file":"/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"},"inputUuid":"15a7669f-68e8-4839-84f8-c1333c8fd54b"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}
^C2025-02-01 18:48:31,908 - ERROR - Error: 
++Sent raw: b'\x88\x82mJ\xf6\xc1n\xa2'
2025-02-01 18:48:31,908 - DEBUG - ++Sent raw: b'\x88\x82mJ\xf6\xc1n\xa2'
++Sent decoded: fin=1 opcode=8 data=b'\x03\xe8'
2025-02-01 18:48:31,908 - DEBUG - ++Sent decoded: fin=1 opcode=8 data=b'\x03\xe8'
2025-02-01 18:48:31,909 - INFO - Closed connection with status code None: None
tearing down on exception 
2025-02-01 18:48:31,909 - INFO - tearing down on exception 
(venv) rifaterdemsahin@Rifats-MacBook-Pro websocket % python3 ./run.py
2025-02-01 18:48:33,659 - INFO - Connecting to OBS WebSocket...
--- request header ---
2025-02-01 18:48:33,663 - DEBUG - --- request header ---
GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: oh471dDXwe1P122hyNVFsQ==
Sec-WebSocket-Version: 13
Connection: Upgrade


2025-02-01 18:48:33,663 - DEBUG - GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: oh471dDXwe1P122hyNVFsQ==
Sec-WebSocket-Version: 13
Connection: Upgrade


-----------------------
2025-02-01 18:48:33,663 - DEBUG - -----------------------
--- response header ---
2025-02-01 18:48:33,663 - DEBUG - --- response header ---
HTTP/1.1 101 Switching Protocols
2025-02-01 18:48:33,663 - DEBUG - HTTP/1.1 101 Switching Protocols
Connection: Upgrade
2025-02-01 18:48:33,663 - DEBUG - Connection: Upgrade
Sec-WebSocket-Accept: OGp3NNZ9znT8CgRNoOOeSkF+19w=
2025-02-01 18:48:33,663 - DEBUG - Sec-WebSocket-Accept: OGp3NNZ9znT8CgRNoOOeSkF+19w=
Server: WebSocket++/0.8.2
2025-02-01 18:48:33,663 - DEBUG - Server: WebSocket++/0.8.2
Upgrade: websocket
2025-02-01 18:48:33,663 - DEBUG - Upgrade: websocket
-----------------------
2025-02-01 18:48:33,663 - DEBUG - -----------------------
Websocket connected
2025-02-01 18:48:33,663 - INFO - Websocket connected
2025-02-01 18:48:33,663 - INFO - WebSocket connection opened
++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"l2HcsjAYLMZJTEUvHeSvMvTj4YaC2WW12WW/u0rbVaE=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:33,664 - DEBUG - ++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"l2HcsjAYLMZJTEUvHeSvMvTj4YaC2WW12WW/u0rbVaE=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"l2HcsjAYLMZJTEUvHeSvMvTj4YaC2WW12WW/u0rbVaE=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:33,664 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"l2HcsjAYLMZJTEUvHeSvMvTj4YaC2WW12WW/u0rbVaE=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:48:33,664 - INFO - Received message: {"d":{"authentication":{"challenge":"l2HcsjAYLMZJTEUvHeSvMvTj4YaC2WW12WW/u0rbVaE=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}
2025-02-01 18:48:33,664 - DEBUG - Sending request: {"op": 1, "d": {"rpcVersion": 1, "authentication": "i6JykJ2AcMAIp8jq/1qtep6CgeSSbAF25E/KLsP2ZuQ="}}
++Sent raw: b'\x81\xe3\x93#\x90\xe0\xe8\x01\xff\x90\xb1\x19\xb0\xd1\xbf\x03\xb2\x84\xb1\x19\xb0\x9b\xb1Q\xe0\x83\xc5F\xe2\x93\xfaL\xfe\xc2\xa9\x03\xa1\xcc\xb3\x01\xf1\x95\xe7K\xf5\x8e\xe7J\xf3\x81\xe7J\xff\x8e\xb1\x19\xb0\xc2\xfa\x15\xda\x99\xf8i\xa2\xa1\xf0n\xd1\xa9\xe3\x1b\xfa\x91\xbc\x12\xe1\x94\xf6S\xa6\xa3\xf4F\xc3\xb3\xf1b\xd6\xd2\xa6f\xbf\xab\xdfP\xc0\xd2\xc9V\xc1\xdd\xb1^\xed'
2025-02-01 18:48:33,664 - DEBUG - ++Sent raw: b'\x81\xe3\x93#\x90\xe0\xe8\x01\xff\x90\xb1\x19\xb0\xd1\xbf\x03\xb2\x84\xb1\x19\xb0\x9b\xb1Q\xe0\x83\xc5F\xe2\x93\xfaL\xfe\xc2\xa9\x03\xa1\xcc\xb3\x01\xf1\x95\xe7K\xf5\x8e\xe7J\xf3\x81\xe7J\xff\x8e\xb1\x19\xb0\xc2\xfa\x15\xda\x99\xf8i\xa2\xa1\xf0n\xd1\xa9\xe3\x1b\xfa\x91\xbc\x12\xe1\x94\xf6S\xa6\xa3\xf4F\xc3\xb3\xf1b\xd6\xd2\xa6f\xbf\xab\xdfP\xc0\xd2\xc9V\xc1\xdd\xb1^\xed'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "i6JykJ2AcMAIp8jq/1qtep6CgeSSbAF25E/KLsP2ZuQ="}}'
2025-02-01 18:48:33,664 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "i6JykJ2AcMAIp8jq/1qtep6CgeSSbAF25E/KLsP2ZuQ="}}'
2025-02-01 18:48:33,664 - INFO - Authentication completed
2025-02-01 18:48:33,664 - DEBUG - Sending request: {"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "settings": {"text": "Spread the love"}}}}
++Sent raw: b'\x81\xfe\x00\xd5\xf9G\x17\x91\x82ex\xe1\xdb}7\xa7\xd5g5\xf5\xdb}7\xea\xdb5r\xe0\x8c"d\xe5\xad>g\xf4\xdb}7\xb3\xaa"c\xd8\x977b\xe5\xaa"c\xe5\x90)p\xe2\xdbk7\xb3\x8b"f\xe4\x9c4c\xd8\x9de-\xb1\xdb$\x7f\xf0\x97 r\xce\x8d"o\xe5\xdbk7\xb3\x8b"f\xe4\x9c4c\xd5\x983v\xb3\xc3gl\xb3\x90)g\xe4\x8d\tv\xfc\x9ce-\xb1\xdb\x1fC\xd4\xa1\x13O\xb3\xd5g5\xf8\x977b\xe5\xac2~\xf5\xdb}7\xb3\xc0st\xa0\x9a! \xa0\xd4v$\xa2\xcbj#\xa5\xc0":\xa9\xc0##\xbc\x9c"!\xa5\x9c%!\xf3\xc1"!\xa2\xdbk7\xb3\x8a"c\xe5\x90)p\xe2\xdb}7\xea\xdb3r\xe9\x8de-\xb1\xdb\x14g\xe3\x9c&s\xb1\x8d/r\xb1\x95(a\xf4\xdb:j\xec\x84'
2025-02-01 18:48:33,664 - DEBUG - ++Sent raw: b'\x81\xfe\x00\xd5\xf9G\x17\x91\x82ex\xe1\xdb}7\xa7\xd5g5\xf5\xdb}7\xea\xdb5r\xe0\x8c"d\xe5\xad>g\xf4\xdb}7\xb3\xaa"c\xd8\x977b\xe5\xaa"c\xe5\x90)p\xe2\xdbk7\xb3\x8b"f\xe4\x9c4c\xd8\x9de-\xb1\xdb$\x7f\xf0\x97 r\xce\x8d"o\xe5\xdbk7\xb3\x8b"f\xe4\x9c4c\xd5\x983v\xb3\xc3gl\xb3\x90)g\xe4\x8d\tv\xfc\x9ce-\xb1\xdb\x1fC\xd4\xa1\x13O\xb3\xd5g5\xf8\x977b\xe5\xac2~\xf5\xdb}7\xb3\xc0st\xa0\x9a! \xa0\xd4v$\xa2\xcbj#\xa5\xc0":\xa9\xc0##\xbc\x9c"!\xa5\x9c%!\xf3\xc1"!\xa2\xdbk7\xb3\x8a"c\xe5\x90)p\xe2\xdb}7\xea\xdb3r\xe9\x8de-\xb1\xdb\x14g\xe3\x9c&s\xb1\x8d/r\xb1\x95(a\xf4\xdb:j\xec\x84'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "settings": {"text": "Spread the love"}}}}'
2025-02-01 18:48:33,664 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "settings": {"text": "Spread the love"}}}}'
2025-02-01 18:48:33,664 - INFO - Image change request sent for /Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg
++Rcv raw: b'\x81~\x00\xb4{"d":{"requestId":"change_text","requestStatus":{"code":300,"comment":"Your request is missing the `inputSettings` field.","result":false},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:33,667 - DEBUG - ++Rcv raw: b'\x81~\x00\xb4{"d":{"requestId":"change_text","requestStatus":{"code":300,"comment":"Your request is missing the `inputSettings` field.","result":false},"requestType":"SetInputSettings"},"op":7}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_text","requestStatus":{"code":300,"comment":"Your request is missing the `inputSettings` field.","result":false},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:33,667 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_text","requestStatus":{"code":300,"comment":"Your request is missing the `inputSettings` field.","result":false},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:48:33,668 - INFO - Received message: {"d":{"requestId":"change_text","requestStatus":{"code":300,"comment":"Your request is missing the `inputSettings` field.","result":false},"requestType":"SetInputSettings"},"op":7}
2025-02-01 18:48:33,668 - ERROR - Request failed: Your request is missing the `inputSettings` field.
++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:33,668 - DEBUG - ++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:33,668 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:48:33,668 - INFO - Received message: {"d":{"negotiatedRpcVersion":1},"op":2}
---
