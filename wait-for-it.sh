#!/usr/bin/env bash
# wait-for-it.sh

host="$1"
shift
cmd="$@"

until nc -z "$host" 5432; do
  echo "Waiting for database to be ready..."
  sleep 2
done

echo "Database is ready, starting the application..."
exec $cmd

