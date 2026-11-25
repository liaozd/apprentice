"""1. 两数之和 — 用例

用例来源:LeetCode 官方示例 + 边界补充。
同一组用例跑本目录下所有解法;解法可以原地修改 nums,测试按行拷贝保护原始用例。
"""

import importlib.util
from pathlib import Path

import pytest

_DIR = Path(__file__).parent
# 不同题目录下会有同名解法文件(dfs.py / bfs.py……),pytest 默认导入模式下
# 裸 import 会在单进程内发生模块名冲突,因此按文件路径加载并加题目前缀。
_PREFIX = _DIR.name.replace("-", "_")


def _load(stem: str):
    spec = importlib.util.spec_from_file_location(f"{_PREFIX}_{stem}", _DIR / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVERS = {
    "暴力枚举": _load("brute_force").solve,
    "哈希表": _load("hash_map").solve,
}

CASES = [
    # (nums, target, expected)
    # LC 官方示例 1:[2,7,11,15] + 9 → [0,1]
    ([2, 7, 11, 15], 9, [0, 1]),
    # LC 官方示例 2:[3,2,4] + 6 → [1,2]
    ([3, 2, 4], 6, [1, 2]),
    # LC 官方示例 3:[3,3] + 6 → [0,1](相同值不同下标,不能用同一元素两次)
    ([3, 3], 6, [0, 1]),
    # 边界:负数
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    # 边界:解不在首尾
    ([5, 1, 9, 2, 7], 11, [1, 4]),
]

CASE_IDS = ["示例1", "示例2", "相同值", "负数", "解不在首尾"]


@pytest.mark.parametrize("solver", list(SOLVERS.values()), ids=list(SOLVERS.keys()))
@pytest.mark.parametrize("nums,target,expected", CASES, ids=CASE_IDS)
def test_two_sum(solver, nums, target, expected):
    # 解法可以原地修改 nums;按行拷贝,保护原始用例
    arr = nums[:]
    result = solver(arr, target)
    # 返回下标顺序不限,排序后比较
    assert sorted(result) == sorted(expected)
    # 校验确实是合法解:两个不同下标、和为 target
    i, j = result
    assert i != j
    assert arr[i] + arr[j] == target
