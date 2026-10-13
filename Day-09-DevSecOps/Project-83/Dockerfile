FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 10001 appuser

USER 10001

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD test -d /home/appuser || exit 1

CMD ["sleep", "3600"]
