import telnetlib

hostname = 'hostname'
username = 'username'
password = 'password'

tn = telnetlib.Telnet(hostname)
tn.read_until(b"login: ")

tn.write(username.encode('ascii') + b"\n")
if password:
    print(tn.read_until(b"Password:"))
    tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
# tn.write(b"date\n")

tn.write(b"cli\n")
print(tn.read_until(bytes(("%s>" % hostname).encode())).decode('ascii'))

tn.write(b"set cli screen-length 0\n")
print(tn.read_until(bytes(("%s>" % hostname).encode())).decode('ascii'))

tn.write(b"show version\n")
print(tn.read_until(bytes(("%s>" % hostname).encode())).decode('ascii'))

tn.write(b"show configuration|display set\n")
print(tn.read_until(bytes(("%s>" % hostname).encode())).decode('ascii'))

tn.write(b"exit\n")
print(tn.read_until(bytes(("%").encode())).decode('ascii'))

tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
