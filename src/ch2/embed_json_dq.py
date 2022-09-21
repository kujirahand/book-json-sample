# もしもダブルクォートでJSON文字列を表現する場合
json_str = "" + \
  "{\"tokyo\": [{\"date\": \"6日(水)\"," + \
  "\"forecast\": \"曇\"}, " + \
  "{\"date\": \"7日(木)\", \"forecast\": \"晴\"}]}"
print(json_str)

