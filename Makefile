EMPTY_STR=""

.PHONY: prepare-release
prepare-release:
	tox -e update-submodules-versions


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
	echo "* GovKit:"          "$(shell git config --get submodule.governatooorr.url)"        "-" "$(shell git submodule status governatooorr | cut -c 43-)"
	echo "* MechKit:"         "$(shell git config --get submodule.mech.url)"                 "-" "$(shell git submodule status mech | cut -c 43-)"
	echo "* KeeperKit:"       "$(shell git config --get submodule.agent-academy-2.url)"      "-" "$(shell git submodule status agent-academy-2 | cut -c 43-)"
	echo "* MessagingKit:"    "$(shell git config --get submodule.open-acn.url)"             "-" "$(shell git submodule status open-acn | cut -c 43-)"
	echo ""
	echo "Demos"
	echo "* Hello World:"     "$(shell git config --get submodule.hello-world.url)"                 "-" "$(shell git submodule status hello-world | cut -c 43-)"
	echo ""
	echo ""
	echo "* SMPKit:          $(shell git submodule status autonomous-fund | cut -c 43-)\t\t" "$(shell cd autonomous-fund && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MintKit:         $(shell git submodule status agent-academy-1 | cut -c 43-)\t\t" "$(shell cd agent-academy-1 && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* CoordinationKit: $(shell git submodule status contribution-service | cut -c 43-)\t" "$(shell cd contribution-service && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MLKit:           $(shell git submodule status apy-oracle | cut -c 43-)\t\t\t" "$(shell cd apy-oracle && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* OracleKit:       $(shell git submodule status price-oracle | cut -c 43-)\t\t" "$(shell cd price-oracle && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* IEKit:           $(shell git submodule status IEKit | cut -c 43-)\t\t\t" "$(shell cd IEKit && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* GovKit:          $(shell git submodule status governatooorr | cut -c 43-)\t\t\t" "$(shell cd governatooorr && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MechKit:         $(shell git submodule status mech | cut -c 43-)\t\t\t" "$(shell cd mech && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* KeeperKit:       $(shell git submodule status agent-academy-2 | cut -c 43-)\t\t\t" "$(shell cd agent-academy-2 && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* MessagingKit:    $(shell git submodule status open-acn | cut -c 43-)\t\t\t" "$(shell cd open-acn && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"
	echo "* Hello World      $(shell git submodule status hello-world | cut -c 43-)\t\t\t" "$(shell cd hello-world && git log -1 --format='%cd' --date=format:'%Y-%m-%d')"

