import asyncio
import sys
from telethon import TelegramClient
from telethon.tl.types import Chat, Channel
import msvcrt

api_id = '' # Replace with your API ID
api_hash = ''   # Replace with your API Hash
phone_number = ''   # Replace with your phone number 628xxxxx

client = TelegramClient('session_name', api_id, api_hash)

def get_user_input(group_name):
    print(f"\nLeave group: {group_name}")
    print("Press ENTER to leave, ESC to cancel: ", end='', flush=True)
    
    while True:
        key = msvcrt.getch()
        if key == b'\r':
            print("LEAVE")
            return True
        elif key == b'\x1b':
            print("CANCEL")
            return False

async def leave_all_groups():
    await client.start(phone_number)
    
    print("Retrieving group list...")
    
    dialogs = await client.get_dialogs()
    groups = []
    
    for dialog in dialogs:
        if isinstance(dialog.entity, Chat):
            groups.append(dialog.entity)
        elif isinstance(dialog.entity, Channel):
            groups.append(dialog.entity)
    
    if not groups:
        print("No groups found.")
        return
    
    print(f"Found {len(groups)} groups.")
    
    for group in groups:
        group_name = group.title
        
        if get_user_input(group_name):
            try:
                await client.delete_dialog(group)
                print(f"Successfully left group: {group_name}")
            except Exception as e:
                print(f"Failed to leave group {group_name}: {str(e)}")
        else:
            print(f"Cancelled leaving group: {group_name}")
    
    print("\nFinished processing all groups.")

async def main():
    try:
        await leave_all_groups()
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
