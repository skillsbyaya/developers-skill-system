#!/bin/sh
set -eu

usage() {
  echo "Usage: $0 [--link] [claude|codex|all]" >&2
  echo "  --link  symlink to this clone instead of copying, so edits here are live at once" >&2
  exit 2
}

link=false
if [ "${1:-}" = --link ]; then
  link=true
  shift
fi

mode=${1:-all}
case "$mode" in
  claude|codex|all) ;;
  *) usage ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
install_home=${DEVELOPERS_SKILL_HOME:-$HOME}

place() {
  rm -rf -- "$2"
  if [ "$link" = true ]; then
    ln -s "$1" "$2"
  else
    cp -R "$1" "$2"
  fi
}

install_set() {
  platform=$1
  target=$2
  manifest=$target/.developers-skill-system.manifest
  next_manifest=$target/.developers-skill-system.manifest.next

  case "$target" in
    "$install_home/.claude/skills"|"$install_home/.agents/skills") ;;
    *) echo "Refusing unexpected install target: $target" >&2; exit 1 ;;
  esac

  mkdir -p "$target"
  : > "$next_manifest"

  for source in "$repo_root"/skills/*; do
    [ -d "$source" ] || continue
    name=$(basename "$source")
    if [ "$platform" = codex ] && [ "$name" = use-codex ]; then
      continue
    fi
    place "$source" "$target/$name"
    printf '%s\n' "$name" >> "$next_manifest"
  done

  platform_root=$repo_root/platform/$platform/skills
  if [ -d "$platform_root" ]; then
    for source in "$platform_root"/*; do
      [ -d "$source" ] || continue
      name=$(basename "$source")
      place "$source" "$target/$name"
      printf '%s\n' "$name" >> "$next_manifest"
    done
  fi

  if [ -f "$manifest" ]; then
    while IFS= read -r old_name; do
      case "$old_name" in
        ''|*[!a-z0-9-]*) continue ;;
      esac
      if ! grep -qx "$old_name" "$next_manifest"; then
        rm -rf -- "$target/$old_name"
      fi
    done < "$manifest"
  fi

  sort -u "$next_manifest" > "$manifest"
  rm -f -- "$next_manifest"

  if [ "$platform" = claude ]; then
    agents=$install_home/.claude/agents
    mkdir -p "$agents"
    for source in "$repo_root"/subagents/claude-code/*.md; do
      [ -f "$source" ] || continue
      place "$source" "$agents/$(basename "$source")"
    done
  fi

  if [ "$link" = true ]; then
    echo "Linked $platform skills in $target to $repo_root"
  else
    echo "Installed $platform skills in $target"
  fi
}

if [ "$mode" = claude ] || [ "$mode" = all ]; then
  install_set claude "$install_home/.claude/skills"
fi

if [ "$mode" = codex ] || [ "$mode" = all ]; then
  install_set codex "$install_home/.agents/skills"
fi
