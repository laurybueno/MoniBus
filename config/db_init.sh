#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    ALTER SYSTEM SET synchronous_commit TO OFF;
    ALTER SYSTEM SET huge_pages TO TRY;
EOSQL
