# isb
Incremental Searchable Bookmarks.

<!-- toc -->
- [isb](#isb)
  - [概要](#概要)
  - [なぜブラウザのブックマーク機能を使わない？](#なぜブラウザのブックマーク機能を使わない)
  - [動作要件](#動作要件)
  - [デモ](#デモ)
  - [使い方](#使い方)
    - [linklist.md のフォーマット](#linklistmd-のフォーマット)
    - [検索について](#検索について)
  - [FAQ](#faq)
    - [Q: 生成された HTML をローカルで IE で開くと警告が出て動作しない](#q-生成された-html-をローカルで-ie-で開くと警告が出て動作しない)
  - [License](#license)
  - [Author](#author)

## 概要
インクリメンタルサーチが可能なブックマークツール。

Markdown 形式で URL とコメントを書いといて、それをビルドして HTML ファイルを生成。このファイルをブラウザで開く。インクリメンタルサーチ機能があるのでブックマーク数を絞り込むのも容易。

## なぜブラウザのブックマーク機能を使わない？
IE のみサポートするウェブサイトやシステムを多数扱う必要があるが、IE のブックマーク管理機能は非常に使いづらい（Firefox とは段違いである）。代替手段が欲しかった。

## 動作要件
- Python3 (動作確認は Python3.6 on Windows7/10)

## デモ
[linklist.md](linklist.md) こんなファイルを書いてビルドすると、

↓

[index.html](index.html) こんなファイルが生成されます。サンプルは [GitHub Pages](https://stakiran.github.io/isb/index.html) にも置いてます。

## 使い方
- (1) linklist.md にブックマークを書く
- (2) template.html に生成 HTML のテンプレートを書く
  - ``{{body}}`` 部分にブックマーク内容が入ります
- (3) python builder.py を実行して HTML を生成する
  - Windows なら builder.py のラッパーバッチ build.bat を用意しているので、これを叩くだけでビルドできます
  - builder.py に与えるファイル名は linklist.md 固定じゃなくても良いです(--input と --output と --template の三引数を与えれば何でもいいです)

### linklist.md のフォーマット
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

### 検索について
- 大文字/小文字を区別しません
- スペースで区切ると AND 検索になります

## FAQ

### Q: 生成された HTML をローカルで IE で開くと警告が出て動作しない
A: インターネットオプション > 詳細設定タブ > セキュリティ の「マイコンピュータのファイルでのアクティブコンテンツの実行を許可する」をオンにしてください。

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
