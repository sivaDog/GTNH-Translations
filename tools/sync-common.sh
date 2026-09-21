#!/usr/bin/env bash
# Shared helpers for the sync-verified-*.sh scripts.
#
# Source it after REPO_ROOT is set:
#   . "$REPO_ROOT/tools/sync-common.sh"
#
# Keeps the local instance path out of the repo and out of the scripts' output,
# so pasted logs and screenshots do not carry a home directory.

# Resolve the instance .minecraft directory: $INSTANCE_MC, else INSTANCE_MC from
# .env (gitignored), else give up with instructions. No default is baked in.
resolve_instance_mc() {
  if [[ -z "${INSTANCE_MC:-}" && -f "$REPO_ROOT/.env" ]]; then
    INSTANCE_MC="$(sed -n 's/^INSTANCE_MC=//p' "$REPO_ROOT/.env" \
      | head -n 1 | tr -d '\r' | sed 's/^"\(.*\)"$/\1/')"
  fi

  if [[ -z "${INSTANCE_MC:-}" ]]; then
    cat >&2 <<'MSG'
INSTANCE_MC is not set.

Point it at your Prism instance's .minecraft directory, either by adding a line
to .env (gitignored, so the path stays out of the repo):

  INSTANCE_MC=/path/to/instances/<instance>/.minecraft

or by passing it for a single run:

  INSTANCE_MC=/path/to/.minecraft ./sync.sh
MSG
    exit 1
  fi

  # .env may hold a Windows-style path. Fold it to POSIX under MSYS so prefix
  # matching and short_path behave the same however it was written.
  if [[ "$INSTANCE_MC" =~ ^[A-Za-z]:[/\\] ]] && command -v cygpath >/dev/null 2>&1; then
    INSTANCE_MC="$(cygpath -u "$INSTANCE_MC")"
  fi

  export INSTANCE_MC
}

# Print a path with the repo root, the instance root and the home directory
# folded away. A path under none of them is reduced to its last two components
# rather than printed whole.
short_path() {
  local path="$1"
  if [[ -n "${REPO_ROOT:-}" && "$path" == "$REPO_ROOT"/* ]]; then
    printf './%s' "${path#"$REPO_ROOT"/}"
  elif [[ -n "${INSTANCE_MC:-}" && "$path" == "$INSTANCE_MC" ]]; then
    printf '<instance>'
  elif [[ -n "${INSTANCE_MC:-}" && "$path" == "$INSTANCE_MC"/* ]]; then
    printf '<instance>/%s' "${path#"$INSTANCE_MC"/}"
  elif [[ -n "${HOME:-}" && "$path" == "$HOME"/* ]]; then
    printf '~/%s' "${path#"$HOME"/}"
  else
    printf '.../%s/%s' "$(basename "$(dirname "$path")")" "$(basename "$path")"
  fi
}
