#!/bin/bash
while IFS= read -r line; do
    [[ -z ${line//[[:space:]]/} ]] && continue
    [[ ${line:0:1} == "#" ]] && continue
    git_tool=${line%% *}
    annotation=${line#* }
    git clone "$git_tool"
done < tools.txt
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb -o msfinstall
chmod +x msfinstall
# python3 -m pip install -i https://pypi.org/simple/ GitHacker
