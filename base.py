import mysql.connector as c

f = open('file.txt','r')
x = f.read()
username = (x.split('\n'))[0]
password = (x.split('\n'))[1]
f.close()

db = c.connect(host='localhost',user=username,passwd=password)
mc = db.cursor()

mc.execute('create database if not exists Password')
mc.execute('use Password')

M_PASS = '1t520th1n6'         #MASTER PASSWORD
PASS = input('Enter the Master Password to gain access to the application: ')

while PASS == M_PASS:
    print('-----------------------------------------------')
    print('''Welcome to Password Manager! Choose any of the following to continue
1. Create Password Vault
2. Add an entry to your Vault
3. Display all usernames in a Vault
4. Modify password
5. Forgot your password
6. Delete an entry from your Vault
7. Display all Vaults
8. Delete Vault
9. Exit Application''')
    ch = input('Enter your choice(1-9): ')

    #CreateVault
    if ch == '1':
        tb = input('\nEnter name of vault: ')                #tb -> table_name
        tb_name = tuple(tb.split(' '))              #table name in the form of a tuple
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            print('\nVault already exists\n')
        else:
            mc.execute('create table {}(Username varchar(20) NOT NULL, Password varchar(50) NOT NULL)'.format(tb))
            print('\nSTATUS : Vault successfully created!\n')
            db.commit()

    #AddEntry
    elif ch == '2':
        tb = input('\nEnter Vault name: ')
        tb_name = tuple(tb.split(' '))              #table name in the form of a tuple
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            print('Enter the username and password to save it into the vault')
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                print('\nUsername already exists!\n')
            else:
                pswd = input('Enter password: ')
                mc.execute('insert into %s values("%s","%s")' %(tb,usrname,pswd))
                db.commit()
                print('\nSTATUS : Input Successful!\n')
        else:
            print('\nSorry, Invalid VaultName!')
            print('STATUS : Input UNSUCCESSFUL!\n')

    #DisplayUsernames
    elif ch == '3':
        tb = input('\nEnter Vault name: ')
        tb_name = tuple(tb.split(' '))
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            print('\nPlease confirm your identity')
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                pswd = input('Confirm your password: ')
                mc.execute('select Password from %s where Username="%s"' %(tb,str(usrname)))
                x = mc.fetchone()
                if pswd == x[0]:
                    mc.execute('select Username from {}'.format(tb))
                    x = mc.fetchall()
                    print('\nUsernames: ')
                    for i in x:
                        print(i)
                else:
                    print('\nYour password doesnot match with your Username')
                    print('STATUS : Attempt UNSUCCESSFUL!\n')
            else:
                print('\nInvalid UserName!')
                print('User not found!\n')
        else:
            print('\nSorry, Invalid VaultName!')
            print('Vault not found!\n')

    #ModifyPassword
    elif ch == '4':
        tb = input('\nEnter Vault name: ')
        tb_name = tuple(tb.split(' '))
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                pswd = input('Confirm your old password: ')
                mc.execute('select Password from %s where Username="%s"' %(tb,str(usrname)))
                x = mc.fetchone()
                if pswd == x[0]:
                    pswd_new = input('\nEnter new password: ')    
                    mc.execute('update %s set Password="%s" where Username="%s"' %(tb,str(pswd_new),str(usrname)))
                    db.commit()
                    print('\nSTATUS : Password successfully changed!\n')
                else:
                    print('\nYour Password doesnot match with your Username!')
                    print('STATUS : Password Modification UNSUCCESSFUL!\n')
            else:
                print('\nInvalid UserName!')
                print('User not found!\n')
        else:
            print('\nSorry, Invalid VaultName!')
            print('Vault not found!\n')

    #RetainPassword
    elif ch == '5':
        PASS = input('\nPlease confirm the Master Password to continue: ')
        if PASS != M_PASS:
            print('''\nUnauthorised login attempt detected
STATUS: User access DENIED!''')
            db.close()
            break
        tb = input('Enter Vault name: ')
        tb_name = tuple(tb.split(' '))
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                mc.execute('select Password from %s where Username="%s"' %(tb,str(usrname)))
                x = mc.fetchone()
                print('\nYour password: ',x[0],'\n')
            else:
                print('\nInvalid Username!')
                print('User not found!\n')
        else:
            print('\nSorry, Invalid VaultName')
            print('Vault not found!\n')

    #DeleteEntry
    elif ch == '6':
        tb = input('\nEnter Vault name: ')
        tb_name = tuple(tb.split(' '))
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            print('\nEnter your details below to delete the entry')
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                pswd = input('Confirm your password: ')
                mc.execute('select Password from %s where Username="%s"' %(tb,str(usrname)))
                x = mc.fetchone()
                if pswd == x[0]:
                    mc.execute('delete from %s where Username="%s"' %(tb,str(usrname)))
                    db.commit()
                    print('\nSTATUS : Entry successfully deleted!\n')
                else:
                    print('\nYour Password doesnot match with your Username')
                    print('STATUS : Entry Deletion UNSUCCESSFUL!\n')
            else:
                print('\nInvalid Username!')
                print('User not found!\n')
        else:
            print('\nSorry, Invalid VaultName!')
            print('Vault not found!\n')

    #ViewVaults
    elif ch == '7':
        PASS = input('\nPlease confirm the Master Password to continue: ')
        if PASS != M_PASS:
            print('''\nUnauthorised login attempt detected
STATUS: User access DENIED!''')
            db.close()
            break
        mc.execute('show tables')
        print('\nPassword Vaults:')
        for i in mc:
            print(i)

    #DeleteVault
    elif ch == '8':
        tb = input('\nEnter Vault name: ')
        tb_name = tuple(tb.split(' '))
        mc.execute('show tables')
        x = mc.fetchall()
        if tb_name in x:
            print('\nPlease confirm your identity')
            usrname = input('Enter username: ')
            usrname_tuple = tuple(usrname.split(' '))
            mc.execute('select Username from {}'.format(tb))
            x = mc.fetchall()
            if usrname_tuple in x:
                pswd = input('Confirm your password: ')
                mc.execute('select Password from %s where Username="%s"' %(tb,str(usrname)))
                x = mc.fetchone()
                if pswd == x[0]:
                    mc.execute('drop table {}'.format(tb))
                    db.commit()
                    print('\nSTATUS : Vault is successfully deleted!\n')
                else:
                    print('\nYour Password doesnot match with your Username')
                    print('STATUS : Vault Deletion UNSUCCESSFUL!\n')
            else:
                print('\nInvalid Username!')
                print('User not found!\n')
        else:
            print('\nSorry, Invalid VaultName!')
            print('Vault not found!\n')

    #ExitApplication
    elif ch == '9':
        print('\nThankyou, Have a great day!\n')
        break

    else:
        print('\nInvalid Input! Choose a number from the range 1-9\n')
        
else:
    print('''\nUnauthorised login attempt detected
STATUS : User access DENIED!\n''')
    db.close()

