#!/usr/bin/env bash

# 查找文件大小在(1000B - 2240B)之间的文件
find . -size '+100c' -and -size '-200c'

# -!取反，且配合括号使用，并且需要“\”转义
find . -! \( -size '-100c' -or -mtime +3 \)

# {}代表查找到的结果，\;用在最后，前面必须用空格或是tab分割。
find . -size '+100c' -exec ls -al {} \;

