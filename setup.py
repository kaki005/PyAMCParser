from setuptools import find_packages, setup

setup(
    name='amc_parser',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="A lightweight library to parse and visualize asf/amc files",  # 説明
    author='kaki005',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
