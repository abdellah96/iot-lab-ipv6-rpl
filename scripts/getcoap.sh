#!/bin/bash -e
#
# Test IPv6 connectivity and CoAP interaction.

router6=$1
prefix=${router6%::*}

if [ $# -ne 1 ] || [ -z $router6 ]; then
	echo "Usage: $0 <rpl-border-router-v6addr>"
	exit 1
fi

expid=$(./scripts/submit.sh | grep '"id":' | awk -F'[ ,]*' '{print $3}')

addrs=$(lynx -dump http://["$router6"] | sed -nr 's/.*(2001:.*::[0-9a-f]*)[ \/].*/\1/p')
echo $addrs

i=0
while [ $i -lt 60 ]; do
	for addr in $addrs; do
		datafile=./data/"$expid"-$(printf "$addr" | tail -c4).txt
		{ coap get -T -t 2 coap://["$addr"]:5683/test/hello 2>/dev/null || echo 0; } | \
		grep -o '[0-9]\+' 1>>"$datafile" &
	done
	sleep 5 &
	wait
	i=$(($i + 1))
done
