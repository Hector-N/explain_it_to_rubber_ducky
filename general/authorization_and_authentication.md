# Authorization and Authentication


## SSH protocol?

[What are SSH Keys?](https://jumpcloud.com/blog/what-are-ssh-keys)

SSH protocol (Secure Shell) - is a method to secure remote login from one system to another.  

SHH protocol is widely used to carry out tasks such as issuing remote commands  
and remotely managing network infrastructure and system components.  

In order to use it, we need some pieces of software:
* SSH daemon - on the remote system
* SSH client - on the system used to issue commands

SSH keys - are an authentication method used to gain access to an encrypted connection  
between systems and then use that connection to manage the remote system.  
SSH keys come in many sizes and always come in pairs.  
Every pair is made up of a **privat key** and **public key**.  
If a pair of keys is on user machine - they referred as **user keys**.  
If on a remote system - they're **host keys**.  
**Session keys** - another type of keys used to encrypt a large amount of data being transmitted.  

SSH Key Authentication routine:
1. initiate a connection to the remote system using the SSH protocol
1. remote uses provided username and protocol to determine which public key to use to authenticate client
1. remote uses that public key to encrypt a random challenge message and sends it back to client
1. client decrypts message with privat key, appends session id, and sends it to remote system
1. remote checks for match and authenticates a client

This process proves to the server that you have the corresponding  
private key  to the public key it has on file.

However, the security that this authentication process provides  
can be undermined  when SSH keys are not properly managed.
