import boto3
import sys

if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("[ERROR] You have passed in an invalid target-id, example target-id is ou-zhz0-prn5fmbc")
        sys.exit()
    else:
        print("[INFO] Valid argument detected, proceeding with account migration")
        destination_id = str(sys.argv[1])

        # Gather source ids
        with open("source_ids.txt") as f:
            source_ids = f.read().splitlines()

        l = len(source_ids)    

        print("[INFO] Detected {} source id(s) to be migrated".format(l))
        print("[INFO] Beginning processing of source id(s)...")
        
        # Process the source ids for migration
        client = boto3.client('organizations')

        for source_id in source_ids:
            print("[INFO] Now attempting to move source id: {}".format(source_id))
            get_parent = client.list_parents(ChildId=source_id)
            parent_id = get_parent["Parents"][0]["Id"]
    
            try:
                response = client.move_account(
                    AccountId=source_id, SourceParentId=parent_id, DestinationParentId=destination_id
                )
                print("[INFO] Successfully moved source id: {} to target id: {}".format(source_id, destination_id))
            except client.exceptions.DuplicateAccountException:
                print("[NOTICE] Source id: {} is already migrated to target id: {}".format(source_id, destination_id))

        print("[INFO] Successfully migrated required accounts.")
