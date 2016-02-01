import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP: %s" % totp.now())
