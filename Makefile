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


.SILENT: release-message
release-message:
	echo "## v0.0.0" "($(shell date +%Y-%m-%d))"
	echo ""
	echo "Frameworks\n"
	echo "* Open Autonomy Framework:" "$(shell git config --get submodule.open-autonomy.url)" "-" "$(shell git submodule status open-autonomy | cut -c 43-)"
	echo ""
	echo "Toolkits"
	echo ""
	echo "* SMPKit:"          "$(shell git config --get submodule.autonomous-fund.url)"      "-" "$(shell git submodule status autonomous-fund | cut -c 43-)"
	echo "* MintKit:"         "$(shell git config --get submodule.agent-academy-1.url)"      "-" "$(shell git submodule status agent-academy-1 | cut -c 43-)"
	echo "* CoordinationKit:" "$(shell git config --get submodule.contribution-service.url)" "-" "$(shell git submodule status contribution-service | cut -c 43-)"
	echo "* MLKit:"           "$(shell git config --get submodule.apy-oracle.url)"           "-" "$(shell git submodule status apy-oracle | cut -c 43-)"
	echo "* OracleKit:"       "$(shell git config --get submodule.price-oracle.url)"         "-" "$(shell git submodule status price-oracle | cut -c 43-)"
	echo "* IEKit:"           "$(shell git config --get submodule.IEKit.url)"                "-" "$(shell git submodule status IEKit | cut -c 43-)"
	echo ""
	echo "* SMPKit:          $(shell git submodule status autonomous-fund | cut -c 43-)\t\t" "$(shell cd autonomous-fund && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MintKit:         $(shell git submodule status agent-academy-1 | cut -c 43-)\t\t" "$(shell cd agent-academy-1 && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* CoordinationKit: $(shell git submodule status contribution-service | cut -c 43-)\t" "$(shell cd contribution-service && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MLKit:           $(shell git submodule status apy-oracle | cut -c 43-)\t\t\t" "$(shell cd apy-oracle && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* OracleKit:       $(shell git submodule status price-oracle | cut -c 43-)\t\t" "$(shell cd price-oracle && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* IEKit:           $(shell git submodule status IEKit | cut -c 43-)\t\t\t" "$(shell cd IEKit && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"




