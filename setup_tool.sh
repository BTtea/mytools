#!/bin/bash
while IFS= read -r line; do
    [[ -z ${line//[[:space:]]/} ]] && continue
    [[ ${line:0:1} == "#" ]] && continue
    git_tool=${line%% *}
    annotation=${line#* }
    git clone "$git_tool"
done < tools.txt
# python3 -m pip install -i https://pypi.org/simple/ GitHacker
