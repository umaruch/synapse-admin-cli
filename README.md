### Description
Synapse server administration tools

### Roadmap
- [*] Login
- [*] Register new one user
- [*] Register new users from file
- [*] Add one user to room
- [*] Add list users to rooms

### Install
Download latest version

`
pip install .\dist\synapse_admin-0.0.1-py3-none-any.whl
`

### Commands
Add base server url and login as admin
`
synapse-admin init
`

Register new user
`
synapse-admin register (--setdisplayname for authomatic change display name)
`

Register multiple user from file
`
synapse-admin register --file path_to_file (--setdisplayname for authomatic change display name)
`

File must been format:
username;displayname;is_admin(0,1)


Add user to room
`
synapse-admin users addroom
`

Add multiple users to multiple rooms
`
synapse-admin users addroom --file path_to_file
`
File must been format:
user_id;room_id

