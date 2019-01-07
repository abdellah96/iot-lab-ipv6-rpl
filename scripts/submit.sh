#!/bin/sh -e
#
# Submit an experiment with 5 nodes @Strasbourg.

t="$1"
[ -z "$1" ] && t=5

n=5
firmware=./http-server.iotlab-m3
profile=profconso
#profile=profradio

# Submit experiment with a schedule date (e.g. 20 May 2014 14:00:00):
# add -r $(date +%s -d "20 May 2014 14:00:00 UTC")

if ! iotlab-experiment get -l --state Running | grep 'Running' 1>/dev/null; then
	iotlab-experiment submit -n contiki -d "$t" -l strasbourg,m3,50-54,,"$profile"
		#strasbourg,m3,10-14,,"$profile"
		#"$n",site=strasbourg+archi=m3:at86rf231+mobile=0,,"$profile"
	iotlab-experiment wait
fi

iotlab-experiment get -l --state Running
