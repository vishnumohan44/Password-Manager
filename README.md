# Password-Manager

The PASSWORD MANAGER is a program that helps you manage your passwords.

You can do the following operations on this program:
1. Create Password Vault
2. Add an entry to your Vault
3. Display all usernames in a Vault
4. Modify password
5. Forgot your password
6. Delete an entry from your Vault
7. Display all Vaults
8. Delete Vault

This is a wide platform where you can create any number of password vaults and differentiate all your passwords effectively.
```
EXAMPLE: You can create two different Vaults namely 'Office' and 'Personal'. You can store all your Office password 
in 'Office-Vault' and all your personal passwords in 'Personal-Vault'.
```
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
```
Requirements:
1. Python 3
2. MySQL
3. Install mysql connector - Type "pip install mysql-connector" in command prompt shell if you donot have.
```
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
```
Instructions:
1. Store the FOLLOWING FILES TOGETHER in a single folder:
   file.py
   base.py
   main.py
2. Run  "main.py"  ONLY.
3. Input YOUR directory username and password to connect to your database, after which, the connection process will start.
   Eg: user=root  ,  password=1234  (input your database details only)
4. Once connected, you will be able to use the application.
```
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
```
In order to gain access to the application, you must type in the MASTER PASSWORD.
‏
MASTER PASSWORD : "1t520th1n6"
```
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------

## NOTE: PLEASE GO THROUGH THIS BEFORE YOU START USING THE APPLICATION
```
1. A PasswordVault once created, cannot be created a second time unless the first one is deleted.
   Eg: Once a Vaultname 'Random' is created, another Vault with the same name cannot be created until this existing Vault is 
   deleted.
   NOTE: Donot use any other symbols ( !@#$%^&*()\|, etc ) or space when creating a new password vault (only letters along 
   with numbers, numbers alone will lead to error).

2. Similarly, when inside a vault, if a username exists, another entry with the same username cannot be registered.
   Eg: Inside vault 'Random', suppose a username 'John' exists. Another entry with the same username cannot be added to this 
   vault unless the existing username is deleted.

3. You will have to confirm your identity to view all the usernames in a vault. You can confirm it by entering any of your 
   username and password in that vault.
   Eg: If you want to view all the usernames registered in the vault 'Random', you will have to confirm your identity by 
   entering any of your username and password that exists inside the vault 'Random'.

4. If you want to modify your password for any username, you will have to confirm your identity by typing in your old 
   password.

5. If you forget your password, you can retain it after confirming your identity by entering the MASTER PASSWORD.

6. To delete an ENTRY, you will have to enter the username and password which you want to delete. Password dismatch will 
   lead to UNSUCCESSFUL ATTEMPT.

7. Deleting a VAULT will also require you to confirm your identity.You can confirm it by entering any of your username and 
   password in that vault. As such please note that an empty vault cannot be deleted.
```
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
