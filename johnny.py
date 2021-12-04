# tucsec ctf
# Johnny Lost his password again, stupid kid.
# Luckily I know that he uses his name and bday as the password 
# (* Sigh, This kid will never learn). Can you help him recovery his 
# password for the 69th time?
# 1969a7f5ff58a5c393a4552696b5dab9c676ab95
# Wrap the password in "TUC{...}" (Use: DDMMYYYY)



import hashlib


password = 'johnny'
for year in range(1900,2021):
	for month in range(1,13):
		for day in range(1,32):
			fullPassword = f"{password}{day:02d}{month:02d}{year:04d}"
			print("trying " + fullPassword)
			m = hashlib.sha1(fullPassword.encode())	
			if m.hexdigest() == '1969a7f5ff58a5c393a4552696b5dab9c676ab95':
				print("Full Password found! It is " + fullPassword)
				exit();
