
CONAN_PROFILE ?= default
CONAN_FLAGS+=--build missing
CONAN_FLAGS+=--profile:all $(CONAN_PROFILE)
.PHONY:conan
conan:
	uv tool run conan install . $(CONAN_FLAGS)

.PHONY:build
build: conan
	uv sync --reinstall -v

.PHONY:test
test:
	uv run pytest -sv test/

.PHONY:clean
clean:
	rm -rf build
	git clean -fdx

.PHONY:all
all: clean build test

.DEFAULT_GOAL:=all
