# 版权与保全（Proof）

- 版权：© Ghost-Lily Research 2025 | CC-BY-NC-ND（文本/图）| MIT（代码）
- 哈希：发布时在此记录各文件 SHA256
- 时间戳：建议同步提交到链上（例如：TX: <txid>）

生成哈希（示例）：
```bash
python - <<'PY'
import hashlib, sys, pathlib
for p in pathlib.Path('.').rglob('*'):
    if p.is_file():
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        print(h, p)
PY
```
