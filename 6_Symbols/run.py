import websocket
import json

# Replace with your OBS WebSocket server details
OBS_WEBSOCKET_URL = "ws://localhost:4444"  # URL to your OBS WebSocket server
OBS_PASSWORD = "XXX"  # Password if you set one, leave empty if not

# Function to send a request to OBS WebSocket
def send_request(ws, request):
    ws.send(json.dumps(request))

# Open WebSocket connection to OBS
def on_open(ws):
    # Authenticate if password is set
    if OBS_PASSWORD:
        auth_payload = {
            "op": 1,  # Authentication request
            "d": {
                "password": OBS_PASSWORD
            }
        }
        send_request(ws, auth_payload)

    # Change image source (you must know the source name in OBS)
    source_name = "Image"  # The name of the image source in OBS
    image_file_path = "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg"  # Path to your new image file

    # Set the new image for the source
    change_image_payload = {
        "op": 6,  # Set source settings request
        "d": {
            "sourceName": source_name,
            "sourceSettings": {
                "file": image_file_path
            }
        }
    }

    send_request(ws, change_image_payload)

def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Closed connection")

# Create WebSocket connection to OBS
ws = websocket.WebSocketApp(
    OBS_WEBSOCKET_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

# Run the WebSocket client
ws.run_forever()