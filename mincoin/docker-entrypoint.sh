#!/bin/bash

set -e

if [ $(echo "$1" | cut -c1) = "-" ]; then
  echo "$0: assuming arguments for mincoind"

  set -- mincoind "$@"
fi

if [ $(echo "$1" | cut -c1) = "-" ] || [ "$1" = "mincoind" ]; then
  mkdir -p "$MINCOIN_DATA"
  chmod 700 "$MINCOIN_DATA"
  chown -R mincoin "$MINCOIN_DATA"

  echo "$0: setting data directory to $MINCOIN_DATA"

  set -- "$@" -datadir="$MINCOIN_DATA"
fi

if [ "$1" = "mincoind" ] || [ "$1" = "mincoin-cli" ] || [ "$1" = "mincoin-tx" ]; then
  echo
  exec gosu mincoin "$@"
fi

echo
exec "$@"