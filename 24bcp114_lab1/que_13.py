# Convert bytes into KB, MB and GB.
by=int(input("Enter the bytes:"))
kb=0.001*by
mb=by/(10**6)
gb=by/(10**9)
print("kb:",kb)
print("mb:",mb)
print("gb:",gb)