# Smart-Home-Network

First the tcp_server must be started and then the tcp_client.
The tcp_server and tcp_client each run the smart home protocol and the respective smart home client and server.
They are connected through port 5000 using ipv4 and the tcp protocol.

When the client is started, a message is sent to the server and the client enters a loop, which iteratively recieves messages from the smart home server and sends messages from the user to the server. For example, when we first start the program, the server sends a login prompt for the username and password of the user. Then what the user types in is sent to the server. If the user is in the list of users of the smart home, the server sends back a menu to list the different devices in the smart home, display states of the different devices, change states of the devices, and finally logout. We access the server through commands issued at the client.

When the number of the menu item to list devices is picked, the house alarm, the locks, and the different lights are displayed. Lights are in different rooms of the house, and within each room, a specific set of lights associated with the room is displayed.

When the number of the menu item to display states is picked, each device is displayed along with the various state associated with the device. A house alarm can be armed or disarmed. Locks can be locked or opened. Lights can be on or off, dimmed or bright, and green, blue, red, or white.

When the number of the menu item to display states is picked, the states and list of the devices are displayed.
When we type a menu number in the prompt of the different devices displayed, we change their state:

1. There is only one house alarm. It can be armed/disarmed by typing a 4 digit pin into the command line.
2. There are 4 locks. Each lock has 5 different 4 digit pin numbers associated with them. When we want to unlock/lock a lock, we must type one of these pin numbers in the prompt.
3. The lights have three different states associated with them. They can be turned on or off, be dimmed or bright, or red,white,green, or blue. A submenu is diaplyed to the user for him/her to decide which state to change.
