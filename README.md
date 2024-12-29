# PyBridge – A Python-based Communication and Command Bridge

**PyBridge** is a lightweight, multithreaded Python application that enables real-time, bidirectional **communication** between two systems. This tool allows both the client and server to send and receive messages simultaneously, creating a seamless communication experience.

## Features
- **Full-Duplex Communication**: Both client and server can send and receive messages simultaneously.
- **Multithreading**: Efficient use of threads ensures smooth and responsive interaction.
- **Customizable**: Easily adapt the IP address, port, or logic to fit your needs.
- **Lightweight**: Minimal dependencies and straightforward implementation.

## Files 

```server.py```
- Connects to a listening client.
- Enables the server to send and receive messages in real time.

```client.py```
- Sets up a listener for the server to connect.
- Allows the client to participate in full-duplex communication.

## Requirements
Python 3.x
A local or network connection between the two systems.

## Usage
1. Start the Client
- Run the client script on one machine:
```bash
python3 client.py
```
- The client will start listening on 127.0.0.1:1111.

2. Start the Server
- Run the server script on another machine:

```bash
python3 server.py
```
- The server will connect to the client at 127.0.0.1:1111.

3. Communicate
- Both sides can type messages and see them displayed in real time.
- To terminate, close the script manually (Ctrl+C).

## Example
### Client
```bash
$ python3 client.py
Listing....
Connected.
$ Hi there! (Sent to server)
Server: Hello from server! (Received from server)
```
### Server
```bash
$ python3 server.py
Connecting...
Connected.
$ Hello from server! (Sent to client)
Client: Hi there! (Received from client)
```

## Implementation Details
1. **Threading**:
- Two threads handle sending and receiving messages independently for seamless interaction.

2. **Socket Communication**:
- Uses TCP sockets for reliable data transfer.

3. **Full-Duplex Design**:
- Both client and server run identical threading logic for simultaneous message exchange.

## Notes
- **Security Warning**: This tool is for **educational purposes** only and should not be used in unauthorized or insecure environments.
- Modify the IP address and port as needed for your network.

## Future Enhancements
- Add encryption (e.g., SSL/TLS) for secure communication.
- Implement user authentication.
- Add support for file transfers.

## License
This project is provided under the MIT License.

