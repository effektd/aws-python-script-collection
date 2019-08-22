# Migrate AWS Organisation entities to a new target

This is a very simple and straightforward python script that will migrate an AWS Organisation entity id (e.g. Organisation ID `ou-zfdp-88qel781` or AWS Account Numbers: `845227215716`) to a desired AWS Organisation target ID (e.g. A root account id: `r-zfdp` or an organisational unit id: `ou-zfdp-88qel781` ).

You can place as many targets as you like in the `source_ids.txt` file, however they must be each on a new line. You may also mix and match between id types.

**NOTE**: It is generally not recommended to move both organisationtial units and accounts in the same execution (unless you know what you're doing)

## How to use it

- Navigate to the parent directory containing `script.py`
- Populate the `source_ids.txt` file with the entities you wish to migrate
- Login to your AWS Organisations master/root account with sufficent privlidges
- You need to pass in the desired destination/target for your source ids to be migrated to
- Run the following command `python script.py <target id>`
    - Example `python script.py ou-zfdp-88qel781`
- The script will provide a total count of detected source ids and then proceed to migrate each source id one by one
- The script will notify you if a source id has already been migrated to the desired target id
- The script will not handle any exceptions other than the source id being already migrated
- Once the script has completed you will be notified
- It is recommended you verify the migrations via the UI or CLI to confirm success
