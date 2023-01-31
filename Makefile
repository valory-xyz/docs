.PHONY: prepare-release
prepare-release:
	git submodule update --recursive --remote --init
	cd open-autonomy/; git checkout $$(git tag | tail -n 1)
	cd agent-academy-1/; git checkout $$(git tag | tail -n 1)
	cd apy-oracle/; git checkout $$(git tag | tail -n 1)
	cd autonomous-fund/; git checkout $$(git tag | tail -n 1)
	cd contribution-service/; git checkout $$(git tag | tail -n 1)
	cd price-oracle/; git checkout $$(git tag | tail -n 1)
	