country = input('請輸入您的國籍：')
age = input('請輸入您的年齡：')
if country == '臺灣' or country == '台灣':
	if int(age) >= 18:
		print('您已符合駕照報考資格。')
	else:
		print('您尚未符合駕照報考資格。')
elif country == '美國':
	if int(age) >= 16:
		print('您已符合駕照報考資格。')
	else:
		print('您尚未符合駕照報考資格。')
else:
	print('請確認您輸入的國籍符合範圍。')