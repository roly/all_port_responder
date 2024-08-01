# all_port_responder

Using IPtables to redirect every port to the responder.py script this lets us respond to every TCP port 
this is useful if you want to quickly test what ports are accesble externally from a network you are on 

## setup iptables 

run the setup_iptables script 

it would be a good idea to then maybe install iptables-persistant afterwards 
`sudo apt install iptables-persistent` 

## install the service 

first edit tcp_responder.service 

sudo cp tcp_responder.service /etc/systemd/system/

