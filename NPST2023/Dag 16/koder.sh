#!/usr/bin/bash

git checkout ikke-merge-før-julaften
export DISABLE_SELF_DESTRUCT=1
./.git/hooks/pre-merge-commit
cat feltagenter_kontaktmanual.md