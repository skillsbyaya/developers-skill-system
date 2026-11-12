#!/bin/sh
# Ranks Markdown files by residue marker words, so a sweep reads the worst first.
# Usage: residue-scan.sh [path ...]      (default: the current directory)
# Output: hits, words, path; highest hits first. A hit is a line to judge, not a verdict.

PATTERN='no longer|used to |formerly|previously|originally|earlier version|superseded|deprecated|workaround|for now|temporar|going forward|replace[sd] the|instead of the (old|former|previous)|(was|were|has been|have been) (removed|retired|replaced|dropped|renamed|moved|fixed)|(fixed|landed|corrected|removed|dropped|retired|renamed|moved|since|as of|until)[^.|]{0,24}(#[0-9]+|20[0-9][0-9]-[0-9][0-9])|landed as|correction[:( ]'

[ $# -eq 0 ] && set -- .

find "$@" \( -name .git -o -name node_modules -o -name archive -o -name migrations \) -prune \
  -o -type f -name '*.md' -print |
while IFS= read -r file; do
  hits=$(grep -ciE "$PATTERN" "$file")
  [ "$hits" -gt 0 ] && printf '%s\t%s\t%s\n' "$hits" "$(wc -w < "$file" | tr -d ' ')" "$file"
done | sort -rn | head -40
