# [Previous OBSWebSocket class code remains the same...]

if __name__ == "__main__":
    # Create the WebSocket client
    obs_ws = OBSWebSocket("ws://localhost:4444", "XXX")
    
    # Define a custom message handler to execute after authentication
    def on_authenticated(ws):
        logging.info("Authentication successful, changing image...")
        obs_ws.change_image("Image", "/Users/rifaterdemsahin/Downloads/expense16_taxi.jpeg")
    
    # Add the handler to the class instance
    obs_ws.on_authenticated = on_authenticated
    
    try:
        # Start the connection
        obs_ws.connect()
    except KeyboardInterrupt:
        logging.info("Shutting down...")