# lem2gtiff
====<BR>
Overview

## Description
日本では航空レーザー測量データの多くはxyz形式かLEMと呼ばれる形式で納品されることが多いようです。植生のように点群として扱いたい場合もありますが、多くの場合は
GeoTiff等の一般的なラスターデータとして利用すると思います。DEMのように規則的なメッシュとなったデータの場合は、LEM形式のデータを利用するのが手っ取り早いと思います。
LEM形式のデータは、図郭名の後に、lemとcsvという2種類の拡張子が付いたファイルで構成されています。
lemは固定長の標高データの繰り返しからなるデータ本体で、csvはデータの位置や格子間隔、投影法等が格納されたファイルです。
lem2gtiffは同一フォルダー内にある大量のlem形式のファイルを一括してgeotiff形式のファイルに変換することを目的に開発しました。
## Demo

## VS.
国土地理院さんなどからLEM形式データを変換するソフトが出されていたりします。ただし、フォルダー内のデータを一括変換するものが見つからなかったので作成してみました。
## Requirement
Python3系の環境で、numpy, pandas, gdalがインストールされている必要があります。

## Usage
gdalが導入されたpythonのターミナル環境から下記のように行います。<BR>
python lem2gtiff01b.py <LEMデータのパス名>
例えば、lemfiles という名前のフォルダーにcsvとlemの複数のセットがある場合は<BR>
<p>python lem2gtiff01.py lemfiles</p>
となります。

## Install
anacondaで環境を構築するのが手っ取り早いと思います。gdalの導入は<a href="https://www.kkaneko.jp/dblab/3dmap/trygeotiff.htmlhttps://www.kkaneko.jp/dblab/3dmap/trygeotiff.html">このサイト</a>などが参考になります。

## Licence
[CC](https://creativecommons.org/licenses/by-nc/4.0/)

## Author
[yokayoka](https://github.com/yokayoka)
