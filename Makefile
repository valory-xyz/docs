.PHONY: build-release
build-release:
	git submodule update --recursive --init
	cd open-autonomy/; git checkout $$(git tag | tail -n 1)
	