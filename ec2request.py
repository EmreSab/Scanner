import requests
import time

# The URL to which the request will be sent
url = 'http://52.1.0.211/api/scan'

while True:
    try:
        # Wait for input from the scanner/keyboard. This blocks until a line is received
        rfid = input()

        # Trim any newline or whitespace (if your scanner sends any at the end)
        rfid = rfid.strip()

        # Ensure the RFID data is not empty
        if rfid:
            # Data to be sent
            data = {'rfid': rfid}

            # Attempt to send the data
            try:
                response = requests.post(url, json=data)
                # Print response status for debugging
                print(f"Status Code: {response.status_code}, Response: {response.text}")
            except requests.exceptions.RequestException as e:
                # Handle any errors in sending the request
                print(f"Request failed: {e}")

        # Delay between iterations can be adjusted or removed as per your requirements
        time.sleep(1)

    except KeyboardInterrupt:
        # Allows you to exit the script gracefully when you press Ctrl+C
        print("Exiting...")
        break
    except EOFError:
        # Handles case where the input stream is closed, allowing graceful exit
        print("Input closed, exiting...")
        break
