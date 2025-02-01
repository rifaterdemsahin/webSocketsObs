(venv) rifaterdemsahin@Rifats-MacBook-Pro websocket % python3 ./run.py
2025-02-01 18:52:38,444 - INFO - Connecting to OBS WebSocket...
--- request header ---
2025-02-01 18:52:38,457 - DEBUG - --- request header ---
GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: V2Wqp0cqTDCdQrAmD3GAyg==
Sec-WebSocket-Version: 13
Connection: Upgrade


2025-02-01 18:52:38,457 - DEBUG - GET / HTTP/1.1
Upgrade: websocket
Host: localhost:4444
Origin: http://localhost:4444
Sec-WebSocket-Key: V2Wqp0cqTDCdQrAmD3GAyg==
Sec-WebSocket-Version: 13
Connection: Upgrade


-----------------------
2025-02-01 18:52:38,457 - DEBUG - -----------------------
--- response header ---
2025-02-01 18:52:38,457 - DEBUG - --- response header ---
HTTP/1.1 101 Switching Protocols
2025-02-01 18:52:38,457 - DEBUG - HTTP/1.1 101 Switching Protocols
Connection: Upgrade
2025-02-01 18:52:38,457 - DEBUG - Connection: Upgrade
Sec-WebSocket-Accept: MTrlLycTfZ4spt68ei5sTMHI3Uo=
2025-02-01 18:52:38,457 - DEBUG - Sec-WebSocket-Accept: MTrlLycTfZ4spt68ei5sTMHI3Uo=
Server: WebSocket++/0.8.2
2025-02-01 18:52:38,457 - DEBUG - Server: WebSocket++/0.8.2
Upgrade: websocket
2025-02-01 18:52:38,457 - DEBUG - Upgrade: websocket
-----------------------
2025-02-01 18:52:38,457 - DEBUG - -----------------------
Websocket connected
2025-02-01 18:52:38,457 - INFO - Websocket connected
2025-02-01 18:52:38,457 - INFO - WebSocket connection opened
++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"UPbkTXGhEktYJgB1IIJof8ORbF/q2e+bWKMTQdHLMSI=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:52:38,457 - DEBUG - ++Rcv raw: b'\x81~\x00\xbf{"d":{"authentication":{"challenge":"UPbkTXGhEktYJgB1IIJof8ORbF/q2e+bWKMTQdHLMSI=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"UPbkTXGhEktYJgB1IIJof8ORbF/q2e+bWKMTQdHLMSI=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:52:38,457 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"authentication":{"challenge":"UPbkTXGhEktYJgB1IIJof8ORbF/q2e+bWKMTQdHLMSI=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}'
2025-02-01 18:52:38,457 - INFO - Received message: {"d":{"authentication":{"challenge":"UPbkTXGhEktYJgB1IIJof8ORbF/q2e+bWKMTQdHLMSI=","salt":"aqD1SwRhbiFNSZsFxV0OA1UdExO5N20dp3tPEgPJ/k4="},"obsWebSocketVersion":"5.5.4","rpcVersion":1},"op":0}
2025-02-01 18:52:38,457 - DEBUG - Sending request: {"op": 1, "d": {"rpcVersion": 1, "authentication": "JhSzrsYRLJ9/etzzBUQuJRG7IySSo29QbvqLflPN34s="}}
++Sent raw: b'\x81\xe3\xdd\xafo\xe2\xa6\x8d\x00\x92\xff\x95O\xd3\xf1\x8fM\x86\xff\x95O\x99\xff\xdd\x1f\x81\x8b\xca\x1d\x91\xb4\xc0\x01\xc0\xe7\x8f^\xce\xfd\x8d\x0e\x97\xa9\xc7\n\x8c\xa9\xc6\x0c\x83\xa9\xc6\x00\x8c\xff\x95O\xc0\x97\xc7<\x98\xaf\xdc6\xb0\x91\xe5V\xcd\xb8\xdb\x15\x98\x9f\xfa>\x97\x97\xfd(\xd5\x94\xd6<\xb1\xb2\x9dV\xb3\xbf\xd9\x1e\xae\xbb\xc3?\xac\xee\x9b\x1c\xdf\xff\xd2\x12'
2025-02-01 18:52:38,457 - DEBUG - ++Sent raw: b'\x81\xe3\xdd\xafo\xe2\xa6\x8d\x00\x92\xff\x95O\xd3\xf1\x8fM\x86\xff\x95O\x99\xff\xdd\x1f\x81\x8b\xca\x1d\x91\xb4\xc0\x01\xc0\xe7\x8f^\xce\xfd\x8d\x0e\x97\xa9\xc7\n\x8c\xa9\xc6\x0c\x83\xa9\xc6\x00\x8c\xff\x95O\xc0\x97\xc7<\x98\xaf\xdc6\xb0\x91\xe5V\xcd\xb8\xdb\x15\x98\x9f\xfa>\x97\x97\xfd(\xd5\x94\xd6<\xb1\xb2\x9dV\xb3\xbf\xd9\x1e\xae\xbb\xc3?\xac\xee\x9b\x1c\xdf\xff\xd2\x12'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "JhSzrsYRLJ9/etzzBUQuJRG7IySSo29QbvqLflPN34s="}}'
2025-02-01 18:52:38,458 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 1, "d": {"rpcVersion": 1, "authentication": "JhSzrsYRLJ9/etzzBUQuJRG7IySSo29QbvqLflPN34s="}}'
2025-02-01 18:52:38,458 - INFO - Authentication completed
2025-02-01 18:52:38,458 - DEBUG - Sending request: {"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "inputSettings": {"text": "Spread the love"}}}}
++Sent raw: b'\x81\xfe\x00\xda\x80\x1a\x19\x1e\xfb8vn\xa2 9(\xac:;z\xa2 9e\xa2h|o\xf5\x7fjj\xd4ci{\xa2 9<\xd3\x7fmW\xeejlj\xd3\x7fmj\xe9t~m\xa269<\xf2\x7fhk\xe5imW\xe48#>\xa2yq\x7f\xee}|A\xf4\x7faj\xa269<\xf2\x7fhk\xe5imZ\xe1nx<\xba:b<\xe9tik\xf4Txs\xe58#>\xa2BM[\xd8NA<\xac:;w\xeejlj\xd5opz\xa2 9<\xb9.z/\xe3|./\xad+*-\xb27-*\xb9\x7f4&\xb9~-3\xe5\x7f/*\xe5x/|\xb8\x7f/-\xa269<\xe9tik\xf4I|j\xf4swy\xf38#>\xfb8m{\xf8n;$\xa08Jn\xf2\x7fxz\xa0nq{\xa0vvh\xe58dc\xfdg'
2025-02-01 18:52:38,458 - DEBUG - ++Sent raw: b'\x81\xfe\x00\xda\x80\x1a\x19\x1e\xfb8vn\xa2 9(\xac:;z\xa2 9e\xa2h|o\xf5\x7fjj\xd4ci{\xa2 9<\xd3\x7fmW\xeejlj\xd3\x7fmj\xe9t~m\xa269<\xf2\x7fhk\xe5imW\xe48#>\xa2yq\x7f\xee}|A\xf4\x7faj\xa269<\xf2\x7fhk\xe5imZ\xe1nx<\xba:b<\xe9tik\xf4Txs\xe58#>\xa2BM[\xd8NA<\xac:;w\xeejlj\xd5opz\xa2 9<\xb9.z/\xe3|./\xad+*-\xb27-*\xb9\x7f4&\xb9~-3\xe5\x7f/*\xe5x/|\xb8\x7f/-\xa269<\xe9tik\xf4I|j\xf4swy\xf38#>\xfb8m{\xf8n;$\xa08Jn\xf2\x7fxz\xa0nq{\xa0vvh\xe58dc\xfdg'
++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "inputSettings": {"text": "Spread the love"}}}}'
2025-02-01 18:52:38,458 - DEBUG - ++Sent decoded: fin=1 opcode=1 data=b'{"op": 6, "d": {"requestType": "SetInputSettings", "requestId": "change_text", "requestData": {"inputName": "XTEXTX", "inputUuid": "94c1cf71-1332-449e-89d4-ee64eb6b8e63", "inputSettings": {"text": "Spread the love"}}}}'
2025-02-01 18:52:38,458 - INFO - Image change request sent for /Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg
++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:52:38,459 - DEBUG - ++Rcv raw: b'\x81\'{"d":{"negotiatedRpcVersion":1},"op":2}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:52:38,459 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"negotiatedRpcVersion":1},"op":2}'
2025-02-01 18:52:38,459 - INFO - Received message: {"d":{"negotiatedRpcVersion":1},"op":2}
++Rcv raw: b'\x81t{"d":{"requestId":"change_text","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:52:38,459 - DEBUG - ++Rcv raw: b'\x81t{"d":{"requestId":"change_text","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_text","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:52:38,459 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"requestId":"change_text","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}'
2025-02-01 18:52:38,459 - INFO - Received message: {"d":{"requestId":"change_text","requestStatus":{"code":100,"result":true},"requestType":"SetInputSettings"},"op":7}
2025-02-01 18:52:38,459 - INFO - Request successful
++Rcv raw: b'\x81~\x00\xc2{"d":{"eventData":{"inputName":"XTEXTX","inputSettings":{"text":"Spread the love"},"inputUuid":"94c1cf71-1332-449e-89d4-ee64eb6b8e63"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:52:38,466 - DEBUG - ++Rcv raw: b'\x81~\x00\xc2{"d":{"eventData":{"inputName":"XTEXTX","inputSettings":{"text":"Spread the love"},"inputUuid":"94c1cf71-1332-449e-89d4-ee64eb6b8e63"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"XTEXTX","inputSettings":{"text":"Spread the love"},"inputUuid":"94c1cf71-1332-449e-89d4-ee64eb6b8e63"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:52:38,466 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"XTEXTX","inputSettings":{"text":"Spread the love"},"inputUuid":"94c1cf71-1332-449e-89d4-ee64eb6b8e63"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:52:38,467 - INFO - Received message: {"d":{"eventData":{"inputName":"XTEXTX","inputSettings":{"text":"Spread the love"},"inputUuid":"94c1cf71-1332-449e-89d4-ee64eb6b8e63"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}
++Rcv raw: b'\x81~\x00\xa2{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionStarted"},"op":5}'
2025-02-01 18:57:48,097 - DEBUG - ++Rcv raw: b'\x81~\x00\xa2{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionStarted"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionStarted"},"op":5}'
2025-02-01 18:57:48,098 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionStarted"},"op":5}'
2025-02-01 18:57:48,098 - INFO - Received message: {"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionStarted"},"op":5}
++Rcv raw: b'\x81~\x00\xa5{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionVideoEnded"},"op":5}'
2025-02-01 18:57:48,407 - DEBUG - ++Rcv raw: b'\x81~\x00\xa5{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionVideoEnded"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionVideoEnded"},"op":5}'
2025-02-01 18:57:48,408 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionVideoEnded"},"op":5}'
2025-02-01 18:57:48,408 - INFO - Received message: {"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionVideoEnded"},"op":5}
++Rcv raw: b'\x81~\x00\x9f{"d":{"eventData":{"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":4,"eventType":"CurrentProgramSceneChanged"},"op":5}'
2025-02-01 18:57:48,409 - DEBUG - ++Rcv raw: b'\x81~\x00\x9f{"d":{"eventData":{"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":4,"eventType":"CurrentProgramSceneChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":4,"eventType":"CurrentProgramSceneChanged"},"op":5}'
2025-02-01 18:57:48,409 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":4,"eventType":"CurrentProgramSceneChanged"},"op":5}'
2025-02-01 18:57:48,409 - INFO - Received message: {"d":{"eventData":{"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":4,"eventType":"CurrentProgramSceneChanged"},"op":5}
++Rcv raw: b'\x81~\x00\xa0{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionEnded"},"op":5}'
2025-02-01 18:57:48,759 - DEBUG - ++Rcv raw: b'\x81~\x00\xa0{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionEnded"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionEnded"},"op":5}'
2025-02-01 18:57:48,759 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionEnded"},"op":5}'
2025-02-01 18:57:48,759 - INFO - Received message: {"d":{"eventData":{"transitionName":"Fade","transitionUuid":"cb58236d-6e20-42cb-8297-ef3a7afabc05"},"eventIntent":16,"eventType":"SceneTransitionEnded"},"op":5}
++Rcv raw: b'\x81~\x00\xa8{"d":{"eventData":{"sceneItemId":1,"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":128,"eventType":"SceneItemSelected"},"op":5}'
2025-02-01 18:57:52,586 - DEBUG - ++Rcv raw: b'\x81~\x00\xa8{"d":{"eventData":{"sceneItemId":1,"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":128,"eventType":"SceneItemSelected"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"sceneItemId":1,"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":128,"eventType":"SceneItemSelected"},"op":5}'
2025-02-01 18:57:52,587 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"sceneItemId":1,"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":128,"eventType":"SceneItemSelected"},"op":5}'
2025-02-01 18:57:52,587 - INFO - Received message: {"d":{"eventData":{"sceneItemId":1,"sceneName":"recorder","sceneUuid":"b7592e82-0bde-4866-a14f-5b5c004e8cbd"},"eventIntent":128,"eventType":"SceneItemSelected"},"op":5}
++Rcv raw: b'\x81~\x00\xcd{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":2,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:57:57,239 - DEBUG - ++Rcv raw: b'\x81~\x00\xcd{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":2,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":2,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:57:57,239 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":2,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:57:57,252 - INFO - Received message: {"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":2,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}
++Rcv raw: b'\x81~\x00\xcd{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":0,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:58:02,323 - DEBUG - ++Rcv raw: b'\x81~\x00\xcd{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":0,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":0,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:58:02,323 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":0,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}'
2025-02-01 18:58:02,327 - INFO - Received message: {"d":{"eventData":{"inputName":"macOS Screen Capture","inputSettings":{"type":0,"window":214},"inputUuid":"55a9ba7d-1a7b-46d0-932c-d213a4834ccf"},"eventIntent":8,"eventType":"InputSettingsChanged"},"op":5}
++Rcv raw: b'\x81~\x00\xa3{"d":{"eventData":{"outputActive":false,"outputPath":null,"outputState":"OBS_WEBSOCKET_OUTPUT_STARTING"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,447 - DEBUG - ++Rcv raw: b'\x81~\x00\xa3{"d":{"eventData":{"outputActive":false,"outputPath":null,"outputState":"OBS_WEBSOCKET_OUTPUT_STARTING"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"outputActive":false,"outputPath":null,"outputState":"OBS_WEBSOCKET_OUTPUT_STARTING"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,447 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"outputActive":false,"outputPath":null,"outputState":"OBS_WEBSOCKET_OUTPUT_STARTING"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,448 - INFO - Received message: {"d":{"eventData":{"outputActive":false,"outputPath":null,"outputState":"OBS_WEBSOCKET_OUTPUT_STARTING"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}
++Rcv raw: b'\x81~\x00\xd4{"d":{"eventData":{"outputActive":true,"outputPath":"/Users/rifaterdemsahin/Movies/2025-02-01 18-58-05.mp4","outputState":"OBS_WEBSOCKET_OUTPUT_STARTED"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,462 - DEBUG - ++Rcv raw: b'\x81~\x00\xd4{"d":{"eventData":{"outputActive":true,"outputPath":"/Users/rifaterdemsahin/Movies/2025-02-01 18-58-05.mp4","outputState":"OBS_WEBSOCKET_OUTPUT_STARTED"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"outputActive":true,"outputPath":"/Users/rifaterdemsahin/Movies/2025-02-01 18-58-05.mp4","outputState":"OBS_WEBSOCKET_OUTPUT_STARTED"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,462 - DEBUG - ++Rcv decoded: fin=1 opcode=1 data=b'{"d":{"eventData":{"outputActive":true,"outputPath":"/Users/rifaterdemsahin/Movies/2025-02-01 18-58-05.mp4","outputState":"OBS_WEBSOCKET_OUTPUT_STARTED"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}'
2025-02-01 18:58:05,462 - INFO - Received message: {"d":{"eventData":{"outputActive":true,"outputPath":"/Users/rifaterdemsahin/Movies/2025-02-01 18-58-05.mp4","outputState":"OBS_WEBSOCKET_OUTPUT_STARTED"},"eventIntent":64,"eventType":"RecordStateChanged"},"op":5}
