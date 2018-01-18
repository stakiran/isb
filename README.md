# isb
Incremental Searchable Bookmarks.

<!-- toc -->
- [isb](#isb)
  - [Overview](#overview)
  - [Why?](#why)
  - [Requirement](#requirement)
  - [Demo](#demo)
  - [How to build](#how-to-build)
  - [linklist.md のフォーマット](#linklistmd-のフォーマット)
  - [FAQ](#faq)
    - [Q: 生成された HTML をローカルで IE で開くと警告が出て動作しない](#q-生成された-html-をローカルで-ie-で開くと警告が出て動作しない)
  - [License](#license)
  - [Author](#author)

## Overview
インクリメンタルサーチが可能なブックマークツール。

Markdown 形式で URL とコメントを書いといて、それをビルドして HTML ファイルを生成。このファイルをブラウザで開く。インクリメンタルサーチ機能があるのでブックマーク数を絞り込むのも容易。

## Why?
IE のみサポートするウェブサイトやシステムを多数扱う必要があるが、IE のブックマーク管理機能は非常に使いづらい（Firefox とは段違いである）。代替手段が欲しかった。

## Requirement
- Python 3 (Tested on Python 3.6 and Windows 7+)

## Demo
[linklist.md](linklist.md) こんなファイルを書いてビルドすると、

↓

[index.html](index.html) こんなファイルが生成されます。サンプルは [GitHub Pages](https://stakiran.github.io/isb/index.html) にも置いてます。

## How to build
- (1) linklist.md にブックマークを書く
- (2) template.html に生成 HTML のテンプレートを書く
  - ``{{body}}`` 部分にブックマーク内容が入ります
- (3) python builder.py を実行して HTML を生成する
  - Windows なら builder.py のラッパーバッチ build.bat を用意しているので、これを叩くだけでビルドできます
  - builder.py に与えるファイル名は linklist.md 固定じゃなくても良いです(--input と --output と --template の三引数を与えれば何でもいいです)

## linklist.md のフォーマット
見出し:

```
# (見出し名)
```

ブックマーク一件:

```
- (ブックマーク名),(URL) (サーチで引っ掛ける用のキーワード)
```

コメント（生成HTMLには出力されない）:

```
; コメント
```

テキスト（ブックマークではなく単なるテキストを挿入する）:

```
* (テキスト)
```

## FAQ

### Q: 生成された HTML をローカルで IE で開くと警告が出て動作しない
A: インターネットオプション > 詳細設定タブ > セキュリティ の「マイコンピュータのファイルでのアクティブコンテンツの実行を許可する」をオンにしてください。

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
