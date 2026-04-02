import sys
import math

def normalize_vector():
    # コマンドライン引数のチェック
    if len(sys.argv) < 2:
        print("Usage: python normalize.py x,y,z")
        return

    try:
        # '4,3,0' のような文字列を数値のリストに変換
        input_str = sys.argv[1]
        coords = [float(n) for n in input_str.split(',')]

        if len(coords) != 3:
            print("Error: 3つの数値をカンマ区切りで入力してください (例: 4,3,0)")
            return

        x, y, z = coords

        # ベクトルの長さ（ノルム）を計算
        length = math.sqrt(x**2 + y**2 + z**2)

        if length == 0:
            print("Error: ゼロベクトルは正規化できません")
            return

        # 各要素を長さで割る
        nx = x / length
        ny = y / length
        nz = z / length

        # 結果をカンマ区切りで出力（末尾の.0を省くため、必要に応じてフォーマット）
        print(f"{nx:g},{ny:g},{nz:g}")

    except ValueError:
        print("Error: 数値を正しく入力してください")

if __name__ == "__main__":
    normalize_vector()