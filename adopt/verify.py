# -*- coding: utf-8 -*-
"""校验 Agent 宪法文本是否与 canonical 哈希一致。

用法：
    python verify.py <文件路径或 URL>
输出：
    OK  <sha256>   与 v1.3.0 canonical 一致
    FAIL <sha256>  不一致（或文件被改动）
"""
import hashlib
import sys
import urllib.request

CANONICAL = "f97de165398004a37c819b93c3a5c35abc6587c568acc278f5626dd4fc32e37c"


def load(src: str) -> bytes:
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": "agent-constitution-verify/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    with open(src, "rb") as f:
        return f.read()


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    digest = hashlib.sha256(load(sys.argv[1])).hexdigest()
    if digest == CANONICAL:
        print(f"OK  {digest}")
        return 0
    print(f"FAIL {digest}\n     expected {CANONICAL}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
