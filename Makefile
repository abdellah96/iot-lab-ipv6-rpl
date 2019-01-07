BASEDIR = $(PWD)
CONTIKI = $(PWD)/iot-lab/parts/contiki
PATCH  ?= 1 4 5

EXAMPLES = border-router coap-server tsch-border-router tsch-coap-server

base: coap-server border-router
tsch: tsch-coap-server tsch-border-router

help:
	@cat $(BASEDIR)/Makefile.help | sed "s/@EXAMPLES@/$(EXAMPLES)/"
	@echo
	@ls -1 $(BASEDIR)/patches
	@echo

all: $(EXAMPLES)

$(BASEDIR)/iot-lab:
	git submodule update

$(CONTIKI): $(BASEDIR)/iot-lab
	cd $(BASEDIR)/iot-lab && make setup-contiki

$(EXAMPLES): $(CONTIKI)
	cd $(CONTIKI) \
	&& git reset --hard \
	&& git pull \
	&& for n in $(PATCH); do \
		git apply -v $(BASEDIR)/patches/*0$$n-*.diff; \
	done \
	&& case $@ in \
		coap-server) example=iotlab/04-er-rest-example;; \
		border-router) example=ipv6/rpl-border-router;; \
		tsch-coap-server) example=iotlab/06-rpl-tsch-coap;; \
		tsch-border-router) example=iotlab/05-rpl-tsch-border-router;; \
		*) example=non/existent/example/dir;; \
	esac \
	&& cd ./examples/$$example \
	&& git --no-pager diff \
	&& LDFLAGS=-s make TARGET=iotlab-m3 \
	&& mv -v ./*.iotlab-m3 $(BASEDIR)/

clean:
	rm -f $(BASEDIR)/*.iotlab-m3

.PHONY: help all $(EXAMPLES) clean
