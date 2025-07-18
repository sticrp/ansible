#!/usr/bin/env python3
import pexpect
import sys

if len(sys.argv) != 4:
    print("Uso: reboot_ruckus.py <host> <usuario> <senha>")
    sys.exit(1)

host, usuario, senha = sys.argv[1], sys.argv[2], sys.argv[3]

child = pexpect.spawn(f"ssh -o StrictHostKeyChecking=no -tt {host}", timeout=20)

child.expect("Please login:")
child.sendline(usuario)

child.expect("password:")
child.sendline(senha)

child.expect("rkscli:")
child.sendline("reboot")

child.expect("Are you sure you want to reboot.*")
child.sendline("yes")

child.expect(pexpect.EOF)
print(child.before.decode('utf-8', errors='ignore'))
