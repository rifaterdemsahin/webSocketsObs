import websocket
import json
import logging
import base64
import hashlib

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace with your OBS WebSocket server details
OBS_WEBSOCKET_URL = "ws://localhost:4444"
OBS_PASSWORD = "YYmm123!"

class OBSWebSocket:
    def __init__(self, url, password):
        self.url = url
        self.password = password
        self.ws = None
        self.authenticated = False

    def connect(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.run_forever()

    def on_open(self, ws):
        logging.info("WebSocket connection opened")
        # Wait for the initial identification message from OBS

    def on_message(self, ws, message):
        logging.info(f"Received message: {message}")
        try:
            data = json.loads(message)
            
            # Handle authentication
            if not self.authenticated and "op" in data and data["op"] == 0:
                self.handle_authentication(data)
            
            # Handle other responses
            elif "status" in data:
                if data["status"] == "error":
                    logging.error(f"Error from OBS: {data['error']}")
                else:
                    logging.info(f"Success response: {data}")

        except json.JSONDecodeError:
            logging.error(f"Failed to parse message: {message}")

    def handle_authentication(self, data):
        if "d" in data and "authentication" in data["d"]:
            auth_required = data["d"]["authentication"]
            if auth_required:
                challenge = data["d"].get("challenge")
                salt = data["d"].get("salt")

                secret = base64.b64encode(
                    hashlib.sha256(
                        (self.password + salt).encode('utf-8')
                    ).digest()
                ).decode('utf-8')

                auth_response = base64.b64encode(
                    hashlib.sha256(
                        (secret + challenge).encode('utf-8')
                    ).digest()
                ).decode('utf-8')

                auth_payload = {
                    "op": 1,
                    "d": {
                        "rpcVersion": 1,
                        "authentication": auth_response
                    }
                }
                self.send_request(auth_payload)
                self.authenticated = True
                logging.info("Authentication completed")

    def change_image(self, source_name, image_path):
        if not self.authenticated:
            logging.error("Not authenticated yet")
            return

        payload = {
            "op": 6,
            "d": {
                "requestType": "SetInputSettings",
                "requestId": "change_image",
                "inputName": source_name,
                "inputSettings": {
                    "file": image_path
                }
            }
        }
        self.send_request(payload)

    def send_request(self, payload):
        if self.ws and self.ws.sock and self.ws.sock.connected:
            message = json.dumps(payload)
            logging.debug(f"Sending request: {message}")
            self.ws.send(message)
        else:
            logging.error("WebSocket is not connected")

    def on_error(self, ws, error):
        logging.error(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        logging.info(f"Closed connection with status code {close_status_code}: {close_msg}")

if __name__ == "__main__":
    obs_ws = OBSWebSocket(OBS_WEBSOCKET_URL, OBS_PASSWORD)
    
    try:
        obs_ws.connect()
    except KeyboardInterrupt:
        logging.info("Shutting down...")