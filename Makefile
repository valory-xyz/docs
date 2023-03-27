.PHONY: prepare-release
prepare-release:
	git submodule update --recursive --remote --init
	cd open-autonomy/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd agent-academy-1/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd apy-oracle/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd autonomous-fund/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd contribution-service/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd IEKit/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	cd price-oracle/; git fetch origin --tags --force; git checkout $$(git tag --sort=committerdate | tail -n 1)
	git submodule status
	