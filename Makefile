build:
	bash scripts/build.sh

check-diff: build
	if [ -n "$(shell git status --porcelain)" ]; then \
		echo "There are changes to the root directory. Please commit them before running this command."; \
		exit 1; \
	fi