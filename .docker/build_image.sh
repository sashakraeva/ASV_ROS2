#!/usr/bin/env bash

echo -e "Building iaac_hull image"

DOCKER_BUILDKIT=1 \
docker build --pull --rm -f ./.docker/Dockerfile \
--build-arg BUILDKIT_INLINE_CACHE=1 \
--target bash \
--tag iaac_hull .