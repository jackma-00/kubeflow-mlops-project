default: run

compile:
	cd pipeline \
	&& ./compile.sh

run: compile
	python kfp_client.py