#!/bin/sh -e
#
# Flash all the nodes according to the CoAP experiment.
# Manage the tunslip6 process.

router_firmware=./border-router.iotlab-m3
nodes_firmware=./er-example-server.iotlab-m3
tun6='2001:660:4701:f0a5::1'
psfile=$(mktemp)

if [ $# -gt 0 ]; then
	case "$1" in
		http) nodes_firmware=./http-server.iotlab-m3;;
	esac
fi

# get first node number
n=$(iotlab-experiment get -l --state Running|grep -A1 '"resources":'|tail -1|awk -F[-.] '{print $2}')
# TODO: check "$n"

### START ###
ps -af > "$psfile"
if ! grep "$tun6" "$psfile" 1>/dev/null; then

	# start tunslip6 with the tunslip6.py wrapper
	echo starting tunslip6 ...
	sudo tunslip6.py -v2 -L -a m3-"$n" -p 20000 "$tun6"/64 \
		1>/tmp/tunslip6.out 2>/tmp/tunslip6.err &

	echo "flashing border router using $router_firmware ..."
	iotlab-node --update "$router_firmware" -l strasbourg,m3,"$n"
fi
rm -f "$psfile"

echo "flashing other nodes using $nodes_firmware ..."
iotlab-node --update "$nodes_firmware" -e strasbourg,m3,"$n"

router6=$(sed -nr 's/.*(2001:.*::[0-9a-f]{2,4}).*/\1/p' /tmp/tunslip6.out | tail -1)

echo "IPv6 tunslip6 tunnel => $tun6"
echo "IPv6 router address => $router6"
ping6 -c1 "$router6"

echo waiting to converge ...
i=0
while [ $(lynx -dump http://["$router6"]|sed -nr 's/.*(2001:.*::[0-9a-f]*)[ \/].*/\1/p'|wc -l) -ne 4 ]; do
	i=$(($i + 1))
	sleep 1
done

echo
echo "Took $i sec to see all nodes"
lynx -dump http://["$router6"]
