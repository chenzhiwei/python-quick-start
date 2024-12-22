IMG ?= docker.io/siji/taishan

ifeq ($(shell command -v docker 2>/dev/null),)
    DOCKER=podman
else
    DOCKER=docker
endif

all: build

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

env: ## Create the virtual environment
	uv lock
	uv venv

build: ## Install the dependencies
	uv sync

docker-build: ## Build the docker image
	git clean -df src
	git clean -df test
	$(DOCKER) build -t ${IMG} -f Dockerfile.prod .
