ion decisions are immediately available
   - Architectural patterns and code insights are preserved
   - Project history and rationale are maintained

3. **Intelligent Context Building**
   - Serena MCP provides relevant memories based on current work
   - Past solutions and patterns inform new implementations
   - Project evolution is tracked and understood

### Memory Optimization

**Effective Memory Usage**:
- Use descriptive, searchable memory names
- Include project phase and timestamp context
- Reference specific features or architectural decisions
- Make future retrieval intuitive

**Memory Content Strategy**:
- Store decisions and rationale, not just outcomes
- Include alternative approaches considered
- Document integration patterns and dependencies
- Preserve learning and insights for future reference

**Memory Lifecycle Management**:
- Regular cleanup of outdated memories
- Consolidation of related session memories
- Archiving of completed project phases
- Pruning of obsolete architectural decisions

## Best Practices for Persistent Sessions

### Session Start Protocol
1. Always begin with `/sc:load` for existing projects
2. Use `/sc:reflect` to understand current state from memory
3. Plan work based on persistent context and stored patterns
4. Build on previous decisions and architectural choices

### Session End Protocol
1. Use `/sc:reflect` to assess completeness against stored goals
2. Save key decisions with `/sc:save` for future sessions
3. Document next steps and open questions in memory
4. Preserve context for seamless future continuation

### Memory Quality Maintenance
- Use clear, descriptive memory names for easy retrieval
- Include context about decisions and alternative approaches
- Reference specific code locations and patterns
- Maintain consistency in memory structure across sessions

## Integration with Other SuperClaude Features

### MCP Server Coordination
- **Serena MCP**: Provides the persistent memory infrastructure
- **Sequential MCP**: Uses stored memories for enhanced complex analysis
- **Context7 MCP**: References stored patterns and documentation approaches
- **Morphllm MCP**: Applies stored refactoring patterns consistently

### Agent Collaboration with Memory
- Agents access persistent memories for enhanced context
- Previous specialist decisions are preserved and referenced
- Cross-session agent coordination through shared memory
- Consistent specialist recommendations based on project history

### Command Integration with Persistence
- All `/sc:` commands can reference and build on persistent context
- Previous command outputs and decisions are available across sessions
- Workflow patterns are stored and reusable
- Implementation history guides future command decisions

## Troubleshooting Persistent Sessions

### Common Issues

**Memory Not Loading**:
- Verify Serena MCP is configured and running properly
- Check memory file permissions and accessibility
- Ensure consistent project naming conventions
- Validate memory file integrity and format

**Context Loss Between Sessions**:  
- Always use `/sc:save` before ending sessions
- Use descriptive memory names for easy retrieval
- Regular `/sc:reflect` to validate memory completeness
- Backup important memory files periodically

**Memory Conflicts**:
- Use timestamped memory names for version control
- Regular cleanup of obsolete memories
- Clear separation between project and session memories
- Consistent memory naming conventions across sessions

### Quick Fixes

**Reset Session State**:
```bash
/sc:load --fresh  # Start without previous context
/sc:reflect       # Assess current state
```

**Memory Cleanup**:
```bash
/sc:reflect --cleanup  # Remove obsolete memories
/sc:save --consolidate # Merge related memories
```

**Context Recovery**:
```bash
/sc:load --recent     # Load most recent memories
/sc:reflect --repair  # Identify and fix context gaps
```

## Advanced Persistent Session Patterns

### Multi-Phase Projects
- Use phase-specific memory naming for organization
- Maintain architectural decision continuity across phases
- Cross-phase dependency tracking through persistent memory
- Progressive complexity management with historical context

### Team Collaboration
- Shared memory conventions and naming standards
- Decision rationale preservation for team context
- Integration pattern documentation accessible to all team members
- Consistent code style and architecture enforcement through memory

### Long-Term Maintenance
- Memory archiving strategies for completed projects
- Pattern library development through accumulated memories
- Reusable solution documentation built over time
- Knowledge base building through persistent memory accumulation

## Key Benefits of Persistent Session Management

### Project Continuity
- Seamless work continuation across multiple conversations
- No context loss between Claude Code sessions
- Preserved architectural decisions and technical rationale
- Long-term project evolution tracking

### Enhanced Productivity
- Reduced need to re-explain project context
- Faster startup time for continued work
- Building on previous insights and patterns
- Cumulative project knowledge growth

### Quality Consistency
- Consistent architectural patterns across sessions
- Preserved code quality decisions and standards
- Reusable solutions and best practices
- Maintained technical debt awareness

---

**Key Takeaway**: Session management through Serena MCP transforms SuperClaude from single-conversation assistance to persistent project partnership, maintaining context, decisions, and learning across all development phases and Claude Code conversations.


================================================
FILE: docs/user-guide-jp/commands.md
================================================
# SuperClaude コマンドガイド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#superclaude-commands-guide)

`/sc:*`SuperClaude は、ワークフロー用コマンドと`@agent-*`スペシャリスト用コマンドの 21 個の Claude Code コマンドを提供します。

## コマンドの種類

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#command-types)

|タイプ|使用場所|形式|例|
|---|---|---|---|
|**スラッシュコマンド**|クロード・コード|`/sc:[command]`|`/sc:implement "feature"`|
|**エージェント**|クロード・コード|`@agent-[name]`|`@agent-security "review"`|
|**インストール**|ターミナル|`SuperClaude [command]`|`SuperClaude install`|

## クイックテスト

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#quick-test)

```shell
# Terminal: Verify installation
python3 -m SuperClaude --version
# Claude Code CLI verification: claude --version

# Claude Code: Test commands
/sc:brainstorm "test project"    # Should ask discovery questions
/sc:analyze README.md           # Should provide analysis
```

**ワークフロー**：`/sc:brainstorm "idea"`→→`/sc:implement "feature"`​`/sc:test`

## 🎯 SuperClaude コマンドの理解

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#-understanding-superclaude-commands)

## SuperClaudeの仕組み

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#how-superclaude-works)

SuperClaude は、Claude Code が特殊な動作を実行するために読み込む動作コンテキストファイルを提供します。 と入力すると`/sc:implement`、Claude Code は`implement.md`コンテキストファイルを読み込み、その動作指示に従います。

**SuperClaude コマンドはソフトウェアによって実行されるのではなく**、フレームワークから特殊な命令ファイルを読み取ることで Claude コードの動作を変更するコンテキスト トリガーです。

### コマンドの種類:

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#command-types-1)

- **スラッシュコマンド**（`/sc:*`）：ワークフローパターンと動作​​モードをトリガーする
- **エージェントの呼び出し**（`@agent-*`）：特定のドメインスペシャリストを手動で起動する
- **フラグ**（`--think`、`--safe-mode`）：コマンドの動作と深さを変更する

### コンテキストメカニズム:

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#the-context-mechanism)

1. **ユーザー入力**: 入力する`/sc:implement "auth system"`
2. **コンテキスト読み込み**: クロードコード読み取り`~/.claude/superclaude/Commands/implement.md`
3. **行動の採用**：クロードはドメインの専門知識、ツールの選択、検証パターンを適用します
4. **強化された出力**: セキュリティ上の考慮事項とベストプラクティスを備えた構造化された実装

**重要なポイント**: これにより、従来のソフトウェア実行ではなくコンテキスト管理を通じて洗練された開発ワークフローが作成されます。

### インストールコマンドと使用コマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#installation-vs-usage-commands)

**🖥️ ターミナルコマンド**（実際の CLI ソフトウェア）：

- `SuperClaude install`- フレームワークコンポーネントをインストールします
- `SuperClaude update`- 既存のインストールを更新します
- `SuperClaude uninstall`- フレームワークのインストールを削除します
- `python3 -m SuperClaude --version`- インストール状態を確認する

**💬 クロード コード コマンド**(コンテキスト トリガー):

- `/sc:brainstorm`- 要件検出コンテキストをアクティブ化します
- `/sc:implement`- 機能開発コンテキストをアクティブ化します
- `@agent-security`- セキュリティスペシャリストのコンテキストをアクティブ化します
- すべてのコマンドはClaude Codeチャットインターフェース内でのみ機能します

> **クイック スタート**: `/sc:brainstorm "your project idea"`→ `/sc:implement "feature name"`→を試して`/sc:test`、コア ワークフローを体験してください。

## 🧪 セットアップのテスト

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#-testing-your-setup)

### 🖥️ ターミナル検証（ターミナル/CMDで実行）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#%EF%B8%8F-terminal-verification-run-in-terminalcmd)

```shell
# Verify SuperClaude is working (primary method)
python3 -m SuperClaude --version
# Example output: SuperClaude 4.1.5

# Claude Code CLI version check
claude --version

# Check installed components
python3 -m SuperClaude install --list-components | grep mcp
# Example output: Shows installed MCP components
```

### 💬 クロードコードテスト（クロードコードチャットに入力）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#-claude-code-testing-type-in-claude-code-chat)

```
# Test basic /sc: command
/sc:brainstorm "test project"
# Example behavior: Interactive requirements discovery starts

# Test command help
/sc:help
# Example behavior: List of available commands
```

**テストが失敗した場合**:[インストールガイド](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/getting-started/installation.md)または[トラブルシューティングを確認してください](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#troubleshooting)

### 📝 コマンドクイックリファレンス

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#-command-quick-reference)

|コマンドタイプ|走る場所|形式|目的|例|
|---|---|---|---|---|
|**🖥️ インストール**|ターミナル/CMD|`SuperClaude [command]`|セットアップとメンテナンス|`SuperClaude install`|
|**🔧 構成**|ターミナル/CMD|`python3 -m SuperClaude [command]`|高度な設定|`python3 -m SuperClaude --version`|
|**💬 スラッシュコマンド**|クロード・コード|`/sc:[command]`|ワークフロー自動化|`/sc:implement "feature"`|
|**🤖 エージェントの呼び出し**|クロード・コード|`@agent-[name]`|手動スペシャリストの有効化|`@agent-security "review"`|
|**⚡ 強化されたフラグ**|クロード・コード|`/sc:[command] --flags`|行動修正|`/sc:analyze --think-hard`|

> **注意**：すべての`/sc:`コマンドと`@agent-`呼び出しは、ターミナルではなくClaude Codeチャット内で動作します。これらのコマンドと呼び出しは、Claude CodeがSuperClaudeフレームワークから特定のコンテキストファイルを読み取るようにトリガーします。

## 目次

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#table-of-contents)

- [必須コマンド](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#essential-commands)- ここから始めましょう（8つのコアコマンド）
- [一般的なワークフロー](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#common-workflows)- 機能するコマンドの組み合わせ
- [完全なコマンドリファレンス](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#full-command-reference)- カテゴリ別に整理された全21個のコマンド
- [トラブルシューティング](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#troubleshooting)- よくある問題と解決策
- [コマンドインデックス](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#command-index)- カテゴリ別にコマンドを検索

---

## 必須コマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#essential-commands)

**即時の生産性向上のためのコアワークフロー コマンド:**

### `/sc:brainstorm`- プロジェクト発見

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scbrainstorm---project-discovery)

**目的**: 対話型の要件検出とプロジェクト計画  
**構文**:`/sc:brainstorm "your idea"` `[--strategy systematic|creative]`

**ユースケース**:

- 新しいプロジェクトの計画:`/sc:brainstorm "e-commerce platform"`
- 機能の探索:`/sc:brainstorm "user authentication system"`
- 問題解決:`/sc:brainstorm "slow database queries"`

### `/sc:implement`- 機能開発

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scimplement---feature-development)

**目的**: インテリジェントなスペシャリストルーティングによるフルスタック機能の実装  
**構文**:`/sc:implement "feature description"` `[--type frontend|backend|fullstack] [--focus security|performance]`

**ユースケース**:

- 認証:`/sc:implement "JWT login system"`
- UI コンポーネント:`/sc:implement "responsive dashboard"`
- API:`/sc:implement "REST user endpoints"`
- データベース:`/sc:implement "user schema with relationships"`

### `/sc:analyze`- コード評価

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scanalyze---code-assessment)

**目的**: 品質、セキュリティ、パフォーマンスにわたる包括的なコード分析  
**構文**:`/sc:analyze [path]` `[--focus quality|security|performance|architecture]`

**ユースケース**:

- プロジェクトの健全性:`/sc:analyze .`
- セキュリティ監査:`/sc:analyze --focus security`
- パフォーマンスレビュー:`/sc:analyze --focus performance`

### `/sc:troubleshoot`- 問題診断

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#sctroubleshoot---problem-diagnosis)

**目的**: 根本原因分析による体系的な問題診断  
**構文**:`/sc:troubleshoot "issue description"` `[--type build|runtime|performance]`

**ユースケース**:

- ランタイムエラー:`/sc:troubleshoot "500 error on login"`
- ビルドの失敗:`/sc:troubleshoot --type build`
- パフォーマンスの問題:`/sc:troubleshoot "slow page load"`

### `/sc:test`- 品質保証

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#sctest---quality-assurance)

**目的**: カバレッジ分析による包括的なテスト  
**構文**:`/sc:test` `[--type unit|integration|e2e] [--coverage] [--fix]`

**ユースケース**:

- 完全なテストスイート:`/sc:test --coverage`
- ユニットテスト:`/sc:test --type unit --watch`
- E2E検証:`/sc:test --type e2e`

### `/sc:improve`- コード強化

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scimprove---code-enhancement)

**目的**: 体系的なコードの改善と最適化を適用する  
**構文**:`/sc:improve [path]` `[--type performance|quality|security] [--preview]`

**ユースケース**:

- 一般的な改善点:`/sc:improve src/`
- パフォーマンスの最適化:`/sc:improve --type performance`
- セキュリティ強化:`/sc:improve --type security`

### `/sc:document`- ドキュメント生成

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scdocument---documentation-generation)

**目的**: コードとAPIの包括的なドキュメントを生成する  
**構文**:`/sc:document [path]` `[--type api|user-guide|technical] [--format markdown|html]`

**ユースケース**:

- APIドキュメント:`/sc:document --type api`
- ユーザーガイド:`/sc:document --type user-guide`
- 技術ドキュメント:`/sc:document --type technical`

### `/sc:workflow`- 実装計画

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#scworkflow---implementation-planning)

**目的**: 要件から構造化された実装計画を生成する  
**構文**:`/sc:workflow "feature description"` `[--strategy agile|waterfall] [--format markdown]`

**ユースケース**:

- 機能計画:`/sc:workflow "user authentication"`
- スプリント計画:`/sc:workflow --strategy agile`
- アーキテクチャ計画：`/sc:workflow "microservices migration"`

---

## 一般的なワークフロー

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#common-workflows)

**実証済みのコマンドの組み合わせ:**

### 新しいプロジェクトのセットアップ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#new-project-setup)

```shell
/sc:brainstorm "project concept"      # Define requirements
/sc:design "system architecture"      # Create technical design  
/sc:workflow "implementation plan"    # Generate development roadmap
```

### 機能開発

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#feature-development)

```shell
/sc:implement "feature name"          # Build the feature
/sc:test --coverage                   # Validate with tests
/sc:document --type api               # Generate documentation  
```

### コード品質の改善

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#code-quality-improvement)

```shell
/sc:analyze --focus quality           # Assess current state
/sc:improve --preview                 # Preview improvements
/sc:test --coverage                   # Validate changes
```

### バグ調査

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#bug-investigation)

```shell
/sc:troubleshoot "issue description"  # Diagnose the problem
/sc:analyze --focus problem-area      # Deep analysis
/sc:improve --fix --safe-mode         # Apply targeted fixes
```

## 完全なコマンドリファレンス

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#full-command-reference)

### 開発コマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#development-commands)

|指示|目的|最適な用途|
|---|---|---|
|**ワークフロー**|実施計画|プロジェクトロードマップ、スプリント計画|
|**埋め込む**|機能開発|フルスタック機能、API開発|
|**建てる**|プロジェクトのコンパイル|CI/CD、プロダクションビルド|
|**デザイン**|システムアーキテクチャ|API仕様、データベーススキーマ|

### 分析コマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#analysis-commands)

|指示|目的|最適な用途|
|---|---|---|
|**分析する**|コード評価|品質監査、セキュリティレビュー|
|**トラブルシューティング**|問題診断|バグ調査、パフォーマンスの問題|
|**説明する**|コードの説明|学習、コードレビュー|

### 品質コマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#quality-commands)

|指示|目的|最適な用途|
|---|---|---|
|**改善する**|コード強化|パフォーマンスの最適化、リファクタリング|
|**掃除**|技術的負債|デッドコードの削除、整理|
|**テスト**|品質保証|テスト自動化、カバレッジ分析|
|**書類**|ドキュメント|APIドキュメント、ユーザーガイド|

### プロジェクト管理

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#project-management)

|指示|目的|最適な用途|
|---|---|---|
|**見積もり**|プロジェクト見積もり|タイムライン計画、リソース割り当て|
|**タスク**|タスク管理|複雑なワークフロー、タスク追跡|
|**スポーン**|メタオーケストレーション|大規模プロジェクト、並列実行|

### ユーティリティコマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#utility-commands)

|指示|目的|最適な用途|
|---|---|---|
|**ギット**|バージョン管理|コミット管理、ブランチ戦略|
|**索引**|コマンド検出|機能の探索、コマンドの検索|

### セッションコマンド

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#session-commands)

|指示|目的|最適な用途|
|---|---|---|
|**負荷**|コンテキストの読み込み|セッションの初期化、プロジェクトのオンボーディング|
|**保存**|セッションの永続性|チェックポイント、コンテキスト保存|
|**反映する**|タスクの検証|進捗評価、完了検証|
|**選択ツール**|ツールの最適化|パフォーマンスの最適化、ツールの選択|

---

## コマンドインデックス

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#command-index)

**機能別:**

- **計画**：ブレインストーミング、設計、ワークフロー、見積もり
- **開発**：実装、ビルド、git
- **分析**：分析、トラブルシューティング、説明
- **品質**: 改善、クリーンアップ、テスト、ドキュメント化
- **管理**: タスク、スポーン、ロード、保存、反映
- **ユーティリティ**: インデックス、選択ツール

**複雑さ別:**

- **初心者**：ブレインストーミング、実装、分析、テスト
- **中級**：ワークフロー、設計、改善、ドキュメント
- **上級**：スポーン、タスク、選択ツール、リフレクト

## トラブルシューティング

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#troubleshooting)

**コマンドの問題:**

- **コマンドが見つかりません**: インストールを確認してください:`python3 -m SuperClaude --version`
- **応答なし**: Claude Codeセッションを再開する
- **処理遅延**: `--no-mcp`MCPサーバーなしでテストするために使用します

**クイックフィックス:**

- セッションをリセット:`/sc:load`再初期化する
- ステータスを確認:`SuperClaude install --list-components`
- ヘルプ:[トラブルシューティングガイド](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/reference/troubleshooting.md)

## 次のステップ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/commands.md#next-steps)

- [フラグガイド](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md)- コマンドの動作を制御する
- [エージェントガイド](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/agents.md)- スペシャリストのアクティベーション
- [例のクックブック](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/reference/examples-cookbook.md)- 実際の使用パターン


================================================
FILE: docs/user-guide-jp/flags.md
================================================
# SuperClaude フラグガイド 🏁

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#superclaude-flags-guide-)

**ほとんどのフラグは自動的にアクティブになります**。Claude Code は、リクエスト内のキーワードとパターンに基づいて適切なコンテキストを実行するための動作指示を読み取ります。

## 必須の自動アクティベーションフラグ（ユースケースの90%）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#essential-auto-activation-flags-90-of-use-cases)

### コア分析フラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#core-analysis-flags)

|フラグ|起動時|何をするのか|
|---|---|---|
|`--think`|5つ以上のファイルまたは複雑な分析|標準的な構造化分析（約4Kトークン）|
|`--think-hard`|アーキテクチャ分析、システム依存関係|強化されたツールによる詳細な分析（約1万トークン）|
|`--ultrathink`|重要なシステムの再設計、レガシーシステムの近代化|すべてのツールで最大深度分析（約32Kトークン）|

### MCP サーバーフラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#mcp-server-flags)

|フラグ|サーバ|目的|自動トリガー|
|---|---|---|---|
|`--c7`/`--context7`|コンテキスト7|公式ドキュメント、フレームワークパターン|ライブラリのインポート、フレームワークに関する質問|
|`--seq`/`--sequential`|一連|多段階推論、デバッグ|複雑なデバッグ、システム設計|
|`--magic`|魔法|UIコンポーネント生成|`/ui`コマンド、フロントエンドキーワード|
|`--play`/`--playwright`|劇作家|ブラウザテスト、E2E検証|テスト要求、視覚的検証|
|`--morph`/`--morphllm`|モルフィム|一括変換、パターン編集|一括操作、スタイルの強制|
|`--serena`|セレナ|プロジェクトメモリ、シンボル操作|シンボル操作、大規模なコードベース|

### 動作モードフラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#behavioral-mode-flags)

|フラグ|起動時|何をするのか|
|---|---|---|
|`--brainstorm`|漠然とした要望、探索キーワード|共同発見のマインドセット|
|`--introspect`|自己分析、エラー回復|推論プロセスを透明性を持って公開する|
|`--task-manage`|>3ステップ、複雑なスコープ|委任を通じて調整する|
|`--orchestrate`|マルチツール操作、パフォーマンスニーズ|ツールの選択と並列実行の最適化|
|`--token-efficient`/`--uc`|コンテキスト >75%、効率性のニーズ|シンボル強化通信、30～50%削減|

### 実行制御フラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#execution-control-flags)

|フラグ|起動時|何をするのか|
|---|---|---|
|`--loop`|「改善する」「磨く」「洗練する」というキーワード|反復的な強化サイクル|
|`--safe-mode`|生産、リソース使用率85%以上|最大限の検証、慎重な実行|
|`--validate`|リスク >0.7、本番環境|実行前のリスク評価|
|`--delegate`|>7 ディレクトリまたは >50 ファイル|サブエージェント並列処理|

## コマンド固有のフラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#command-specific-flags)

### 分析コマンドフラグ（`/sc:analyze`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#analysis-command-flags-scanalyze)

|フラグ|目的|価値観|
|---|---|---|
|`--focus`|特定のドメインをターゲットとする|`security`、、、、`performance`​`quality`​`architecture`|
|`--depth`|分析の徹底性|`quick`、`deep`|
|`--format`|出力形式|`text`、、`json`​`report`|

### ビルドコマンドフラグ（`/sc:build`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#build-command-flags-scbuild)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|ビルド構成|`dev`、、`prod`​`test`|
|`--clean`|ビルド前にクリーンアップ|ブール値|
|`--optimize`|最適化を有効にする|ブール値|
|`--verbose`|詳細な出力|ブール値|

### 設計コマンドフラグ（`/sc:design`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#design-command-flags-scdesign)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|設計目標|`architecture`、、、、`api`​`component`​`database`|
|`--format`|出力形式|`diagram`、、`spec`​`code`|

### コマンドフラグの説明（`/sc:explain`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#explain-command-flags-scexplain)

|フラグ|目的|価値観|
|---|---|---|
|`--level`|複雑さのレベル|`basic`、、`intermediate`​`advanced`|
|`--format`|説明スタイル|`text`、、`examples`​`interactive`|
|`--context`|ドメインコンテキスト|任意のドメイン（例：`react`、`security`）|

### コマンドフラグの改善（`/sc:improve`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#improve-command-flags-scimprove)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|改善の焦点|`quality`、、、、、`performance`​`maintainability`​`style`​`security`|
|`--safe`|保守的なアプローチ|ブール値|
|`--interactive`|ユーザーガイダンス|ブール値|
|`--preview`|実行せずに表示する|ブール値|

### タスクコマンドフラグ（`/sc:task`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#task-command-flags-sctask)

|フラグ|目的|価値観|
|---|---|---|
|`--strategy`|タスクアプローチ|`systematic`、、`agile`​`enterprise`|
|`--parallel`|並列実行|ブール値|
|`--delegate`|サブエージェントの調整|ブール値|

### ワークフローコマンドフラグ（`/sc:workflow`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#workflow-command-flags-scworkflow)

|フラグ|目的|価値観|
|---|---|---|
|`--strategy`|ワークフローアプローチ|`systematic`、、`agile`​`enterprise`|
|`--depth`|分析の深さ|`shallow`、、`normal`​`deep`|
|`--parallel`|並列調整|ブール値|

### コマンドフラグのトラブルシューティング ( `/sc:troubleshoot`)

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#troubleshoot-command-flags-sctroubleshoot)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|問題カテゴリ|`bug`、、、、`build`​`performance`​`deployment`|
|`--trace`|トレース分析を含める|ブール値|
|`--fix`|修正を適用する|ブール値|

### クリーンアップコマンドフラグ（`/sc:cleanup`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#cleanup-command-flags-sccleanup)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|クリーンアップ対象|`code`、、、、`imports`​`files`​`all`|
|`--safe`/`--aggressive`|清掃強度|ブール値|
|`--interactive`|ユーザーガイダンス|ブール値|
|`--preview`|実行せずに表示する|ブール値|

### コマンドフラグの推定（`/sc:estimate`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#estimate-command-flags-scestimate)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|焦点を推定する|`time`、、`effort`​`complexity`|
|`--unit`|時間単位|`hours`、、`days`​`weeks`|
|`--breakdown`|詳細な内訳|ブール値|

### インデックスコマンドフラグ（`/sc:index`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#index-command-flags-scindex)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|インデックスターゲット|`docs`、、、、`api`​`structure`​`readme`|
|`--format`|出力形式|`md`、、`json`​`yaml`|

### コマンドフラグを反映する ( `/sc:reflect`)

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#reflect-command-flags-screflect)

|フラグ|目的|価値観|
|---|---|---|
|`--type`|反射スコープ|`task`、、`session`​`completion`|
|`--analyze`|分析を含める|ブール値|
|`--validate`|完全性を検証する|ブール値|

### スポーンコマンドフラグ（`/sc:spawn`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#spawn-command-flags-scspawn)

|フラグ|目的|価値観|
|---|---|---|
|`--strategy`|調整アプローチ|`sequential`、、`parallel`​`adaptive`|
|`--depth`|分析の深さ|`normal`、`deep`|

### Gitコマンドフラグ（`/sc:git`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#git-command-flags-scgit)

|フラグ|目的|価値観|
|---|---|---|
|`--smart-commit`|コミットメッセージを生成する|ブール値|
|`--interactive`|ガイド付き操作|ブール値|

### 選択ツールコマンドフラグ ( `/sc:select-tool`)

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#select-tool-command-flags-scselect-tool)

|フラグ|目的|価値観|
|---|---|---|
|`--analyze`|ツール分析|ブール値|
|`--explain`|選択の説明|ブール値|

### テストコマンドフラグ（`/sc:test`）

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#test-command-flags-sctest)

|フラグ|目的|価値観|
|---|---|---|
|`--coverage`|カバー範囲を含める|ブール値|
|`--type`|テストの種類|`unit`、、`integration`​`e2e`|
|`--watch`|ウォッチモード|ブール値|

## 高度な制御フラグ

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#advanced-control-flags)

### 範囲と焦点

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#scope-and-focus)

|フラグ|目的|価値観|
|---|---|---|
|`--scope`|分析境界|`file`、、、、`module`​`project`​`system`|
|`--focus`|ドメインターゲティング|`performance`、、、、、、`security`​`quality`​`architecture`​`accessibility`​`testing`|

### 実行制御

[](https://github.com/khayashi4337/SuperClaude_Framework/blob/master/docs/user-guide/flags.md#execution-control)

|フラグ|目的|価値観|
|---|---|---|
|`--concurren