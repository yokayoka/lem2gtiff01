# lemファイルからGeotiffに変換するスクリプト（フォルダー内一括変換版
# lem2gtiff
# 29 Apr. 2020 by Hiromu Daimaru
# This script is released under the CC BY-NC-SA 4.0.
# https://creativecommons.org/licenses/by-nc-sa/4.0/

import sys
import numpy as np
import pandas as pd
from osgeo import gdal, osr
import glob
import os

def lem2gtiff(mapName, workSpace):
    target_lem = workSpace + '\\' + mapName + '.lem'
    target_csv = workSpace + '\\' + mapName + '.csv'
    header_df = pd.read_csv(target_csv, names = ['item', 'value'], encoding = 'CP932')
    xnum = header_df[header_df["item"] == '東西方向の点数']['value']
    xnum = int(xnum)
    ynum = header_df[header_df["item"] == '南北方向の点数']['value']
    ynum = int(ynum)
    ul_x = header_df[header_df["item"] == '区画左下Y座標']['value']
    ul_x = int(ul_x)/100
    ul_y = header_df[header_df["item"] == '区画左下X座標']['value']
    ul_y = int(ul_y)/100
    h_res = header_df[header_df["item"] == '東西方向のデータ間隔']['value']
    h_res = float(h_res)
    v_res = header_df[header_df["item"] == '南北方向のデータ間隔']['value']
    v_res = float(v_res)
    # 平面直角座標系番号
    geosysnum = header_df[header_df["item"] == '平面直角座標系番号']['value']
    geosysnum = int(geosysnum)
    epsgnum = geosysnum + 2442

    # lemファイルをオープンする
    lem_data = open(target_lem, "r")
    # 行ごとにすべて読み込んでリストデータにする
    lem_lines = lem_data.readlines()

    # 空の配列を作成する
    lem_array = np.empty((0,xnum), int)
    # 1行ずつ配列を追加していく
    for line in lem_lines[0:ynum]:
        line = line.rstrip('\n')
        row_list = [int(line[i: i+ 5]) for i in range(10, len(line), 5)]
        row_arr = np.array(row_list)
        lem_array = np.vstack((lem_array, row_arr))

        # 0.1m単位で書かれているので0.1をかける
    dem_arr = lem_array * 0.1
    #描画順が逆なので上下を反転する
    dem_arr = np.flip(dem_arr, axis = 0)

    drv = gdal.GetDriverByName("GTiff")
    out_tif = pathname + '\\' + mapName + '.tif'
    dem = drv.Create(out_tif, xnum, ynum, 1, gdal.GDT_Float32)
    dem.SetGeoTransform((ul_x, h_res, 0, ul_y, 0, v_res)) # 座標系指定
    srs = osr.SpatialReference() # 空間参照情報
    srs.ImportFromEPSG(epsgnum) # 平面直角3系に座標系を指定
    dem.SetProjection(srs.ExportToWkt()) # 空間情報を結合
    dem.GetRasterBand(1).WriteArray(dem_arr)
    dem.FlushCache()
    dem = None

args = sys.argv
# lem と csv が入っているフォルダー
#pathname = 'D:\\2018Hiroshima\\rinya_data\\lem'
pathname = args[1]

# lem ファイルの存在を確認するためのパラメーター
lem_exp = pathname + '\\*.lem'

# lemファイルのリストを取得
lem_list = [os.path.basename(p) for p in glob.glob(lem_exp)]

# マップ名（拡張子より前の文字列）のリストを湯徳
map_list= [f.rstrip('.lem') for f in lem_list]

for map in map_list:
    lem2gtiff(map, pathname)
