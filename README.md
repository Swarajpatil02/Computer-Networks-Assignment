# Computer Networks Assignment

## Contents

- `socket_server.py` - TCP server program
- `socket_client.py` - TCP client program
- `network_device_classifier.py` - network component classification program
- `outputs/Computer_Networks_Report.pdf` - typed report containing programs, outputs, and results
- `outputs/q1_server_output.txt` - sample server output
- `outputs/q1_client_output.txt` - sample client output
- `outputs/q2_output.txt` - sample classification output

## Question 1: Socket Programming

### Step 1 - Start the server

Open PowerShell/Command Prompt in this folder and run:

```bash
python socket_server.py
```

### Step 2 - Start the client

Open a second PowerShell/Command Prompt in the same folder and run:

```bash
python socket_client.py
```

Enter:

```text
Hello Server!
```

The server receives the message and sends an acknowledgement.

## Question 2: Classification

Run:

```bash
python network_device_classifier.py
```

The program displays the OSI layer and primary function for each device/media type.

## Requirements

- Python 3.x
- No external Python packages are required.
