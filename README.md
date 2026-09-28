# 食品新国标切换审查台

本仓库保存各接入方已经确认的事件信封、时间和版本约定。示例数据只用于核对共同字段，不代表完整业务实现。

## 测试命令

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 编译或构建命令

```bash
python -m compileall -q src
```

## 使用方式

接入方可读取 `fixtures/event.json`，并通过 `validate_event` 检查事件标识、主体、来源、带时区时间和正整数版本。
