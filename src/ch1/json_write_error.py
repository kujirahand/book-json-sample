# 不完全なJSON書き込み例
import json

# [エラー] encodingの指定を忘れている --- (※1)
with open('test_error.json', 'w') as fp:
    json.dump('日本語あいうえお', fp, ensure_ascii=False)

# [OK] encodingを正しく指定している --- (※2)
with open('test_ok.json', 'w', encoding='utf-8') as fp:
    json.dump('日本語あいうえお', fp, ensure_ascii=False)

