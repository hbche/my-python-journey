# 集成

如何将我们的 Agent Skills 集成到我们的 Agent 或 工具。

## 集成方式

| 方式                 | 说明                                                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 基于文件系统的 Agent | 在计算机环境（bash/unix）中运行，最强大。通过 shell 命令（如 `cat /path/to/my-skill/SKILL.md`）激活 Skill，通过 shell 命令访问捆绑资源。 |
| 基于工具的 Agent     | 没有专用计算机环境，通过实现自定义工具让模型触发 Skill 并访问捆绑资源。具体工具实现由开发者决定。                                        |

## 集成概览

一个兼容 Skills 的 Agent 需要：

1. 发现（Discover）：在配置的目录中扫描 Skills
2. 加载元数据（Load metadata）：启动时加载 name 和 description
3. 匹配（Match）：将用户任务与相关 Skill 匹配
4. 激活（Activate）：加载完整的 Skill 指令
5. 执行（Execute）：按需运行脚本和访问资源

## Skill 发现

Skills 是包含 `SKILL.md` 文件的文件夹。Agent 应扫描配置的目录来查找有效的 Skills。

## 加载元数据

启动时，仅解析每个 `SKILL.md` 的 frontmatter，保持初始上下文占用低。

### 解析 Frontmatter 的伪代码

``` ts
function parseMetadata(skillPath):
    content = readFile(skillPath + "/SKILL.md")
    frontmatter = extractYAMLFrontmatter(content)

    return {
        name: frontmatter.name,
        description: frontmatter.description,
        path: skillPath
    }
}
```

### 注入到上下文中

将 Skill 元数据包含在系统提示词中，让模型知道有哪些 Skills 可用。对于 Claude 模型，推荐使用 XML 格式：

``` xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>Extracts text and tables from PDF files, fills forms, merges documents.</description>
    <location>/path/to/skills/pdf-processing/SKILL.md</location>
  </skill>
  <skill>
    <name>data-analysis</name>
    <description>Analyzes datasets, generates charts, and creates summary reports.</description>
    <location>/path/to/skills/data-analysis/SKILL.md</location>
  </skill>
</available_skills>
```

注意事项：

- 基于文件系统的 Agent：包含 `location` 字段（SKILL.md 的绝对路径）
- 基于工具的 Agent：可以省略 `location`
- 保持元数据简洁，每个 Skill 大约增加 50-100 tokens 的上下文

## 安全考虑

脚本执行会引入安全风险，需要考虑：

- 沙箱化：在隔离环境中运行脚本
- 白名单：仅执行来自受信任 Skills 的脚本
- 确认：在运行潜在危险操作前询问用户
- 日志记录：记录所有脚本执行以供审计

## 参考实现

[skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) 库提供 Python 工具和 CLI：

### validate

- 验证 Skill 目录：
    ``` bash
    skills-ref validate <path>
    ```

validate 流程

```
判断 skill_path 是否存在 + 是否目录
     ↓
在 skill_path 目录下查找 SKILL.md 或 skill.md 文件
     ↓
读取 SKILL.md 或 skill.md 文件内容
     ↓
从 skill md 文件中解析元数据
     ↓
校验并返回解析出来的元数据
```

### to-prompt

- 生成 `<available_skills>` XML:
    ``` bash
    skills-ref to-prompt <path>...
    ```
