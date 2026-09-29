#!/bin/sh
set -eu

usage() {
  echo "Usage: $0 [claude|codex|all]" >&2
  exit 2
}

mode=${1:-all}
case "$mode" in
  claude|codex|all) ;;
  *) usage ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
install_home=${DEVELOPERS_SKILL_HOME:-$HOME}

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
    rm -rf -- "$target/$name"
    cp -R "$source" "$target/$name"
    printf '%s\n' "$name" >> "$next_manifest"
  done

  platform_root=$repo_root/platform/$platform/skills
  if [ -d "$platform_root" ]; then
    for source in "$platform_root"/*; do
      [ -d "$source" ] || continue
      name=$(basename "$source")
      rm -rf -- "$target/$name"
      cp -R "$source" "$target/$name"
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
  echo "Installed $platform skills in $target"
}

if [ "$mode" = claude ] || [ "$mode" = all ]; then
  install_set claude "$install_home/.claude/skills"
fi

if [ "$mode" = codex ] || [ "$mode" = all ]; then
  install_set codex "$install_home/.agents/skills"
fi
