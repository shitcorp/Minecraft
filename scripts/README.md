# Script - Docs

## check_backups.py

### Description:
- Checks for old backups and deletes them if they are too old
- Comes inhandy when the server is running out of disk space again

### Usage:
- Edit the configuration variables on top of the file
- Run the script with python like so:
  ```bash
  python3 scripts/check_backups.py
  ```

## attach.sh

### Description:
- Attaches to the docker container in which the minecraft server is running
- Detach command: `CTRL-p` `CTRL-q` 
### Usage:
- Just execute the script
  ```bash
  ./scripts/attach.sh
  ```