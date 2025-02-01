import websocket
import json
import logging
import base64
import hashlib

inputUuid = "15a7669f-68e8-4839-84f8-c1333c8fd54b"

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

    def on_message(self, ws, message):
        logging.info(f"Received message: {message}")
        try:
            data = json.loads(message)
            
            # Handle initial connection message
            if "op" in data and data["op"] == 0 and "d" in data:
                if "authentication" in data["d"]:
                    self.handle_authentication(data["d"]["authentication"])
            
            # Handle response messages
            elif "op" in data and data["op"] == 7:
                self.handle_response(data["d"])

        except json.JSONDecodeError:
            logging.error(f"Failed to parse message: {message}")
        except Exception as e:
            logging.error(f"Error processing message: {str(e)}")

    def handle_response(self, response_data):
        if "requestStatus" in response_data:
            status = response_data["requestStatus"]
            if not status.get("result", False):
                logging.error(f"Request failed: {status.get('comment', 'Unknown error')}")
            else:
                logging.info("Request successful")

    def handle_authentication(self, auth_data):
        try:
            if auth_data:
                challenge = auth_data.get("challenge", "")
                salt = auth_data.get("salt", "")

                if not challenge or not salt:
                    logging.error("Missing authentication challenge or salt")
                    return

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
                
                # Change image after successful authentication
                self.change_image(inputUuid, "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg")

        except Exception as e:
            logging.error(f"Authentication error: {str(e)}")

    def change_image(self, input_uuid, image_path):
        if not self.authenticated:
            logging.error("Not authenticated yet")
            return

        payload = {
            "op": 6,
            "d": {
                "requestType": "SetInputSettings",
                "requestId": "change_image",
                "requestData": {  # Add this nested level
                    "inputName": "XIMAGEX",
                    "inputUuid": input_uuid,
                    "inputSettings": {
                        "file": image_path
                    }
                }
            }
        }
        self.send_request(payload)
        logging.info(f"Image change request sent for {image_path}")

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
    # Replace with your OBS WebSocket server details
    obs_ws = OBSWebSocket("ws://localhost:4444", "#e3EB50")
    
    try:
        logging.info("Connecting to OBS WebSocket...")
        obs_ws.connect()
    except KeyboardInterrupt:
        logging.info("Shutting down...")