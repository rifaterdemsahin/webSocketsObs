# webSocketsObs
Web Sockets Implementation in OBS

To change an image in OBS using WebSockets, you'll first need to set up the OBS WebSocket plugin and connect to OBS using a WebSocket client. Here’s a step-by-step guide:

### **1. Install the OBS WebSocket Plugin**

1. **Download and install OBS WebSocket:**
   - Go to the [OBS WebSocket GitHub page](https://github.com/obsproject/obs-websocket).
   - Download the latest release suitable for your operating system (Windows, macOS, or Linux).
   - Follow the installation instructions provided in the repository.

2. **Enable the WebSocket server in OBS:**
   - Open OBS and go to `Tools` > `WebSockets Server Settings`.
   - Ensure that WebSockets is enabled.
   - Set a password (optional) and make sure the port is 4444 (or another of your choosing).
   - Click **OK** to save.

### **2. Set up a WebSocket Client**

You can use a WebSocket client to send commands to OBS. For this tutorial, we'll use Python, but you could use other tools like JavaScript or Node.js if you prefer.

1. **Install Python and WebSocket client:**
   - First, make sure you have Python installed.
   - Install the `websocket-client` library:
     ```bash
     pip install websocket-client
     ```

### **3. Change Image Using WebSockets**

Now, let’s write a script that will change an image source in OBS. Make sure the image source is already set up in OBS.

#### Python Script for Changing Image:

```python
import websocket
import json

# Replace with your OBS WebSocket server details
OBS_WEBSOCKET_URL = "ws://localhost:4444"  # URL to your OBS WebSocket server
OBS_PASSWORD = "your_password"  # Password if you set one, leave empty if not

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
    source_name = "YourImageSource"  # The name of the image source in OBS
    image_file_path = "path_to_new_image.png"  # Path to your new image file

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
```

### **4. Explanation of the Script**

- **on_open(ws):** This function runs when the WebSocket connection is opened. It sends the authentication request if a password is set and changes the image source to the new file.
- **send_request(ws, request):** This function sends a WebSocket message to OBS.
- **change_image_payload:** This is the payload that tells OBS to change the image for a source. Make sure the `sourceName` is the exact name of the image source in OBS.
- **ws.run_forever():** Keeps the WebSocket connection open and listens for events.

### **5. Run the Script**

1. Replace `your_password` with the password you set in the OBS WebSocket settings (if applicable).
2. Replace `YourImageSource` with the exact name of your image source in OBS.
3. Replace `path_to_new_image.png` with the path to the new image file you want to use.
4. Save the script and run it in the terminal:

   ```bash
   python change_image_in_obs.py
   ```

### **6. Verify in OBS**

Once the script runs, OBS should automatically update the image source to the new image you specified.

### **Troubleshooting:**

- Ensure your OBS WebSocket server is running and OBS is open.
- Make sure the WebSocket URL (e.g., `ws://localhost:4444`) matches the settings in OBS.
- If there are authentication issues, check the password settings.

Let me know if you run into any issues!